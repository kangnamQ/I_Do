print("로봇공학 3주차-2")
print("")


marvel_heroes = ["iron man", "thor", "hulk", "spider man", "black widow", "capt. america", "capt. marvel"]
dc_heroes = ["batman", "superman", "aquaman", "wonder woman", "harley quinn"]
all_heros = marvel_heroes + dc_heroes

myhero = "batman"

if myhero in marvel_heroes:
    print(f"{myhero} is in marvel heroes")
elif myhero in dc_heroes:
    print(f"{myhero} is in dc heroes")
elif myhero not in dc_heroes:
    print(f"{myhero} is NOT in dc heroes")
elif myhero not in marvel_heroes:
    print(f"{myhero} is NOT in marvel heroes")
else:
    print(f"{myhero} is a another heroes")

print("")
for hero in marvel_heroes:
    print(f"my hero is {hero}")
#list 안에 있는 것을 반복

for i in range (10):
    print("i is",i)

print((range(10)))
print(list((range(10))))
#반복

print("marvel len is", len(marvel_heroes))
for i in range (len(marvel_heroes)):
    print(f"the {i}-th hero is",marvel_heroes[i])


print("")
i = 0
print("DC's male heroes ends with 'man'")
while i < len(dc_heroes) and dc_heroes[i].endswith('man'):
    #i가 0~4까지는 만족할 것임, 4이상일 경우 False이므로 while문이 끝남.
    print(f"    {dc_heroes[i]}")
    i += 1

print("\n")
#continue는 반복문에서 continue 이후의 과정을 건너뛰고 다음 loop으로 넘어가는 것
# break는 반복문 자체를 끝낸다.

print("list of marvel heroes")
for hero in marvel_heroes:
    if hero.startswith("spider"):
        print("    Peter Parker by Tobey Maguire was not a kid: "
              "\"With great power comes great responsibility.\"")
        continue
    if hero.startswith("capt"):
        print("    one captain is enough. let me stop here")
        break
    print(f"    {hero} is cool")

#if는 횟수를 예상가능
#while은 횟수를 예상하지 못할 것 같을 때


print("\n실행되는 코드라 #처리")
#name = None
#print("Press 'q' to quit")
#while name != 'q':
#    print("type dc hero's name")
#    name = input()
#    if name is 'q':
#        break
#    if name not in dc_heroes:
#        print(f"{name} is not dc hero\n")
#        continue
#    index = dc_heroes.index(name)
#    print(f"{name}'s index =", index)



print("\n")
#for문을 더 많이 쓴다.

#enumerate는 for문에서 리스트를 반복할 시 원소 뿐만 아니라 인덱스도 받을 수 있는 반복 객체를 만들어 준다.
print("enumerate:", enumerate(marvel_heroes))
print("enumerate:", list(enumerate(marvel_heroes)))

for index, name in enumerate(marvel_heroes):
    print(f"index={index}, name={name}")
#인덱스에는 앞의 값이, name에는 name 값이 들어온다. 튜플 값이기 떄문에.


#zip은 두 개의 리스트를 묶어서 각 리스트의 원소가 하나씩 합쳐진 튜플의 반복 객체를 만들어준다.
print("enumerate:", zip(marvel_heroes, dc_heroes))
print("enumerate:", list(zip(marvel_heroes, dc_heroes)))
#짝을 지을 수 있는 것 까지만 나온다.

for mv_name, dc_name in zip(marvel_heroes, dc_heroes):
    print(f"match: {mv_name} vs {dc_name}")



print("\n")
#딕셔너리는 key와 value가 있기 때문에 둘 중 어떤 것이 필요한지,
# 혹은 둘 다 필요한지에 따라 for문에 들어가는 객체가 달라진다.

#Key만 사용: dict 객체 자체, keys() 함수
#Value만 사용: values() 함수
#둘 다 사용: items() 함수

hero_names = {"iron man": "로다주", "thor": "햄식이"}

for key in hero_names:
    print("hero name:", key)

for key in hero_names.keys():
    print("hero name:", key)

for value in hero_names.values():
    print("한국어 별명:", value)

print("")
for key, value in hero_names.items():
    print(f"{key} is {value}")



print("\n")
super_heroes = []
for hero in marvel_heroes:
    super_heroes.append(hero + "_super")
print("super heroes", super_heroes)


man_heroes = []
for hero in marvel_heroes:
    if hero.endswith("man"):
        man_heroes.append(hero)
print("man heroes:", man_heroes)
#이렇게 하려면 3줄이나 든다.
#그래서 사용하는 것이 List Comprehension이다.

int_square = [i**2 for i in range(10)]
print("int square:", int_square)

print("")
super_heroes = [hero + "_super" for hero in marvel_heroes]
print("super heroes:", super_heroes)

man_heroes = [hero for hero in marvel_heroes if hero.endswith("man")]
print("man heroes:", man_heroes)
#코드가 더 간결해진다.
#list, dictionary, set에도 적용될 수 있다.

abilities = ["suit", "Mjölnir", "physical power", "spider web"]
heroes_with_power = {name: power for name, power in zip(marvel_heroes, abilities)}
print("heroes_with_power:", heroes_with_power)

heroes_man = {name: power for name, power in heroes_with_power.items() if name.endswith("man")}
print("heroes_man:", heroes_man)

heroes_man = {name[:5]: power[:5] for name, power in heroes_with_power.items() if name.endswith("man")}
print("heroes_man:", heroes_man)

