from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

#4개의 특징 이름을 출력한다.
print(iris.feature_names)

#정수는 꽃의 종류를 나타낸다.
#0 = setosa / 1 = versicolor / 2 = virginica
print(iris.target) 


# 학습데이터를 학습에 사용하는 train set와 검증을 위해 사용하는 test set으로 나눠서
# 쓰자는 의미이다.
from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

#(80:20)으로 분할 한다.
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 4)

#몇개의 행, 열로 되어있는 지 알 수 있다.
print(X_train.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=5)
#fit을 부르면은 학습이 되는 것이다. 
knn.fit(X_train, y_train)
#knn에서는 fit에서는 많은 일을 하지 않음

#KNN에선 predict에서 많은 일을 한다. (거리 측정)
y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test, y_pred)
#여기서의 y_test는 정답 / y_pred는 학습한 데이터 // 이 두가지를 비교해 보는 것이다.

print(scores)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)

#0 = setosa / 1 = versicolor / 2 = virginica
classes = {0:'setosa', 1:'versicolor', 2:'virginica'}
#딕셔너리 -> 숫자로 나오는 것을 문자로 나오게 한것

#아직 보지 못한 새로운 데이터를 제시해보자.
#데이터를 두개를 준 것이다.
x_new = [[3, 4, 5, 2], [5, 4, 2, 2]]

#predict를 이용하여 예측해보라고 한것.
y_predict = knn.predict(x_new)

#첫번째 [0] 데이터와 두번째 데이터를 예측한 결
print(classes[y_predict[0]])
print(classes[y_predict[1]])