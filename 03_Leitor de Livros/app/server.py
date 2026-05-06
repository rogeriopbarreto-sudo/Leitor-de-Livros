import os
import json
import threading
from datetime import date
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import anthropic
import requests as req
from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / ".env"
if not dotenv_path.exists():
    dotenv_path = Path(__file__).parent.parent / "Leitor de Livros Resources" / ".env"
load_dotenv(dotenv_path)

HISTORY_FILE = Path(__file__).parent / "history.json"
_history_lock = threading.Lock()

def _load_history():
    try:
        if HISTORY_FILE.exists():
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except Exception:
        pass
    return []

def _save_history(entries):
    try:
        HISTORY_FILE.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as e:
        app.logger.error("history write error: %s", e)

def _add_to_history(entry):
    with _history_lock:
        h = _load_history()
        h = [e for e in h if not (e.get("title") == entry["title"] and e.get("author") == entry["author"])]
        h.insert(0, entry)
        _save_history(h[:10])

app = Flask(__name__, static_folder=".")

limiter = Limiter(
    get_remote_address, app=app,
    default_limits=["200 per day", "30 per minute"],
    storage_uri="memory://"
)

SYSTEM_PROMPT = """Você é um sintetizador de livros especializado. Crie resumos ricos e densos em português, independente do idioma original.

Estruture com estas quatro seções (use ## para os títulos):

## Resumo Geral
Parágrafo de 5 a 8 linhas com a essência e proposta central do livro.

## Pontos-Chave
Entre 6 e 10 bullet points concisos. Cada ponto com substância real, sem paráfrases vagas.

## Citações Marcantes
Ideias ou frases mais impactantes em blockquote (> ...). Citações diretas ou paráfrases fiéis.

## Aplicações Práticas
4 a 6 bullet points específicos e acionáveis para o dia a dia.

Regras: seja denso em conteúdo. Varie os verbos: propõe, demonstra, questiona, defende, mostra, explora, revela. Não repita "o autor argumenta que" mais de uma vez. Sem avaliação pessoal."""


@app.after_request
def security_headers(r):
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.headers["X-Frame-Options"] = "DENY"
    r.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    r.headers["X-XSS-Protection"] = "1; mode=block"
    return r


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/history")
def history_list():
    with _history_lock:
        return jsonify(_load_history())


@app.route("/api/search")
@limiter.limit("30 per minute")
def search():
    q = request.args.get("q", "").strip()[:100]
    if not q:
        return jsonify([])
    try:
        r = req.get(
            "https://openlibrary.org/search.json",
            params={"q": q, "limit": 6, "fields": "title,author_name,language,cover_i"},
            timeout=10
        )
        r.raise_for_status()
        books = [{
            "title":   d.get("title", "")[:200],
            "authors": [a[:100] for a in d.get("author_name", [])[:3]],
            "lang":    "pt" if any(l in ("por", "pt") for l in d.get("language", [])) else "en",
            "thumb":   f"https://covers.openlibrary.org/b/id/{d['cover_i']}-M.jpg" if d.get("cover_i") else "",
        } for d in r.json().get("docs", [])]
        return jsonify(books)
    except Exception as e:
        app.logger.error("search error: %s", e)
        return jsonify({"error": "Erro na busca"}), 502


@app.route("/api/summary", methods=["POST"])
@limiter.limit("5 per minute;50 per day")
def summary():
    try:
        data   = request.get_json(force=True, silent=True) or {}
        title  = str(data.get("title",  "")).strip()[:200]
        author = str(data.get("author", "")).strip()[:200]
        lang   = str(data.get("lang",   "en"))[:5]
        thumb  = str(data.get("thumb",  ""))[:500]

        if not title:
            return jsonify({"error": "Título obrigatório"}), 400

        key = os.getenv("ANTHROPIC_API_KEY", "").strip()
        if not key:
            app.logger.error("summary error: missing ANTHROPIC_API_KEY")
            return jsonify({"error": "Chave API não configurada. Configure ANTHROPIC_API_KEY no ambiente ou em um arquivo .env."}), 500

        lang_label = "Português (Brasil)" if lang == "pt" else "Inglês"
        client = anthropic.Anthropic(api_key=key)
        msg = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            timeout=30,
            system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f'Livro: "{title}"\nAutor: {author}\nIdioma: {lang_label}'
                        }
                    ]
                }
            ]
        )

        summary_text = ""
        if msg and getattr(msg, "content", None):
            first_block = msg.content[0]
            summary_text = getattr(first_block, "text", "") or str(first_block)

        if not summary_text:
            app.logger.error("summary error: Anthropic returned empty content: %s", msg)
            return jsonify({"error": "Resposta vazia do Anthropic"}), 502

        try:
            _add_to_history({
                "date":    date.today().isoformat(),
                "title":   title,
                "author":  author,
                "thumb":   thumb,
                "summary": summary_text,
                "lang":    lang,
            })
        except Exception:
            app.logger.exception("history add error")

        return jsonify({"summary": summary_text})

    except anthropic.AuthenticationError:
        return jsonify({"error": "Chave API inválida"}), 401
    except anthropic.RateLimitError:
        return jsonify({"error": "Limite Anthropic atingido. Aguarde alguns minutos."}), 429
    except anthropic.BadRequestError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        app.logger.exception("summary error")
        return jsonify({"error": "Erro interno no servidor"}), 500


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(port=5000, debug=debug)
