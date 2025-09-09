"""Executa os scripts SQL em ordem dentro de um banco DuckDB em memória.

Este utilitário permite testar e materializar as tabelas criadas nos scripts
`sql/00_create_base.sql`, `sql/01_ingest_sgs.sql` e `sql/02_features_ews.sql` sem
precisar de um SGBD externo. Após a execução, é possível exportar as tabelas
para CSVs em `data/processed/` utilizando o comando COPY do DuckDB.
"""

import os
from pathlib import Path
import duckdb

SQL_DIR = Path("sql")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    # Conexão em memória
    con = duckdb.connect(database=":memory:")

    # Exemplo de carregamento de uma tabela CSV previamente processada (ajuste conforme seu fluxo)
    macro_csv = OUT_DIR / "macro_selic_features.csv"
    if macro_csv.exists():
        con.execute(
            """
            CREATE OR REPLACE TABLE macro_selic AS
            SELECT * FROM read_csv_auto(?);
            """,
            [str(macro_csv)],
        )
        print("Tabela macro_selic criada.")

    # Executa os scripts SQL em ordem, se existirem
    for sql_file in ["00_create_base.sql", "01_ingest_sgs.sql", "02_features_ews.sql"]:
        path = SQL_DIR / sql_file
        if not path.exists():
            print(f"{path} não encontrado; pulando.")
            continue
        print(f"Executando {path}...")
        sql_text = open(path, "r", encoding="utf-8").read()
        con.execute(sql_text)

    # Exemplo: exporte a tabela final (substitua `ews_join` pelo nome correto)
    # try:
    #     con.execute("COPY ews_join TO ? (HEADER, DELIMITER ',');", [str(OUT_DIR / "ews_join.csv")])
    #     print("ews_join.csv exportado para data/processed.")
    # except Exception as exc:
    #     print(f"Erro ao exportar tabela: {exc}")


if __name__ == "__main__":
    main()
