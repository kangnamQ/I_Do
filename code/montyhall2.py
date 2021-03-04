import random

door = ['a', 'b', 'c']
no_change = 0
change = 0

trial = 100

for _ in range(trial):
    car = random.randint(0, 2)
    player_choice = random.randint(0, 2)

    empty_door = []
    # 사회자가 선택하기 위한 경우의 수를 추리기 위해
    for i in range(3):
        if i != player_choice and i != car:
            empty_door.append(door[i])

    com = random.sample(empty_door, 1)[0]

    # 선택을 바꾸지 않은 경우
    if player_choice == car:
        no_change += 1

    # 사회자가 선택한 문을 리스트에서 제거한다.
    empty_door.remove(com)

    # 선택을 바꾼 경우
    if not empty_door:
        change += 1

print("선택을 바꾸지 않은 경우:", (no_change / trial) * 100 , "%")
print("선택을 바꾼 경우:", (change / trial) * 100 , "%")


# https://enjoyso.tistory.com/87