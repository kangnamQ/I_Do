import numpy as np
import matplotlib.pyplot as plt

X0 = np.arange(-25, 25)
y0 = 0.33 * (X0**3) + 50 * (X0**2) - 100 * X0 -30
plt.plot(X0, y0, color='black')

x = 20
learning_rate = 0.01    #학습률
precision = 0.00001     #정밀도
max_iterations = 20    #반복 횟수

# Loss function
loss_func = lambda x: 0.33 * (x**3) + 50 * (x**2) - 100 * x -30

# Gradient (differentiate)
gradient = lambda x: 0.99 * (x**2) + 100 * x - 100

X = [x]
Y = [loss_func(x)]
# 그래디언트 강하법
for i in range(max_iterations):
    print("반복 횟수 : ", i+1)
    print("x값 : ", x)
    print("기울기 값: ", gradient(x))
    print("학습율을 곱한 기울기 : ", learning_rate * gradient(x))
    
    x = x - learning_rate * gradient(x)
    
    print("계산 이후 x : ", x)
    print("손실 함수값(", x, ")=", loss_func(x),"\n")
    X.append(x)
    Y.append(loss_func(x))
    
print(X, "\n")
print(Y, "\n")
plt.scatter(X,Y)

print("최소값 = ", x)
plt.scatter(x,loss_func(x), color='red')


plt.xlabel('X Data')
plt.ylabel('Loss function')
plt.show()