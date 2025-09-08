# TCC – Early‐Warning de Inadimplência (EWS)

Este repositório contém uma estrutura inicial para o **Case A – Early‐warning de Inadimplência (0–30→90+ DPD)**, parte de um Trabalho de Conclusão de Curso (TCC) em Análise de Dados. O objetivo é construir um pipeline reprodutível que permita prever a deterioração da carteira de crédito utilizando apenas dados públicos fornecidos pelo Banco Central do Brasil (BCB).

## Estrutura de pastas

```
data/
  raw/         # dados brutos extraídos das APIs do BCB (CSV)
  processed/   # dados já limpos e integrados (CSV)
notebooks/
  01_ews_inadimplencia_eda.ipynb   # exploração dos dados e análise gráfica
  02_ews_modelagem.ipynb           # construção do índice de risco e modelos de alerta
sql/
  00_create_base.sql               # criação de tabelas base
  01_ingest_sgs.sql                # ingestão das séries da SGS/BCB
  02_features_ews.sql              # transformações e cálculo de variáveis
dashboard/
  tableau/                         # dashboards Tableau (.twbx)
  powerbi/                         # dashboards Power BI (.pbix)
reports/
  Data_Cleaning_Log.md             # registro de limpeza de dados
  Results_Summary_EWS.md           # resumo dos principais achados
```

## Sobre os dados

As séries utilizadas neste case são públicas e estão disponíveis através da API de séries temporais do BCB (SGS). Alguns códigos de séries relevantes:

- **21084**: inadimplência total pessoas físicas (% da carteira com atraso >90 dias)
- **21127**: inadimplência cartão de crédito rotativo (PF)
- **21113**: inadimplência cheque especial (PF)
- **21151**: inadimplência financiamento imobiliário direcionado (PF)
- **11**: taxa SELIC diária (necessário agregação mensal)
- **20633**: concessões de crédito PF (R$ milhões)

Consulte o portal de dados do BCB para obter metadados e as instruções de acesso via API.

## Reproduzindo o projeto

1. **Extrair os dados**: baixe cada série da SGS utilizando as URLs informadas na documentação ou conforme os scripts de ingestão em `sql/01_ingest_sgs.sql`. Salve os CSVs em `data/raw/`.
2. **Criar as tabelas base**: use o script `sql/00_create_base.sql` para criar as tabelas em um SGBD (ex.: PostgreSQL).
3. **Ingestão**: carregue os CSVs nas tabelas correspondentes e execute `sql/01_ingest_sgs.sql`.
4. **Transformações e features**: rode `sql/02_features_ews.sql` para gerar a base `ews_join` com variáveis de interesse e seus derivados (deltas, EMAs, z-scores, etc.).
5. **Exploração e modelagem**: abra os notebooks em `notebooks/` para reproduzir a análise exploratória (EDA) e a construção do índice de risco ou modelo de classificação. Os notebooks contêm células vazias para que você adicione seu código Python.
6. **Dashboards**: utilize os arquivos de dados processados (`data/processed/ews_join.csv`, `lead_lag_corr.csv`, `risk_matrix.csv`) para montar os dashboards no Tableau e Power BI. Os diretórios `dashboard/` contêm arquivos vazios (`.gitkeep`) para preservar a estrutura; salve seus `.twbx` e `.pbix` aqui.

## Licença

As séries temporais utilizadas neste projeto estão licenciadas sob [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/) conforme informado pelo Banco Central do Brasil. O conteúdo deste repositório está sob a licença MIT.
