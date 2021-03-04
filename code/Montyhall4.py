from random import randint


def monty_hall():
    car = randint(0, 2)
    first_choice = randint(0, 2)
    opened_door = car
    while opened_door == car or opened_door == first_choice:
        opened_door = randint(0, 2)
    second_choice = first_choice
    while second_choice == first_choice or second_choice == opened_door:
        second_choice = randint(0, 2)
    return car == first_choice, car == second_choice

hits_of_first = hits_of_second = 0
total = 10000
for _ in range(total):
    hit_of_first, hit_of_second = monty_hall()
    if hit_of_first:
        hits_of_first += 1
    elif hit_of_second:
        hits_of_second += 1

print(f"first: {hits_of_first}/{total} = {hits_of_first / total}")
print(f"second: {hits_of_second}/{total} = {hits_of_second / total}")

#출처: https: // comdoc.tistory.com / entry / Monty - Hall - problem[ComDoc]
