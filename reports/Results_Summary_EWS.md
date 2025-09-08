# Results Summary — Early‐Warning de Inadimplência

Este resumo destaca os principais achados obtidos a partir da análise exploratória e da construção do Early‐Warning System (EWS) para inadimplência.

## Principais insights

- **Correlação defasada:** identificou-se correlação positiva entre a taxa SELIC/taxa de juros PF e a inadimplência total PF em defasagens de 3 a 6 meses, sugerindo que aumentos de juros antecedem picos de inadimplência.
- **Indicador de risco composto:** a combinação das variáveis derivadas (z-scores de inadimplência rotativa, juros PF, SELIC e concessões PF) resultou em um índice capaz de sinalizar “janelas críticas” em que a probabilidade de deterioração da carteira é maior.
- **Segmentos de alerta:** os quadrantes com inadimplência alta e juros altos representam períodos onde políticas de concessão e ações de cobrança devem ser mais agressivas.

## Recomendações

1. **Cobrança preventiva:** iniciar contato com clientes em potencial atraso quando o índice de risco ultrapassar o percentil 95 histórico.
2. **Ajuste de política de crédito:** em ciclos de alta de juros e aumento de inadimplência rotativa, reduzir limites e endurecer critérios de aprovação.
3. **Atualização contínua:** revisar o cálculo do índice e os limiares a cada 12 meses, incorporando novos dados ou indicadores macroeconômicos (inflação, desemprego) quando disponível.

## Limitações

- Os dados são agregados por modalidade; sem microdados de DPD individuais, o alerta serve como proxy macroeconômico.
- Possíveis revisões metodológicas nas séries do BCB podem alterar os resultados. É recomendável versionar as extrações.
