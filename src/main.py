import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('archives/train.csv')

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())
df['Sex'] = df['Sex'].map({
    "male": 0,
    "female": 1
})
df['Embarked'] = df['Embarked'].fillna("S")

df['Embarked'] = df['Embarked'].map({
    "S": 0,
    "C": 1,
    "Q": 2
})

df['FamilySize'] = df['SibSp'] + df['Parch']
df['isAlone'] = (df['FamilySize'] == 0)

x = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'FamilySize', 'isAlone']]
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # dedicando parte para teste e aprendizado

model = RandomForestClassifier(n_estimators=200) # rodou sem erros
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)