from random import randrange

many_door = 3

goats = 0
car = 1
doors = [goats for n in range(many_door)]
where_car = randrange(0, int(many_door))
print(where_car)

doors[where_car] = car
print("확인", doors)


choice = 0

doors[2] = 'goat'
print(doors)

while where_car == 2:
    where_car = randrange(0, int(many_door))
    print(where_car)

re_choice = str(input("선택을 바꾸시겠습니까? (Y / N) : "))
print(re_choice)
while re_choice == 'Y' or 'N':
    re_choice = input("다시 선택하여 주세요. (Y / N) : ")
    if re_choice == 'Y' or "N":
        break
print(re_choice)
