# 04_Despesas Gavea

## Identity

Workstation de gestão financeira do imóvel Gávea. O registro de despesas acontece via app web (despesas-gavea.onrender.com) — os funcionários fotografam a nota e o app salva no Google Sheets. Esta workstation cuida do que vem depois: relatórios, aprovação de reembolsos, análise de gastos e melhorias no app. Não chega aqui: tarefas de outros imóveis.

## Resources

| Resource | Read when... |
| :---- | :---- |

## Workflow

1. **Relatório de despesas:** consultar planilha Sheets por período, consolidar por categoria, apresentar em texto direto com tabela resumo no final.
2. **Reembolso:** identificar despesas pendentes, confirmar aprovação, registrar status na planilha (pendente → aprovado).
3. **Melhorias no app:** alterações vão em `04_Despesas Gavea/app/`, commit e push para `main` — Render faz deploy automático.
4. **Problema no app:** verificar logs no dashboard do Render antes de qualquer alteração no código.

## Editorial Rules

Siga meus princípios de voz em 00_Resources (voice-principles.md).

- Valores em R$ com duas casas decimais (ex: R$ 1.234,56).
- Datas no formato DD/MM/AAAA.
- Relatórios em texto corrido com tabela de resumo no final — sem excesso de subtítulos.
- Nomes de fornecedores exatamente como aparecem na nota fiscal.
