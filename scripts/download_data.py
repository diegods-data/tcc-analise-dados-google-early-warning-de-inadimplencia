"""Baixa séries públicas do BCB/SGS e datasets do Kaggle (opcional).

Este script lê variáveis de ambiente a partir de `.env` para determinar
os diretórios de destino e utiliza as bibliotecas `requests` e `pandas` para
persistir os dados como CSV. Para baixar datasets do Kaggle, é necessário
ter o arquivo `kaggle.json` configurado em `~/.kaggle/`.
"""

import os
from pathlib import Path
import requests
import pandas as pd

try:
    from dotenv import load_dotenv
except ImportError:
    # Caso python-dotenv não esteja instalado, definimos um stub simples.
    def load_dotenv(*args, **kwargs):
        pass

def main() -> None:
    # Carrega variáveis do .env se existir
    load_dotenv()
    raw_dir = Path(os.getenv("RAW_DIR", "./data/raw"))
    raw_dir.mkdir(parents=True, exist_ok=True)

    fetch_bcb_selic(raw_dir)
    fetch_kaggle_dataset(raw_dir, dataset="mlg-ulb/creditcardfraud")


def fetch_bcb_selic(raw_dir: Path) -> None:
    """Baixa a série da taxa SELIC (código 11) da API SGS em formato CSV."""
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        print(f"Erro ao baixar SELIC do BCB: {exc}")
        return

    df = pd.DataFrame(data)
    df.rename(columns={"data": "date", "valor": "selic"}, inplace=True)
    df.to_csv(raw_dir / "bcb_selic.csv", index=False)
    print(f"Série SELIC salva em {raw_dir / 'bcb_selic.csv'}")


def fetch_kaggle_dataset(raw_dir: Path, dataset: str) -> None:
    """Baixa um dataset do Kaggle, se a API estiver configurada."""
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print("Biblioteca kaggle não instalada; pulando download do Kaggle.")
        return

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as exc:
        print(f"Falha ao autenticar na API Kaggle: {exc}\n" "Coloque kaggle.json em ~/.kaggle/ para habilitar downloads.")
        return

    target_dir = raw_dir / "kaggle_credit"
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"Baixando dataset {dataset} para {target_dir}…")
    try:
        api.dataset_download_files(dataset, path=str(target_dir), quiet=False, unzip=True)
        print(f"Dataset Kaggle salvo em {target_dir}")
    except Exception as exc:
        print(f"Erro ao baixar dataset do Kaggle: {exc}")


if __name__ == "__main__":
    main()
