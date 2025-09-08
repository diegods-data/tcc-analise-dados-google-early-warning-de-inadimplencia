-- 02_features_ews.sql
-- Script que gera a tabela unificada e calcula variáveis derivadas para o Early‐warning System.

-- Agregar SELIC diária para média mensal
CREATE MATERIALIZED VIEW IF NOT EXISTS selic_mensal AS
SELECT
    DATE_TRUNC('month', dt)::DATE AS mes,
    AVG(valor) AS selic_media_ad
FROM sgs_11_selic_diaria
GROUP BY 1;

-- Tabela unificada
CREATE MATERIALIZED VIEW IF NOT EXISTS ews_join AS
SELECT
    m AS mes,
    t.valor  AS npl_pf_total,
    r.valor  AS npl_rotativo,
    e.valor  AS npl_especial,
    i.valor  AS npl_imo_dir,
    s.selic_media_ad,
    j.taxa_am AS juros_pf_am,
    c.valor  AS concessoes_pf_mi
FROM generate_series(
    (SELECT MIN(dt) FROM sgs_21084_npl_pf),
    (SELECT MAX(dt) FROM sgs_21084_npl_pf),
    INTERVAL '1 month'
) AS m
LEFT JOIN sgs_21084_npl_pf  t ON DATE_TRUNC('month', t.dt) = m
LEFT JOIN sgs_21127_npl_rot r ON DATE_TRUNC('month', r.dt) = m
LEFT JOIN sgs_21113_npl_esp e ON DATE_TRUNC('month', e.dt) = m
LEFT JOIN sgs_21151_npl_imo i ON DATE_TRUNC('month', i.dt) = m
LEFT JOIN selic_mensal       s ON s.mes = m
LEFT JOIN juros_pf_livres    j ON DATE_TRUNC('month', j.dt) = m
LEFT JOIN sgs_20633_conc_pf  c ON DATE_TRUNC('month', c.dt) = m
ORDER BY mes;

-- Exemplo de cálculo de deltas e z-scores (PostgreSQL)
-- É recomendado ajustar para seu SGBD; aqui apenas como referência:
-- ALTER MATERIALIZED VIEW ews_join ADD COLUMN npl_pf_delta_3m NUMERIC;
-- UPDATE ews_join e
-- SET npl_pf_delta_3m = e.npl_pf_total - LAG(e.npl_pf_total, 3) OVER (ORDER BY e.mes);
