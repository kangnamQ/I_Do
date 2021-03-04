import numpy as np
import matplotlib.pyplot as plt

# 이해하기 쉽게 오차함수를 그려본다. 문제의 그림에서 1사분면에 있기 때문에
# 범위는 0부터 6이상 (10을 선택)을 선택하였습니다.
X0 = np.arange(0, 10)
y0 = (X0 ** 2) - 6 * X0 + 4
plt.plot(X0, y0, color='black')

# Loss function 오차함수를 람다함수로 정의해주고
loss_func = lambda x: (x ** 2) - 6 * x + 4
# Gradient (differentiate) 오차함수의 미분함수도(=기울기) 람다함수로 정의해주었습니다.
gradient = lambda x: 2 * x - 6

# 경사하강법
# 현재위치는 x = 6이고 학습률을 0.3
x = 6
learning_rate = 0.3  # 학습률

# 먼저 오차함수와 오차함수를 미분(기울기)함수도 모두 정의해 두었기 때문에 대입해줍니다.
# x가 6일때의 기울기 값입니다.
g1 = gradient(x)
print("x가 ", x, "일 때의 기울기 : ", g1)
# => x가  6 일 때의 기울기 :  6

# 현재의 x에서 x가 6일때 나온 기울기값에 학습률을 곱해준뒤 x에서 빼줍니다.
g1 = g1 * learning_rate
print("기울기 * 학습률 값 : ", g1)
# => 기울기 * 학습률 값 :  1.7999999999999998
x = x - g1
print("x값에서 계산한 기울기를 뺀 x값 : ", x, "\n")
# => x값에서 계산한 기울기를 뺀 x값 :  4.2

# 계산된 x값을 이용하여 계산을 반복해줍니다.
g2 = gradient(x)
print("x가 ", x, "일 때의 기울기 : ", g2)
# => x가  4.2 일 때의 기울기 :  2.4000000000000004

g2 = g2 * learning_rate
print("기울기 * 학습률 값 : ", g2)
# => 기울기 * 학습률 값 :  0.7200000000000001

x = x - g2
print("x값에서 계산한 기울기를 뺀 x값 : ", x, "\n")
# => x값에서 계산한 기울기를 뺀 x값 :  3.48


# 위와 같은 동일한 작업을 gradient값(기울기값)이 0이 나올 때까지 반복하여 줍니다.
x = 6  # 초기값 = 6
learning_rate = 0.3  # 학습률
plt.scatter(x, loss_func(x))

max_iterations = 50  # 반복 횟수
# 리스트로 만들어서 데이터를 사용하기 쉽게 합니다.
X = [x]
Y = [loss_func(x)]
for i in range(max_iterations):
    print("반복 횟수 : ", i + 1)
    print("x값 : ", x)
    print("기울기 값: ", gradient(x))
    print("학습율을 곱한 기울기 : ", learning_rate * gradient(x))

    x = x - learning_rate * gradient(x)

    print("계산 이후 x : ", x)
    print("손실 함수값(", x, ")=", loss_func(x), "\n")
    X.append(x)
    Y.append(loss_func(x))

print(X, "\n")
print(Y, "\n")
plt.scatter(X, Y)
print("최소값 = ", x)
plt.scatter(x, loss_func(x), color='red')

plt.xlabel('X Data')
plt.ylabel('Loss function')
plt.show()
