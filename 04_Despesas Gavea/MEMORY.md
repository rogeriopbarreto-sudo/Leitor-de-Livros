# 04_Despesas Gavea — Memória

## Contatos

- **Service Account Google:** `despesas-gavea@astral-scout-461712-b3.iam.gserviceaccount.com`

## Decisões-chave

- **Stack:** FastAPI (Python 3.11) + Google Sheets (gspread) + frontend HTML puro
- **Design:** estilo "Mercado" — Fraunces + DM Sans, foto da Pedra da Gávea no header, botão câmera laranja
- **Câmera:** usa `capture="environment"` para abrir câmera traseira direto no celular
- **Total geral:** exibido de forma discreta no final da lista (não no topo)
- **Versão atual:** v1.0 (tag no GitHub)

## Planilha Google Sheets

- **ID:** `1ZM03UT3c49_SQUYjymFBSyxbcESGbmh2wr6PmUu4wAw`
- **Abas:** `expenses` e `price_items`
- **Projeto Google Cloud:** `astral-scout-461712-b3`

## App

- **URL produção:** [despesas-gavea.onrender.com](https://despesas-gavea.onrender.com)
- **GitHub:** [rogeriopbarreto-sudo/despesas-gavea](https://github.com/rogeriopbarreto-sudo/despesas-gavea)
- **Código local:** `04_Despesas Gavea\app\`
- **Deploy:** automático a cada push para `main`

## Próximas melhorias (a definir)

- Fluxo de aprovação e reembolso pelo Roger
- Autenticação para funcionários
