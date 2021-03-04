print("로봇공학 4주차-1")
print("")

# import 키워드를 통해 외부 파이썬 파일의 함수, 변수, 클래스를 가져다 쓸 수 있다.
# 각각의 .py 파일을 모듈(Module)이라 하고 여러 모듈을 묶은 폴더를 패키지(Package)라고 한다.

#list_ops.py를 만들어서 실행
# list_ops.py
def add(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f + b)
    return out
#foo와 bar의 리스트를 합친 데이터를 만들어 내는것

def subtract(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f - b)
    return out

def multiply(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f * b)
    return out

def divide(foo, bar):
    out = []
    for f, b in zip(foo, bar):
        out.append(f / b)
    return out

spam = [51, 23]
ham = [34, 67]

#if __name__ == '__main__':
#    eggs = add(spam, ham)
#    print(eggs)


print("\n 여기서 부터는 모듈 사용 use_list_ops.py")
foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]

from package import list_ops, list_ops as lo

#파일명 자체가 모듈명이 된다.

goo = list_ops.add(foo, bar)
print(("{} + {} = {}".format(foo, bar, goo)))
print(f"{foo} + {bar} = {goo}")
#zip이였어서 자연스럽게 짧은 쪽에 맞춰서 만들어진다.

goo = list_ops.multiply(list_ops.spam, list_ops.ham)
print(("{} + {} = {}".format(list_ops.spam, list_ops.ham, goo)))
print(f"{list_ops.spam} * {list_ops.ham} = {goo}")
print("list_ops.spam: {list_ops.spam}")
# => list_ops.spam: [51, 23]
#변수 spam, ham을 가져왔는데 이것은
#list_ops.py라는 스크립트가 실행되었다는 것을 뜻한다.
#list_ops를 import 만 했지만 내부적으로는 list_ops.py가 실행된 것이다.

#list_ops.py에 실행 가능한 코드를 넣되 외부에서 import 할 때는 실행되지 않게 하고 싶다면
# __name__ 밑에 적어주면 된다.
# list_ops.py에서는 eggs라는 변수가 if __name__ == '__main__': 조건문 아래 있기 때문에
# 외부에서 import 할 때는 선언되지 않는다.
try:
    print("list_ops.eggs: {}".format(list_ops.eggs))
except Exception as e:
    print(e)



print("\n")
#import A as B 라고 하면 A 모듈을 B라는 이름으로 가져오겠다는 뜻이다.

goo = lo.subtract(foo, bar)
print("{} - {} = {}".format(foo, bar, goo))
goo = lo.divide(bar, foo)
print("{} / {} = {}".format(bar, foo, goo))


print("\n")
#아예 외부 모듈명을 쓰지 않고 바로 함수나 변수를 사용하고 싶을 때는 from module import object를 쓰면 된다.
#from을 써서 가져온 객체는 모듈명을 생략하고 사용가능하다.

from package.list_ops import add, subtract, spam

goo = add(foo, bar)
print(f"{foo} + {bar} = {goo}")
goo = subtract(bar, foo)
print(f"{bar} - {foo} = {goo}")
print(f"spam = {spam}")


print("\n")
# dict_ops.py
def add(foo, bar):
    out = {}
    #dict로 사용하는 코드
    for key in foo.keys():
    #foo와 bar의 key가 다를 수 있어서 for과 if사용
        if key in bar:
            out[key] = foo[key] + bar[key]
    return out

def subtract(foo, bar):
    out = {}
    for key in foo.keys():
        if key in bar:
            out[key] = foo[key] - bar[key]
    return out

def multiply(foo, bar):
    out = {}
    for key in foo.keys():
        if key in bar:
            out[key] = foo[key] * bar[key]
    return out

def divide(foo, bar):
    out = {}
    for key in foo.keys():
        if key in bar:
            out[key] = foo[key] / bar[key]
    return out


print("\n")
import package.list_ops as lo
import package.dict_ops as do

weights = [65, 90, 42, 76]
heights = [1.65, 1.78, 1.59, 1.80]
heights_sq = lo.multiply(heights, heights)
print((heights_sq))

bmi = lo.divide(weights, heights_sq)
print("BMI:", bmi)

print("\n")
w_names = ["RM", "Suga", "Jin", "V"]
h_names = ["Jimin", "RM", "Suga", "Jin"]
weights = dict(zip(w_names, weights))
print("weights", weights)
#딕셔너리 만드는 방법
heights = dict(zip(h_names, heights))
print("heights", heights)

heights_sq = do.multiply(heights, heights)
print("heights_sq", heights_sq)
bmi = do.divide(weights, heights_sq)
print("BMI:", bmi)


newdata = {}
try:
    assert 'country' in newdata, 'country is not in newdata'
except AssertionError as ae:
    print(ae)