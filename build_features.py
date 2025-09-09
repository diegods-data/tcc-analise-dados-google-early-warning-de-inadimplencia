"""Gera variáveis derivadas a partir dos dados brutos.

Este script lê os CSVs em `data/raw/`, calcula algumas estatísticas simples
(médias móveis, variações relativas, z-scores) e grava novos CSVs em
`data/processed/`. A função para gerar features de crédito só é executada se
um dataset Kaggle estiver presente.
"""

import os
from pathlib import Path

import pandas as pd
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        pass


def main() -> None:
    load_dotenv()
    raw_dir = Path(os.getenv("RAW_DIR", "./data/raw"))
    processed_dir = Path(os.getenv("PROCESSED_DIR", "./data/processed"))
    processed_dir.mkdir(parents=True, exist_ok=True)

    build_macro_panel(raw_dir, processed_dir)
    build_credit_features_if_present(raw_dir, processed_dir)


def build_macro_panel(raw_dir: Path, processed_dir: Path) -> None:
    """Processa a série SELIC e calcula estatísticas básicas."""
    selic_path = raw_dir / "bcb_selic.csv"
    if not selic_path.exists():
        print(f"Arquivo {selic_path} não encontrado; rode `make data` primeiro.")
        return
    selic = pd.read_csv(selic_path, parse_dates=["date"], dayfirst=True)
    selic["selic"] = pd.to_numeric(selic["selic"], errors="coerce")
    selic = selic.dropna().sort_values("date")
    # Estatísticas de exemplo: média móvel de 7 dias e variação mensal (~21 dias úteis)
    selic["selic_ma7"] = selic["selic"].rolling(7).mean()
    selic["selic_mom"] = selic["selic"].pct_change(periods=21)
    out_path = processed_dir / "macro_selic_features.csv"
    selic.to_csv(out_path, index=False)
    print(f"Features macro salvas em {out_path}")


def build_credit_features_if_present(raw_dir: Path, processed_dir: Path) -> None:
    """Calcula z-scores simples para cada variável numérica de um dataset Kaggle se disponível."""
    kaggle_dir = raw_dir / "kaggle_credit"
    csv_files = list(kaggle_dir.glob("*.csv"))
    if not csv_files:
        print("Nenhum dataset Kaggle encontrado; pulando features de crédito.")
        return
    df = pd.read_csv(csv_files[0])
    for col in df.select_dtypes(include="number").columns:
        if df[col].std(ddof=0) == 0:
            df[f"{col}_z"] = 0.0
        else:
            df[f"{col}_z"] = (df[col] - df[col].mean()) / df[col].std(ddof=0)
    out_path = processed_dir / "credit_features.csv"
    df.to_csv(out_path, index=False)
    print(f"Features de crédito salvas em {out_path}")


if __name__ == "__main__":
    main()
