from tensorflow.keras import models, layers
import numpy as np
from sklearn.datasets import load_iris
    
iris = load_iris()

#MLP로 다시 시도이므로 조건을 그대로 주겠습니다.
X = iris.data[:, (0, 1)]        #꽃의 너비와 높이만을 입력으로 함

y = (iris.target ==0).astype(np.int)    #출력은 "Iris Setosa인가 아닌가" 이다.
print("y 값 : \n", y)

model = models.Sequential()
#model.add(layers.Dense(units = 6,activation='sigmoid',input_shape=(2,)))
model.add(layers.Dense(units = 4,activation='sigmoid',input_shape=(2,)))
model.add(layers.Dense(1 ,activation='sigmoid'))

model.compile(optimizer='sgd',
             loss='mse',
             metrics = ['acc'])

model.fit(X,y,epochs = 10, batch_size=1)

# test
ytest = model.predict(X)
print("훈련한 y값 : \n", ytest) #보기 편하게 하기위해 .T로 전치했음.

error = ytest - y             #ytest 값과 y를 뺄 수 있도록 행렬을 맞춰줌.
print("test 값 - y 값(정답) \n", error)


