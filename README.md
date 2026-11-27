# Análise de Desigualdade Salarial e Poder de Compra por Gênero (RAIS SP & C&A)

## 1. Objetivo e Hipóteses
Este projeto investiga o impacto duplo da desigualdade de gênero no consumo cotidiano, cruzando dados censitários de remuneração do mercado formal paulista com a precificação de peças de vestuário equivalentes no varejo.

- **H1:** O gap salarial entre homens e mulheres persiste mesmo após normalização por carga horária e escolaridade.
- **H2:** Itens equivalentes de vestuário apresentam precificação superior no segmento feminino (*Pink Tax*).
- **H3:** O esforço de compra (medido em horas de trabalho necessárias por peça) é substancialmente maior para mulheres.

## 2. Fontes de Dados e Metodologia
- **Mercado de Trabalho (RAIS - Ministério do Trabalho / PDET):** 14.934.483 vínculos ativos válidos no estado de São Paulo (após filtragem de ativos em 31/12 e remoção de *outliers* extremos). Processamento em lote via Python (`pandas` com *chunking*).
- **Varejo de Vestuário (C&A):** Amostra de peças equivalentes coletadas por departamento (`Feminino` e `Masculino`).
- **Métricas:** Uso de **mediana (Q2)** e **intervalo interquartil (Q1–Q3)** para evitar distorção causada pela assimetria salarial e de preços.

## 3. Principais Resultados

### 3.1. Desigualdade Salarial (RAIS - SP)
| Indicador | Feminino | Masculino | Diferença / Gap |
| :--- | :---: | :---: | :---: |
| Vínculos Ativos | 6.919.507 (46,33%) | 8.014.976 (53,67%) | -7,34 p.p. |
| Mediana Salarial Mensal | R$ 2.655,44 | R$ 3.210,03 | **-17,28%** (-R$ 554,59) |
| Mediana Salário-Hora | R$ 14,59/h | R$ 17,08/h | **-14,55%** (-R$ 2,49/h) |
| Gap no Ensino Superior | R$ 5.312,48 | R$ 6.956,08 | **-23,63%** |
| Gap na Pós-Graduação | R$ 10.320,46 | R$ 14.366,03 | **-28,16%** |

### 3.2. Precificação no Varejo (C&A)
*(Em atualização após integração de `dados/processed/roupas_cea_limpo.csv`)*

### 3.3. Impacto no Poder de Compra (Esforço em Horas)
*(Em atualização no notebook `notebooks/analise_conjunta.ipynb`)*

## 4. Estrutura do Repositório
- `coleta_salarios.py` e `coleta_roupas.py`: scripts de extração e higienização em lote.
- `dados/processed/`: tabelas agregadas e limpas utilizadas nas análises.
- `notebooks/`: análises exploratórias individuais e cruzamento conjunto.
