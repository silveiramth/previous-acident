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
- XGBoost
- MLflow

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

### 4. Modelagem e comparação de algoritmos
Foram testadas duas abordagens diferentes para o problema de classificação, com os experimentos registrados e comparados usando **MLflow**:

- **Random Forest** — várias árvores de decisão treinadas em paralelo, com `max_depth=5`
- **XGBoost** — árvores treinadas em sequência, cada uma corrigindo os erros da anterior, com `learning_rate=0.1` e `n_estimators=100`

Divisão treino/teste: 80% / 20% com `random_state=42`

---

## Resultados

| Modelo | Acurácia |
|---|---|
| Random Forest | 82.1% |
| **XGBoost** | **83.1%** |

O XGBoost apresentou a melhor performance entre os dois modelos testados, ainda que a diferença tenha sido pequena — o que indica que, para esse volume de dados, ambas as abordagens são competitivas.

---

## Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/silveiramth/previous-acident
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install pandas matplotlib seaborn scikit-learn xgboost mlflow
```

4. Baixe o dataset em [kaggle.com/c/titanic](https://www.kaggle.com/c/titanic/data) e coloque o arquivo `train.csv` na pasta do projeto

5. Execute o script principal

6. Para visualizar os experimentos registrados no MLflow:
```bash
python -m mlflow ui
```
Acesse `http://127.0.0.1:5000` no navegador

---

## Dataset

[Titanic: Machine Learning from Disaster - Kaggle](https://www.kaggle.com/c/titanic)