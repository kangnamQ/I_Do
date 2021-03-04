print("로봇공학 1주차-2")
print("")

for a in range(10):
    print(a)
if a == 1:
    print(1)

mylist = ['abc', 'bc', 'cde']
if 'abc' in mylist:
    print("abc is in mylist")

for v in mylist:
    if v.startswith('a') and len(v) > 1:
        print(v)

mylist2 = 1



print("")
a1 = "hello"
print(a1, type(a1), "value:")

a2 = 3.14
print(a2, type(a2), "value:")

a3 = True
print(a3, type(a3), "value:")

a4 = False
print(a4, type(a4), "value:")



print("")
import sys
b = 135.68
c = 15
print("float", type(b), sys.getsizeof(b))
print("integer", type(c), sys.getsizeof(c))

print(b+c)
print(b-c)
print(b*c)
print(b/c)

print("")
d = 10.5
e = 3
print(d ** 3)
print(d ** e)
print(d % e)
print(d // e)


print("")
ex = 13 ** 3
print(ex)
ex1 = ex % 16
print(ex1)
ex2_1 = ex // 16
print(ex2_1)
ex2 = ex2_1 % 16
print(ex2_1, ex2)
ex3_1 = ex2_1 // 16
ex3 = ex3_1 % 16
print(ex3_1, ex3)

print(8 * (16**2) + 9 * 16 + 5)


print("")
exA=hex(ex)
print(exA)
#0x895이므로 16진수 표현하는 0x를 제거하면 895가 나옴.

print("")
ex8=oct(ex)  #10진수를 8진수로
print(ex8)
# 0o = 8진수를 표현할 때 앞에 붙음
ex16=hex(ex)  #10진수를 16진수로
print(ex16)
# 0x = 16진수를 표현할 때 앞에 붙음
ex02=bin(ex)  #10진수를 2진수로
print(ex02)
# 0b = 2진수를 표현할 때 앞에 붙음



print(""), print("")
print("if statements")
if 13 ** 3 > 50 **2:
    print("13**2 > 50**2")
elif 13 ** 3 != 2197:
    print("13**3 != 2197")
elif 13 ** 3 >= 30 **2:
    print("13**3 >= 30**2") #위에꺼는 False 여기서 True가 걸려 이것이 출력
else:
    print("13**3 < 30**2")



print(""), print("")
print("\nWhat is difference between `is` and `==`?")
print("little difference for built-in types(int, float, str)")
intvar = 12
print("intvar == 12:", intvar == 12)
print("intvar is 12:", intvar is 12)
boolvar = True
print("boolvar == True:", boolvar == True)
print("boolvar is True:", boolvar is True)
#int, float, str 에서는 비슷하게 작용한다.
#하지만 오브젝트에서, 객체에서 달라진다.
print("big difference for object types")
foo = [1, 2]
bar = [1, 2]
print("foo == bar:", foo == bar) #안에있는 값을 비교
print("foo is bar:", foo is bar) #메모리를 비교? <같은 값이지만 서로 다른 메모리에 저장되있어서 False가 뜸
goo = bar # 같은 주소를 가지는 포인터만 된다. 값을 복사하는 것이 아닌 주소를 같이 사용하는 것, 객체타입이라서 그엄
print("foo == goo", foo == goo)
goo[0] = 0
print("bar, goo:", bar, goo)
print("foo == goo", foo == goo)
print("bar is goo", bar is goo)
print("goo is bar", goo is bar)


print(""), print("")
value = 10
if (value % 2 == 0) and (value < 12):  #여기서 ()를 안하게 된다면 and, or 먼저 먹게 될 수 있으니 ()를 쳐주는 것이 좋음
    print("value is even and less than 12")
if (value % 2 != 0) or (value < 0):
    print("value is odd or negative")
if (value % 2 != 0) or (value > 0):
    print("or test")
#and는 둘다맞아야 성립되고 or은 하나만 맞아도 성립된다.
print(value % 2 == 0) # 여기서의 %는 나누기 후 나누기를 의미, ==는 비교를 의미하니 True, False로 나옴.

print(""), print("")