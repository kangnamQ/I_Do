#20154523 강남규

# Monty Hall problem
# Suppose you’re on a game show, and you’re given the choice of three doors.
# Behind one door is a car, behind the others, goats. You pick a door, say #1,
# and the host, who knows what’s behind the doors, opens another door, say #3, which has a goat.
# He says to you, "Do you want to pick door #2?"
# Is it to your advantage to switch your choice of doors?
# Reference : https://namu.wiki/w/%EB%AA%AC%ED%8B%B0%20%ED%99%80%20%EB%AC%B8%EC%A0%9C

from random import randrange

#문의 갯수 지정
try:
    many_door = int(input("문의 수를 적어주세요.\n문의 수 : "))
except ValueError:
    print("문의 수의 기본값인 3으로 지정되었습니다.")
    many_door = 3

#문 중 하나에 car 배치
goats = 0
car = 1

doors = [goats for n in range(many_door)]
where_car = randrange(0, int(many_door))
doors[where_car] = car

print("확인", doors)

#문 선택
ex_door = list(range(many_door))
print("문의 리스트. 첫번째 문은 0번 문입니다.\n",ex_door)

try:
    choice = int(input("문을 선택하여 주세요. \n선택 : "))
except ValueError:
    print("문의 기본값인 0번 문으로 지정되었습니다.")
    choice = 0
except IndexError:
    print("문의 기본값인 0번 문으로 지정되었습니다.")
    choice = 0

if choice < 0 or choice >= many_door:
    print("기본값인 첫번째 문, 0번 문으로 지정되었습니다.")
    choice = 0
else:
    print("\n선택한 문은", choice,"번 문입니다.")


#문을 선택하고 바꿀 수 있는 기회(사회자가 문여는 것)
if doors[choice] == car:
    no_in = randrange(0, int(many_door))

    while no_in == choice:
        no_in = randrange(0, int(many_door))

    ex_door[no_in] = 'goat'
    print(ex_door)

elif doors[choice] != car:
    no_in = randrange(0, int(many_door))
    while doors[no_in] == car or no_in == choice:
        no_in = randrange(0, int(many_door))

    ex_door[no_in] = 'goat'
    print(ex_door)

re_choice = input("선택을 바꾸시겠습니까? (Y / N) : ")
while re_choice == 'Y' or 'N':
    re_choice = input("다시 선택하여 주세요. (Y / N) : ")



# 위키 백과 링크
# https://ko.wikipedia.org/wiki/%EB%AA%AC%ED%8B%B0_%ED%99%80_%EB%AC%B8%EC%A0%9C
# https://ko.wikipedia.org/wiki/%EC%A1%B0%EA%B1%B4%EB%B6%80_%ED%99%95%EB%A5%A0
# https://ko.wikipedia.org/wiki/%EB%B2%A0%EC%9D%B4%EC%A6%88_%EC%A0%95%EB%A6%AC