print("로봇공학 2주차-2")
print("")

empty_list1 = []
empty_list2 = list()
basic_list = ["Hello", 1234, 1.234, True]
depth2_list = ["Hello", 1234, [1.234, True]]
depth3_list = [["Hello"], [1234, [1.234, True]]]

print(empty_list2)
print(basic_list)
print(depth2_list)
print(depth3_list)

print(basic_list[2])
print(basic_list[-2])
print(depth2_list[2])
print(depth2_list[2][0])
print(depth3_list[1])
print(depth3_list[1][1])
print(depth3_list[1][1][0])

try:
    print(basic_list[5])
except IndexError as ie:
    print("IndexError:", ie)

text = "life is short, you need python"
print(text[:5])
print(basic_list[:3])
print(basic_list[2:])
print(basic_list[2:10])

print("")
#list
print("\nSlicing")
print("[start:end]", basic_list[1:3])
print("[start:]", basic_list[2:])
print("[:end]", basic_list[:2])
print("[start:negative_end]", basic_list[1:-1])
print("[:negative_end]", basic_list[:-2])
print("[negative_start:negative_end]", basic_list[-4:-2])
print("[nested list1]", depth2_list[1:3])
print("[nested list2]", depth3_list[0:2])
print("[partially overlap]", basic_list[2:10])
#3번까지 밖에 없으므로 2,3번까지만 출력, 얘는 에러안뜸.
print("[out of range]", basic_list[5:10])
#범위를 벗어나서 빈리스트 [] 만 출력함, 얘도 에러안뜸


print("")
#인덱싱 -> 그냥 원소
#슬라이싱 -> 리스트의 부분집합이 들어있는 새로운 리스트
print(depth2_list[2][0])
print(depth2_list[2][0:1]) #리스트가 출력이 된다.


print("")
mammal = ["dog", "cat", "human"]
reptile = ["snake", "lizard", "frog"]
bird = ["eagle", "sparrow", "chicken"]

print(mammal)
print(mammal*2)
animal = mammal*2 + reptile + bird
print(animal)


print("")
print("\nlist functions")
tottenham = ['Kane', 'Moura', 'Lloris', 'Sissoko', 'Alli', 'Rose']
print("Tottenham vs Southampton 2019-03-10 starting line up: \n", tottenham)
print("sort() is a in-place function:", tottenham.sort())
tottenham.sort()
print("sort() is a in-place function:", tottenham)
#sort : 원소, 알파벳순, 크기순 정렬

tottenham.remove('Moura')
print("remove moura:", tottenham)
# remove(): 입력한 원소를 삭제

tottenham.insert(1, 'Son')
print("At 72, Moura out Son in:", tottenham)
# insert(): 원하는 위치에 원소 삽입

alli = tottenham.pop(0)
print("pop alli:", alli, tottenham)
# pop(): 입력이 없으면 마지막 원소를 삭제하고 pop(index)는 index의 원소를 삭제한다.

del tottenham[-2]
print(("at 82, Alli and Rose out:", tottenham))
#del : [](여기서는 -2번째)의 원소를 없엠

tottenham.append('Davies')
tottenham.append('Llorente')
print("At 82, Davies and Llorente in:", tottenham)
# append(): 원소를 마지막에 추가한다. 두 리스트의 원소들을 합칠 때는 +나 extend()를 쓴다.

tottenham.reverse()
print("reverse order", tottenham)
# reverse(): 순서를 거꾸로 뒤집는다.

##remove, pop, del 모두 삭제하는 명령어
#remove는 직접 선택, pop, del은 인덱스 지정


print("\n")
import copy

top_lang_2009 = ["Java", "C", "Python", "C++", "C#"]
print(top_lang_2009)
# => top_lang_2019 = ["Java", "C", "Python", "C++", "PHP"]
top_lang_2019 = copy.deepcopy(top_lang_2009)

top_lang_2019.pop(-1)
#top_lang_2009.remove("C#")
#del top_lang_2009[-1]
print(top_lang_2019)

#top_lang_2019 = copy.deepcopy(top_lang_2009)
#top_lang_2019 = top_lang_2009 << 주소만 공유

top_lang_2019.append("PHP")
print(top_lang_2019)



string = "hello"
mylist = ["hi", 123, 1.23, True]
print(len(string))
print(len(mylist))
#len : 문자열(str)의 길이, list, dict, tuple, set 등의 자료구조의 원소 수를 읽을 수 있다.

del mylist[2]
print("\nafter deleting [2]:", mylist)
del mylist[1:]
print("after deleting [1:]:", mylist)
#del: 객체를 삭제하는 키워드로 자료 구조에서 특정 원소를 삭제할 때 쓰인다. 인덱싱, 슬라이싱이 가능하다.

mylist = [1, 2, 3, 4, 5]
mylist[0] = "Life"
print(mylist)

mylist[1:4] = ["is", "too", "short"]
print(mylist)
#원소 변경: 인덱싱이나 슬라이싱으로 잡은 리스트 범위에 = operator로 원소들을 수정할 수 있다.
#참고로 문자열은 =를 이용한 일부 문자 수정이 안된다.

saying = " ".join(mylist[:4])
print(saying)
saying2 = "/".join(mylist[:4])
print(saying2)
#join : 리스트의 내부 문자열 원소들을 하나의 문자열로 연결해준다.
#연결할 때 각 문자열 사이에 " " 사이에 들어있는 문자열을 끼워 넣어준다.


twice = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]

if "채영" in twice:
    print("채영은 트와이스 입니다.")
if "채령" in twice:
    print("채령은 트와이스 입니다.")
if "채령" not in twice:
    print("채령은 트와이스가 아닙니다. 있지않습니다.")
#in: in은 함수가 아니라 operator다. 리스트에 특정 원소가 들어있는지 확인할 때 쓴다.