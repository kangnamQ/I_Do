import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
    
iris = load_iris()

#MLP로 다시 시도이므로 조건을 그대로 주겠습니다.
X = iris.data[:, (0, 1)]        #꽃의 너비와 높이만을 입력으로 함

y = (iris.target ==0).astype(np.int)    #출력은 "Iris Setosa인가 아닌가" 이다.
print("y 값 : \n", y)

percep = Perceptron(random_state=32)
percep.fit(X, y)

ytest = percep.predict(X)
print("훈련한 y값 : \n", ytest)

error = ytest - y
print("test 값 - y 값(정답) \n", error)

