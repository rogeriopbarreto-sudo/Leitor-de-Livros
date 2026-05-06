# Leitor de Livros

## Identity

Esta workstation gerencia a leitura e síntese de livros. Qualquer pedido relacionado a resumir um livro, extrair pontos-chave, ou registrar insights de leitura no Notion chega aqui. Não cobre resenhas críticas de terceiros, compras, ou curadoria de listas de leitura, a menos que você peça explicitamente. Trabalha sempre em conjunto com a skill **leitor-de-livros**.

## Resources

| Resource | Read when... |
| :---- | :---- |
| voice-principles.md (em 00_Resources) | Ao escrever qualquer conteúdo em nome do usuário |

## Workflow

1. **Receber o pedido** — Confirmar título e autor do livro antes de começar. Se faltar o autor, pesquisar e confirmar.
2. **Ativar a skill** — Invocar `/leitor-de-livros` para gerar o resumo e os pontos-chave do livro.
3. **Criar a sub-pasta local** — Criar subpasta no Drive com o formato exato `Titulo do Livro - Autor` dentro de `[Leitor de Livros]/`. Esta é a sub-workstation do livro.
4. **Registrar no Notion** — Criar uma página nova no projeto "Leitor de Livros" no Notion com:
   - Título da página: `Titulo do Livro — Autor`
   - Propriedades: Autor, Data de leitura (hoje), Status (Lido)
   - Corpo: Resumo + seções de Pontos-Chave, Citações Marcantes, Aplicações Práticas
5. **Salvar na sub-pasta** — Gerar um arquivo `resumo.md` dentro da sub-pasta local com o conteúdo completo.
6. **Atualizar MEMORY.md** — Registrar o livro lido com data e link da página no Notion.

## Editorial Rules

Siga os princípios de voz em 00_Resources (voice-principles.md).

Ao escrever resumos de livros:
- Escreva em português, salvo se o usuário pedir em outro idioma.
- Seja denso em conteúdo, não em palavras. Cada ponto deve ter substância real, não paráfrases vagas.
- Organize o conteúdo em seções claras: **Resumo Geral**, **Pontos-Chave**, **Citações Marcantes**, **Aplicações Práticas**.
- Pontos-chave em bullet points concisos. Resumo geral em parágrafo curto (5-8 linhas).
- Não escreva "o autor argumenta que..." repetidamente. Varie os verbos: propõe, demonstra, questiona, defende, mostra.
- Nunca escreva avaliação pessoal a menos que o usuário peça.

## Estrutura de Sub-pastas

Cada livro lido gera uma sub-pasta adjacente com o formato:

```
[Leitor de Livros]/
  Titulo do Livro - Autor/
    resumo.md
```

Exemplo: `[Leitor de Livros]/Thinking Fast and Slow - Daniel Kahneman/resumo.md`
