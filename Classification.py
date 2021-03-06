import pandas as pd
from sklearn import svm
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, train_test_split

Data_Source = pd.read_csv('tempData/TempSamples2/MyFile/NumberEndFile.csv')
feature_cols = ['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8',
                'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT7', 'SRCPORT8',
                'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
                'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8']
X = Data_Source[feature_cols].values
y = Data_Source['Result'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
clf = svm.SVC()
clf.fit(X_train, y_train)
accuracy_scores = cross_val_score(clf, X_test, y_test, cv=10, scoring='accuracy')
print("accuracy: {}".format(accuracy_scores))
#Classification Report
predicted = clf.predict(X_test)
report = classification_report(y_test, predicted)
print("Classification Report:")
print(report)

# Baseline
Baseclf = DummyClassifier(strategy='uniform', random_state=0)
Baseclf.fit(X_train, y_train)
print("Baseline scores: {}".format(Baseclf.score(X_test, y_test)))

# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
# predicted = linreg.predict(X_test)
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(linreg, X, y, cv=10, scoring='accuracy')
# k_range = list(range(1, 31))
# param_grid = dict(n_neighbors=k_range)
# grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy')
# grid.fit(X, y)
# print(grid.best_score_)
# print(grid.best_params_)
# print(grid.best_estimator_)
# print(scores)
