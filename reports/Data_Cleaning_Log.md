# Data Cleaning Log — Early‐Warning de Inadimplência

Este documento registra as principais etapas de limpeza e transformação dos dados utilizados no case de Early‐warning de inadimplência.

## Fontes e séries importadas

- **21084**: inadimplência total PF (% >90 dias)
- **21127**: inadimplência cartão rotativo PF
- **21113**: inadimplência cheque especial PF
- **21151**: inadimplência financiamento imobiliário direcionado PF
- **11**: taxa SELIC diária (agregada para média mensal)
- **20633**: concessões PF (milhões de reais)

## Passos de limpeza

1. **Conversão de datas:** todas as colunas de data foram convertidas para o formato ISO `YYYY-MM` ou `YYYY-MM-DD`, conforme necessário.
2. **Tipos numéricos:** as colunas de valores foram convertidas para `numeric`/`decimal`, com tratamento de vírgulas e pontos decimais.
3. **Agregação da SELIC:** a série diária da SELIC (código 11) foi agregada em média mensal para alinhar com as séries de inadimplência, respeitando a janela de 10 anos por consulta recomendada pela API.
4. **Mesclagem de dados:** as séries foram unificadas por data (mês) em uma tabela central (`ews_join`) utilizando `LEFT JOIN` para manter a cobertura máxima.
5. **Criação de variáveis derivadas:** foram calculados deltas mensais (1m, 3m, 12m), médias móveis exponenciais (EMA 3m/6m) e scores padronizados (z-scores) para cada variável de interesse.
6. **Tratamento de outliers:** valores extremos foram suavizados por `winsorize` a 1% e 99% quando necessário para estabilizar as transformações.
7. **Controle de versões:** cada extração de dados recebeu timestamp e hash simples para rastreabilidade.

## Observações

- As séries do Banco Central são passíveis de revisões. Recomenda-se checar periodicamente se houve atualizações ou metodologias novas.
- Este log deve ser atualizado sempre que novas etapas de limpeza ou transformação forem realizadas.
