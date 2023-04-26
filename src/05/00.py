# Try to do Kaggle’s Titanic dataset challenge:
# https://www.kaggle.com/competitions/titanic/
#
# It is your job to predict if a passenger survived the sinking of the Titanic or not. For each entry
# in the test set, you must predict a 0 or 1 value (survived or not).
#
# The dataset (train.csv and test.csv) are available on Canvas, so you don’t require a login.
#
# You DO NOT have to submit a csv file to Kaggle, just try to use cross-validation to have an
# idea of how good your model is.
#
# The attributes have the following meaning:
#   - PassengerId: a unique identifier for each passenger
#   - Survived: that's the target, 0 means the passenger did not survive, while 1 means he/she survived.
#   - Pclass: passenger class.
#   - Name, Sex, Age: self-explanatory
#   - SibSp: how many siblings & spouses of the passenger aboard the Titanic.
#   - Parch: how many children & parents of the passenger aboard the Titanic.
#   - Ticket: ticket id
#   - Fare: price paid (in pounds)
#   - Cabin: passengers cabin number
#   - Embarked: where the passenger embarked the Titanic (C=Cherbourg, Q=Queenstown, S=Southampton)
#
# You have to use 2 data preprocessing pipelines and use them combined in a ColumnTransformer. The pipelines are:
# - a numerical pipeline where missing data is replaced by the median, followed by a StandardScaler
# - a categorical pipeline where missing data is replaced by the most frequent value, followed by a One Hot Encoder
#
# Join these pipelines in a ColumnTransformer which you can then apply to the training
# data and test data.
#
# Use a Random Forest Classifier with 100 estimators as a model (use random state 42) and print the cross validation
# score.

# https://johaupt.github.io/blog/columnTransformer_feature_names.html

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
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
    ('estimator', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, y_train = df[columns_categorical + columns_numerical], df["Survived"]

cvs = cross_val_score(transformer, X=X_train, y=y_train, cv=10, scoring="accuracy")
print(cvs, "mean:", cvs.mean())

# [0.74444444 0.79775281 0.74157303 0.80898876 0.88764045 0.83146067
#  0.83146067 0.7752809  0.84269663 0.84269663] mean: 0.8103995006242197
