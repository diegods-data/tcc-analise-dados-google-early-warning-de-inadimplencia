-- 00_create_base.sql
-- Este script cria as tabelas base para armazenar as séries de inadimplência,
-- juros e concessões do Banco Central. Adapte os tipos e esquemas conforme o SGBD utilizado.

CREATE TABLE IF NOT EXISTS sgs_21084_npl_pf (
    dt DATE,
    valor NUMERIC
);

CREATE TABLE IF NOT EXISTS sgs_21127_npl_rot (
    dt DATE,
    valor NUMERIC
);

CREATE TABLE IF NOT EXISTS sgs_21113_npl_esp (
    dt DATE,
    valor NUMERIC
);

CREATE TABLE IF NOT EXISTS sgs_21151_npl_imo (
    dt DATE,
    valor NUMERIC
);

CREATE TABLE IF NOT EXISTS sgs_11_selic_diaria (
    dt DATE,
    valor NUMERIC
);

CREATE TABLE IF NOT EXISTS juros_pf_livres (
    dt DATE,
    taxa_am NUMERIC
);

CREATE TABLE IF NOT EXISTS sgs_20633_conc_pf (
    dt DATE,
    valor NUMERIC
);
