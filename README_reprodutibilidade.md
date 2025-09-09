# Atualização – Reprodutibilidade

Esta atualização descreve como configurar o ambiente e rodar o pipeline para o Case A – Early‑warning de Inadimplência (EWS).

## Configuração do ambiente

1. Clone este repositório.
2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Copie `.env.example` para `.env` e ajuste os caminhos se necessário (por padrão, os dados ficam em `data/raw` e `data/processed`).

## Pipeline automatizado

O `Makefile` simplifica a execução das etapas do projeto:

- `make setup` – cria o ambiente virtual e instala as dependências.
- `make data` – baixa as séries do Banco Central (e, se configurado, um dataset do Kaggle) para `data/raw/`.
- `make features` – gera variáveis derivadas em `data/processed/` a partir dos CSVs brutos.
- `make notebooks` – executa os notebooks usando Papermill e salva cópias `.out.ipynb`.
- `make clean` – remove arquivos temporários gerados na pasta `data/processed/` e as saídas dos notebooks.

Se preferir não usar `make`, execute manualmente:

```bash
python scripts/download_data.py
python scripts/build_features.py
```

## Uso do Kaggle (opcional)

Para baixar datasets públicos do Kaggle, você precisa ter um arquivo `kaggle.json` com suas credenciais em `~/.kaggle/`. Caso contrário, os scripts ignoram essa parte sem gerar erro.

## Dashboards

Após gerar os arquivos em `data/processed/`, conecte-os nos dashboards:

- **Tableau**: vá em **Data > New Data Source > Text File** e selecione `data/processed/macro_selic_features.csv` (e demais CSVs). Estabeleça as relações entre as tabelas, crie visualizações e publique no Tableau Public.
- **Power BI**: use **Obter Dados > Texto/CSV**, selecione os mesmos arquivos e defina os tipos de dados. Crie medidas em DAX (ex.: taxa de inadimplência, variação mensal da SELIC) e monte seu dashboard. 

Com esses artefatos, qualquer usuário poderá reproduzir o pipeline, gerar as bases e construir os dashboards descritos no case.