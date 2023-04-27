# Load the MNIST dataset using fetch_openml(mnist_784) and split it into:
#   - training set (50000)
#   - validation set (10000)
#   - test set (10000)
#
# Train separate classifiers, e.g. knn classifier, SVM, Random Forest and check the scores on the validation set.
#
# Next, use a Voting classifier to combine them and check the scores for hard voting and soft voting on the
# validation set. Which gives the best results in this case?
#
# Train the best one (or best combination) on the test set and check the score.

from typing import Tuple, Union

from sklearn import clone
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.utils import Bunch


def print_splitter():
    print("\n########################################\n")


b: Bunch = fetch_openml('mnist_784', parser="auto")
df = b.get("data")

y = b.get('target')
X_train, X_test, y_train, y_test = train_test_split(df, y, train_size=50000, random_state=42)

X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, train_size=10000, random_state=42)

print(
    "X_train.shape:", X_train.shape,  # X_train.shape: (50000, 784)
    "\nX_test.shape:", X_test.shape,  # X_test.shape: (10000, 784)
    "\nX_val.shape:", X_val.shape,  # X_val.shape: (10000, 784)
)

clfs: list[Tuple[str, Union[RandomForestClassifier, KNeighborsClassifier, SVC]]] = [
    ("Random Forest", RandomForestClassifier(n_estimators=100, random_state=42)),
    ("KNN", KNeighborsClassifier(n_neighbors=5)),
    ("SVM", SVC(random_state=42)),
]

print_splitter()

for name, model in clfs:
    print("Training model:", name)
    model.fit(X_train, y_train)

print_splitter()

for name, model in clfs:
    print("model:", name)
    print("\tscore:", model.score(X_val, y_val))

# model: Random Forest
#   score: 0.9677
# model: KNN
# 	score: 0.9691
# model: SVM
# 	score: 0.9764

print_splitter()

voting_hard_clf = VotingClassifier(estimators=[(clf[0], clone(clf[1])) for clf in clfs], voting="hard")
print("Training model: voting classifier hard")
voting_hard_clf.fit(X_train, y_train)

voting_soft_clf = VotingClassifier(estimators=[(clf[0], clone(clf[1])) for clf in clfs], voting="hard")
print("Training model: voting classifier soft")
voting_soft_clf.fit(X_train, y_train)

print_splitter()

print("model: voting classifier hard")
voting_hard_clf_pred = voting_hard_clf.predict(X_val)
print("\tscore:", accuracy_score(voting_hard_clf_pred, y_val))

print("model: voting classifier soft")
voting_soft_clf_pred = voting_soft_clf.predict(X_val)
print("\tscore:", accuracy_score(voting_soft_clf_pred, y_val))

# model: voting classifier hard
#   score: 0.977
# model: voting classifier soft
#   score: 0.977

print_splitter()

print("Hard: true => ",
      (voting_hard_clf_pred == y_val).value_counts()[0],
      "\n\ttotal: ",
      len(voting_hard_clf_pred),
      end=None)
print("Soft: true => ",
      (voting_soft_clf_pred == y_val).value_counts()[0],
      "\n\ttotal: ",
      len(voting_soft_clf_pred),
      end=None)

# Hard: true =>  9770
# 	total:  10000
# Soft: true =>  9770
# 	total:  10000

print_splitter()

print(voting_hard_clf.score(X_test, y_test))

# 0.9755
