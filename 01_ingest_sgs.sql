-- 01_ingest_sgs.sql
-- Script para carregar os CSVs exportados da API SGS nas respectivas tabelas.
-- Substitua os caminhos dos arquivos conforme sua estrutura local.

-- Exemplo de COPY (PostgreSQL):
-- COPY sgs_21084_npl_pf (dt, valor) FROM '/caminho/data/raw/21084.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
-- COPY sgs_21127_npl_rot (dt, valor) FROM '/caminho/data/raw/21127.csv' WITH (FORMAT csv, HEADER true);
-- COPY sgs_21113_npl_esp (dt, valor) FROM '/caminho/data/raw/21113.csv' WITH (FORMAT csv, HEADER true);
-- COPY sgs_21151_npl_imo (dt, valor) FROM '/caminho/data/raw/21151.csv' WITH (FORMAT csv, HEADER true);
-- COPY sgs_11_selic_diaria (dt, valor) FROM '/caminho/data/raw/11.csv' WITH (FORMAT csv, HEADER true);
-- COPY juros_pf_livres (dt, taxa_am) FROM '/caminho/data/raw/juros_pf.csv' WITH (FORMAT csv, HEADER true);
-- COPY sgs_20633_conc_pf (dt, valor) FROM '/caminho/data/raw/20633.csv' WITH (FORMAT csv, HEADER true);

-- Ajuste as opções de COPY de acordo com o SGBD (MySQL, SQLite, etc.).
