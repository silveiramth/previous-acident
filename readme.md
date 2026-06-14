# Titanic - Análise de Sobrevivência

Análise exploratória e modelo preditivo de sobrevivência dos passageiros do Titanic, utilizando o dataset clássico do Kaggle.

---

## Objetivo

Prever quais passageiros sobreviveriam ao naufrágio do Titanic com base em características como sexo, idade, classe da passagem e valor da tarifa.

---

## Tecnologias utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

## Etapas do projeto

### 1. Análise Exploratória de Dados (EDA)
- Percentual geral de sobreviventes: **38%**
- Taxa de sobrevivência por sexo: mulheres (74%) vs homens (19%)
- Taxa de sobrevivência por classe: 1ª (63%), 2ª (47%), 3ª (24%)
- Distribuição de idades e análise por faixas de valor da passagem

### 2. Limpeza dos dados
- Valores nulos em `Age` preenchidos com a média
- Valores nulos em `Fare` preenchidos com a mediana
- Variável `Sex` convertida para binário (0 = male, 1 = female)
- Variável `Embarked` convertida para numérico (0 = S, 1 = C, 2 = Q)

### 3. Feature Engineering
- Criação da coluna `FamilySize` (SibSp + Parch)
- Criação da coluna `IsAlone` (1 se viajava sozinho, 0 caso contrário)

### 4. Modelagem
- Modelo: `RandomForestClassifier` com `max_depth=5`
- Divisão treino/teste: 80% / 20% com `random_state=42`

---

## Resultados

| Métrica | Valor |
|---|---|
| Acurácia no conjunto de teste | **83%** |

---

## Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/titanic-analysis.git
```

2. Instale as dependências:
```bash
pip install pandas matplotlib seaborn scikit-learn
```

3. Baixe o dataset em [kaggle.com/c/titanic](https://www.kaggle.com/c/titanic/data) e coloque o arquivo `train.csv` na pasta do projeto

4. Execute o notebook ou script principal

---

## Dataset

[Titanic: Machine Learning from Disaster - Kaggle](https://www.kaggle.com/c/titanic)