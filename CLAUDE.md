# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Memory System

Ao início de cada sessão, leia MEMORY.md antes de responder. Use o que encontrar para informar o trabalho — sem anunciar o que leu.

Quando eu disser "lembre-se disso" (ou "remember this"), escreva imediatamente no MEMORY.md e confirme.

Escreva estes arquivos e notas em português.

**Onde guardar:** Comportamento prescritivo ("sempre", "nunca", "antes de X faça Y") → este arquivo. Fatos que podem mudar (contatos, status, decisões) → MEMORY.md. Na dúvida, sugira e confirme.

## Preferences

- Tom profissional mas conversacional. Se soar como memo corporativo, reescreva.
- Respostas concisas, menos de 300 palavras salvo se pedir mais.
- Listas em bullet points; explicações em parágrafos.
- Uma recomendação forte. Só dê alternativas se eu pedir.

## Rules

- **Controle da máquina:** Antes de usar qualquer ferramenta de controle do computador, verificar permissão explícita. Pedir antes de agir.
- Faça perguntas de clarificação antes de iniciar tarefas complexas.
- Ao redigir e-mails: combine a formalidade do original. Verifique se já existe thread com o destinatário antes de criar novo.
- Se não tiver certeza, diga. Não chute.
- Antes de produzir qualquer conteúdo em meu nome, leia voice-principles.md em 00_Resources.
- Workstations usam numeração sequencial de 2 dígitos: 00_nome, 01_nome, 02_nome, etc.

## Routing Map

| Workstation | Route here when I... |
| :---- | :---- |
| 01_Leitor de Livros | ...pedir resumo de um livro, registrar pontos-chave, ou organizar leituras no Notion |
| 02_Ana Coutinho | ...trabalhar na marca, press kit, obras, projetos ou administrativo da Ana Coutinho |
| 03_Latam RJ-SP | ...buscar voos ponte aérea SP-RJ, comparar tarifas Latam, planejar embarque Congonhas/Santos Dumont |
| 04_Despesas Gavea | ...registrar despesas, categorizar gastos, controlar reembolsos ou gerar relatórios do imóvel Gávea |

## References

| Resource | Read when... |
| :---- | :---- |
| voice-principles.md | Writing any content on my behalf |

## Skills Locais

| Skill | Invocar quando... |
| :---- | :---- |
| `/frontend-design` | Criar ou redesenhar qualquer interface web (HTML, React, landing page, dashboard) |

## Desenvolvimento — 04_Despesas Gavea

App FastAPI que usa Anthropic (leitura de notas fiscais), Google Sheets (banco de dados) e Twilio (notificações WhatsApp). Código em `04_Despesas Gavea/app/`.

**Rodar localmente:**

```bash
cd "04_Despesas Gavea/app"
pip install -r requirements.txt
uvicorn main:app --reload
```

**Variáveis de ambiente necessárias** (`.env` na pasta `app/`):

- `ANTHROPIC_API_KEY`
- `GOOGLE_SHEETS_CREDENTIALS` (JSON da service account)
- `GOOGLE_SPREADSHEET_ID`
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM`, `TWILIO_TO`

**Deploy:** push para `main` → Render faz deploy automático em `despesas-gavea.onrender.com`.

## GitHub Actions

`claude.yml` na raiz configura o Claude Code Action: responde a comentários em issues/PRs e processa issues abertas ou atribuídas automaticamente.

## Creating New Workstations

Criar subpasta `NN_Nome` com três itens:

1. **CLAUDE.md** — seções: Identity, Resources (tabela), Workflow (passos numerados), Editorial Rules (abre com voice-principles).
2. **MEMORY.md** — cabeçalho `NN_Nome Memory`, seções Contatos e Decisões-chave.
3. **NN_Nome Resources/** — pasta vazia para arquivos de referência.

Adicionar linha ao Routing Map acima.
