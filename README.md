# Desafio de Ciência de Dados

Este repositório representa a resposta ao desafio de previsão de qualidade em um processo de flotação, do início ao fim. O objetivo é mostrar a minha abordagem para a resolução de problemas em ciência de dados.
O foco está em **maturidade profissional**, **clareza de raciocínio**, **justificativa técnica** e **comunicação com stakeholders**, e **não** na maximização de métricas.

---

## Objetivo

Demonstrar uma abordagem estruturada, reprodutível e bem comunicada para avaliar o **potencial preditivo** dos dados de um processo de flotação, considerando que:

* o domínio do processo produtivo é limitado;
* o projeto é exploratório/piloto;
* o cliente aceita risco técnico inicial;
* a decisão de seguir ou não com o projeto depende da **qualidade da análise** e da **apresentação dos insight obtidos** , não apenas do modelo.

Além disso, o projeto busca responder explicitamente às seguintes questões:

* É possível prever o **% de Sílica no Concentrado** a partir de variáveis de processo?
* Com **quantas horas de antecedência** essa previsão é tecnicamente viável?
* É possível realizar essa previsão **sem utilizar variáveis de qualidade correlatas**, como o % de Ferro no Concentrado?

---

## Resumo

Este projeto demonstrou que **existe sinal preditivo mensurável** nos dados de processo para estimar o % de Sílica no Concentrado com antecedência horária, mesmo em um cenário de dados ruidosos, alta colinearidade e conhecimento limitado do processo.

As análises mostraram que:

* A variável alvo apresenta **forte dependência temporal**, o que torna baselines simples surpreendentemente competitivos;
* A agregação horária é coerente com o processo real de amostragem do target;
* Variáveis de processo químico e operacional (especialmente vazões e densidade) carregam informação relevante;
* A regularização é essencial para lidar com a alta dimensionalidade e multicolinearidade;
* Modelos lineares regularizados superam o baseline ingênuo, mas com ganhos marginais, o que é esperado em processos industriais estáveis.

Do ponto de vista de negócio, os resultados indicam que **há viabilidade técnica para uso preditivo**, desde que o modelo seja encarado como ferramenta de apoio à decisão, e não como mecanismo de controle automático.

## Princípios de Desenvolvimento

* Clareza > complexidade
* Justificativa > performance
* Organização > quantidade de código
* Comunicação > tuning

---

## Estrutura do Projeto

```text
mining-quality-prediction/
│
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── MiningProcess_Flotation_Plant_Database.csv
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_context_and_hypotheses.ipynb
│   ├── 02_data_understanding_and_quality.ipynb
│   ├── 03_exploratory_time_series_analysis.ipynb
│   ├── 04_feature_engineering_and_selection.ipynb
│   ├── 05_baseline_and_interpretable_models.ipynb
│   ├── 06_model_evaluation_and_business_insights.ipynb
│   └── 07_síntese.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── paths.py
│   ├── io.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── visualization.py
│   ├── models.py
│   └── metrics.py
│
├── reports/
│   ├── figures/
│   └── tables/
│
└── outputs/
    ├── models/
    └── metrics/
```

---

## Notebooks

### 01 — Contexto e Hipóteses

* Entendimento inicial do problema
* Limitações de domínio
* Formulação explícita de hipóteses
* Critérios de sucesso do estudo

### 02 — Entendimento e Qualidade dos Dados

* Estrutura do dataset
* Tipos de variáveis
* Problemas de coleta, duplicidade e coerência temporal
* Implicações para modelagem

### 03 — Condicionamento e Validação dos Dados

* Correção da dimensão temporal
* Tratamento de duplicidades
* Consolidação horária dos dados
* Geração do dataset analítico

### 04 — Análise Exploratória dos Dados

* Análise temporal das variáveis de processo
* Comportamento do target no tempo
* Autocorrelação, correlação local e decomposição

### 05 — Engenharia e Seleção de Features

* Criação de defasagens horárias
* Estatísticas agregadas
* Avaliação de redundância
* Seleção via correlação, VIF e Lasso

### 06 — Baselines e Modelos Interpretáveis

* Baseline de persistência
* Regressão linear clássica (OLS)
* Modelos com regularização (Ridge e Lasso)
* Avaliação comparativa

### 07 — Síntese (Resumo Executivo)

* Consolidação do raciocínio
* Avaliação das hipóteses iniciais
* Respostas aos objetivos do projeto
* Implicações práticas e limitações

---