# Perfil de Pessoas com Depressão no Brasil via Mineração de Dados

> Artigo publicado no **SBBD 2025** (Simpósio Brasileiro de Banco de Dados — Artigos Estendidos)  
> **PUC Minas**

[![Artigo](https://img.shields.io/badge/Artigo-SBBD%202025-blue)](https://sol.sbc.org.br/index.php/sbbd_estendido/article/view/37607)
[![Dados](https://img.shields.io/badge/Dados-PNS%202019-green)](https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-lightgrey)](LICENSE)

---

## Sobre o projeto

Este trabalho investiga o perfil socioeconômico, comportamental e clínico de pessoas diagnosticadas com depressão nas regiões **Sudeste** e **Centro-Oeste** do Brasil, utilizando técnicas de **mineração de dados** aplicadas aos microdados da **Pesquisa Nacional de Saúde (PNS) de 2019**.

A depressão é um transtorno de alta prevalência e impacto social no Brasil. A PNS 2019 oferece uma base de dados ampla e representativa que permite identificar padrões e fatores associados ao diagnóstico. O projeto passa por seleção de atributos, balanceamento de classes e treinamento de classificadores, culminando em uma análise comparativa dos modelos.

---

## Metodologia

```
PNS 2019 (microdados)
      │
      ▼
Extração e pré-processamento
      │
      ▼
Seleção de atributos
  ├── Análise de Entropia e Ganho de Informação
  ├── Filtragem por distribuição e entropia condicional
  └── Algoritmo Genético (Random Forest)
      │
      ▼
Balanceamento de classes
  ├── Undersampling (RandomUnderSampler)
  └── Oversampling (SMOTE)
      │
      ▼
Classificadores
  ├── Naive Bayes (GaussianNB)
  └── Random Forest (+ BayesSearchCV)
      │
      ▼
Avaliação: Accuracy, Precision, Recall, F1-score, F1 Macro
```

---

## Resultados

| Modelo | Balanceamento | Accuracy | F1 Macro |
|---|---|---|---|
| Naive Bayes | Original | 0.83 | 0.66 |
| Naive Bayes | Oversampling | 0.81 | 0.65 |
| Random Forest | Undersampling | 0.75 | 0.62 |
| Random Forest | Oversampling | 0.89 | 0.62 |
| Random Forest Otimizado | Oversampling | 0.89 | 0.62 |

O desbalanceamento de classes é o principal desafio: a classe com diagnóstico de depressão representa a minoria da base. O **undersampling** com Random Forest obteve o melhor recall para a classe minoritária (0.73), enquanto o **Naive Bayes** apresentou o melhor F1 Macro geral.

---

## Estrutura do repositório

```
├── article/                  # Artigo publicado no SBBD 2025
├── notebooks/
│   ├── 01_AnaliseEntropia.ipynb         # Cálculo de entropia e ganho de informação
│   ├── 02_Analise_Ganho_Filtro.ipynb    # Filtragem de atributos por ganho
│   ├── 03_Naive_Bayes_PNS.ipynb         # Classificador Naive Bayes
│   ├── 04_Random_Forest_PNS.ipynb       # Random Forest com BayesSearchCV
│   ├── 05_RF_PNS_Preholdout.ipynb       # Random Forest pré-holdout
│   ├── 06_Selecao_Genetica_RF.ipynb     # Seleção de atributos via algoritmo genético
│   └── 07_GerarTabela.ipynb             # Geração de tabelas de resultados
├── reports/
│   ├── Analise_Entropia.tex             # Análise de entropia e seleção de atributos
│   ├── AnaliseBayesEForest.tex          # Resultados dos classificadores
│   └── tabela-mapa0.tex                 # Mapa conceitual de atributos
├── data/
│   ├── processed/                       # Bases CSV tratadas e prontas para uso
│   └── raw/                             # Script de extração + dicionário PNS (SAS/XLS)
├── figures/                             # Gráficos de distribuição por estado e região
└── dictionaries/                        # Dicionário de variáveis da PNS 2019
```

---

## Como executar

### Pré-requisitos

```bash
pip install pandas numpy scikit-learn imbalanced-learn scikit-optimize seaborn matplotlib
```

### Ordem recomendada dos notebooks

1. `01_AnaliseEntropia` → seleção inicial de atributos
2. `02_Analise_Ganho_Filtro` → filtragem complementar
3. `03_Naive_Bayes_PNS` → baseline com Naive Bayes
4. `04_Random_Forest_PNS` → modelo principal
5. `05_RF_PNS_Preholdout` → validação pré-holdout
6. `06_Selecao_Genetica_RF` → refinamento via algoritmo genético
7. `07_GerarTabela` → consolidação dos resultados

> **Nota:** os notebooks utilizam a base `data/processed/database-am-6.csv` por padrão. Os dados brutos da PNS 2019 não estão incluídos no repositório por questão de tamanho — o script `data/raw/extraction.py` pode ser usado para extrair as colunas necessárias a partir do CSV completo da PNS.

---

## Dados

Os dados utilizados são os **microdados da PNS 2019** (IBGE), disponíveis publicamente em:  
https://www.ibge.gov.br/estatisticas/sociais/saude/9160-pesquisa-nacional-de-saude.html

A variável-alvo é **Q092** — diagnóstico médico de depressão. O foco geográfico são as regiões **Sudeste** e **Centro-Oeste** do Brasil.

---

## Citação

Se utilizar este trabalho, por favor cite:

```bibtex
@inproceedings{couto2025depressao,
  title     = {Descrevendo o perfil de pessoas com depressão nas regiões Sudeste e Centro-Oeste do Brasil por meio de Mineração de Dados},
  author    = {Couto, Pedro Grojpen and Alves, Glória Eleonor F. and Zárate, Luís Enrique},
  booktitle = {Anais Estendidos do XL Simpósio Brasileiro de Banco de Dados (SBBD)},
  year      = {2025},
  publisher = {SBC},
  url       = {https://sol.sbc.org.br/index.php/sbbd_estendido/article/view/37607}
}
```

---

## Autores

| Nome | Papel |
|---|---|
| Pedro Grojpen Couto | Autor |
| Glória Eleonor F. Alves | Autora |
| Luis Enrique Zárate | Orientador |

**Instituição:** Pontifícia Universidade Católica de Minas Gerais (PUC Minas)
