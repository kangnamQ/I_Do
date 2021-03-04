print("로봇공학 3주차-1")
print("")

good_for_list = ["pooh", "tigger", "piglet", "rabbit"]
pooh = ["bear", 5, 50]
tigger = ["tiger", 4, 40]
print("list based data management")
print("pooh's species is", pooh[0])
print("pooh's weight is", pooh[2])
print("tigers's age is", tigger[1])

pooh = {"species": "bear", "age": 5, "weight": 50}
tigger = {"species": "tiger", "age": 4, "weight": 40}
print("\ndict based data management")
print("pooh's species is", pooh["species"])
print("pooh's weight is", pooh["weight"])
print("tigers's age is", tigger["age"])

#mydict = {Key1:Value1, Key2:Value2, ...}
#print("read value1 by key1", mydict[Key1])

#1. 읽기 쉬운코드 == 가독성이 좋은 코드
#2. 간결한 코드
#3. 관리가 쉬운 코드
#4. 속도가 빠른 코드

#그래서 가독성이 좋은 Dictionary로 짜는 것이 좋다.

#Key는 숫자나 문자열 (혹은 그 변수)을 써야한다.
#또한 딕셔너리는 key로 들어온 값을 hash() 함수를 통해 hash를 생성하고 이를 기록해 두었다가 특정 키를 찾을 때 활용한다.
#key 값을 직접 비교하지 않고 hash로 변환해서 검색하기 때문에 검색 속도가 빠르다.
#대신 hash() 함수에 들어갈 수 있는 기본 타입만 key로 사용가능하다.
print("\n")
print(hash(1))
print(hash('a'))
print(hash('afsfasd'))
print(hash(1321654))
print(hash(1321.654))
a = [1, 2]
#print(hash(a)) /hash는 리스트를 못받는다.

print("\n")
#딕셔너리의 기본 특징은 순서가 없다는 것이다.
#순서에 의한 인덱스나 슬라이싱도 안된다.
#key값으로만 Value에 접근 가능


pooh = {"species": "bear", "age": 5, "weight": 50}
print(pooh["species"], pooh["age"])
print(pooh)
# 데이터 읽기: 특정 `key`에 연결된 `Value`를 읽기 위해서는 `[Key]`하면 된다.

pooh["weight"] = 100
print(pooh)
# 데이터 수정: 특정 `key`에 연결된 `Value`를 수정할 때는 그냥 값을 키에 넣으면 된다.

pooh["height"] = 80
print(pooh)
# 데이터 추가: 이미 만들어진 딕셔너리에 `Key:Value` 쌍을 추가하는 방법 역시 그냥 값을 키에 넣으면 된다.

del pooh["weight"]
print(pooh)
# 데이터 삭제: 리스트처럼 `del`을 이용한다.

foo = "python is good"
if "good" in foo:
    print("good is in foo")

if "color" in pooh:
    print(pooh["color"])
#in 연산자를 통해 키의 존재유무를 확인 후 쓸 수도 있다.

try:
    print("pooh's color?", pooh["color"])
except KeyError as ke:
    print("[KeyError]", ke)

print("")
print((pooh.keys()))
print(type(pooh.keys()))
print(type(list(pooh.keys())))
print((list(pooh.keys())))
#list로 감싸면 list 타입이 된다.
print((pooh.values()))
print("weight" in pooh.keys())
print("bear" in pooh.values())

keydata = list(pooh.keys())
print(keydata[0])
#list로 감싸야 print가 가능하다.

print("\n")
print("\ndict functions")
scores = {"pooh": 80, "tigger": 70, "piglet": 90, "rabbit": 85}
print("names:", scores.keys())
print("scores:", scores.values())
print("items:", scores.items())

print("names:", list(scores.keys()))
print("scores:", list(scores.values()))
print("items:", list(scores.items()))
#items는 keys와 values 둘다 보여주는 명령어.


print("\n튜플 Tuple")
#튜플(Tuple)을 한 마디로 말하면 수정불가능한 리스트다.

#리스트는 [], 딕셔너리는 {}로 만들었다면 튜플은 ()(parenthesis)로 만든다.
#혹은 ()를 생략해도 된다. ,로 구분해도 하나의 데이터에 들어가면 자동으로 튜플로 인식이 된다.

#튜플은 생성만 할 뿐 원소를 추가, 수정, 삭제할 수 없다.
#생성된 튜플은 값을 읽을 수만 있는데 리스트와 동일하게 인덱싱과 슬라이싱을 통해 읽을 수 있다.


empty_tuple1 = ()
empty_tuple2 = tuple()
#비어있는 리스트, 튜플을 만들때
#꼭 괄호를 써야 비어있는 객체로 인식이 된다. list, tuple만 쓴다면 형식만 인식됨.

#근데 튜플은 수정이 불가해서 비어있는 튜플을 만들어 봤자다..

basic_tuple1 = ("Hello", 1234, 1.234, True)
basic_tuple2 = "Hello", 1234, 1.234, True
depth2_tuple = ("Hello", 1234, (1.234, True))

print(basic_tuple1[1])
print(basic_tuple2[-3])
print(depth2_tuple[-1])
print(depth2_tuple[-1][1])



pooh = "pooh", "bear", 5, 50
name, species, age, weight = pooh
print(name, species, age, weight)
#튜플은 여러 값을 하나에 담았다가 다시 여러 변수에 나눠줄 수 있어서 경우에 따라 유용하게 쓸 수 있다.

tigger = ["tigger", "tiger", 4, 40]
name, species, age, weight = tigger
print(name, species, age, weight)
#근데 리스트도 가능하다...
#나눠주는 데이터의 갯수가 같아야한다.

#튜플을 쓰는건 값을 변경할 수 없어서 좀더 안전할 수 있다.
