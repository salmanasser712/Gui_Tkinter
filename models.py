import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from Gussian import Guss
from sklearn.cluster import KMeans

class Model:

    def knn(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        knn = KNeighborsClassifier(n_neighbors=10)
        knn.fit(X_train, y_train)
        return knn.score(X_test, y_test)

    def Linear(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        lm = LinearRegression()
        lm.fit(X_train, y_train)
        return lm.score(X_test, y_test)

    def Logistic(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        logmodel = LogisticRegression(max_iter= 1000)
        logmodel.fit(X_train, y_train)
        return logmodel.score(X_test, y_test)

    def randforst(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        rfc = RandomForestClassifier(n_estimators=200)
        rfc.fit(X_train, y_train)
        return rfc.score(X_test, y_test)

    def decision(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        dtree = DecisionTreeClassifier(criterion = "entropy", max_depth = 8, min_samples_leaf = 17)
        dtree.fit(X_train, y_train)
        return dtree.score(X_test, y_test)

    def naive(self, data):
        X = data.drop('y', axis=1)
        y = data['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
        X_train['y'] = y_train
        obj = Guss()
        pre = obj.get_per_gus(X_test, X_train)
        return accuracy_score(y_test, pre)

    def K_means(self, data):
        X = data.drop(['y'], axis=1)
        y = data['y']
        kmeans = KMeans(n_clusters=4, random_state=0)
        kmeans.fit(X)
        labels = kmeans.labels_
        return sum(y == labels)/float(y.size)






