# Expand the previous exercise by implementing a GridSearch on e.g. 2 parameters. Can you
# obtain a better cross validation score?

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

columns_numerical = ['Age', 'SibSp', 'Parch', 'Fare']
columns_categorical = ['Pclass', 'Sex', 'Embarked']

df = pd.read_csv("../../resources/titanic/train.csv")

transformer = Pipeline([
    ('preprocessor', ColumnTransformer([
        ("num", Pipeline([
            ('imputer', SimpleImputer(strategy="median")),
            ('scaler', StandardScaler()),  # (x - μ)
        ]), columns_numerical),
        ("class", Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder()),  # OneHotEncoder -> ['a', 'b', 'a'] -> [(1, 0), (0, 1), (1, 0)]
        ]), columns_categorical),
    ])),
    ('estimator', RandomForestClassifier(random_state=42))
])

X_train, y_train = df[columns_categorical + columns_numerical], df["Survived"]

# n_estimators, max_features
gs = GridSearchCV(
    transformer,
    {
        'estimator__n_estimators': np.array(range(50, 250, 50)),
        'estimator__max_features': np.linspace(1, len(X_train.columns), len(X_train.columns), dtype=int)
    },
    cv=10, verbose=10)

gs.fit(X_train, y_train)

print("score:", gs.best_score_)
print('best params:', gs.best_params_)

# score: 0.821585518102372
# best params: {'estimator__max_features': 6, 'estimator__n_estimators': 150}
