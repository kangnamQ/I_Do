print("로봇공학 2주차-1")
print("")

string1 = "Life is too short"
string2 = 'You need python'
print(type(string1), type(string1))
#"",'' < 상관없이 str형

print("Life 'is' too short")
print('You "need" python')
#""와 ''를 구분해서 양쪽에 것과 다른 것을 사용

print("Life \"is\" too short,\nYou \'need\' python")
print("특수문자 \"로 \"자체가 문자로 인식됨   스페이스 또한 인식")

print("안녕? 파이썬")

print("")
print("\n 한줄 넘기기")
print("\t 탭을 쓸 때 사용")
print("\\ \을 쓸 때 사용")
print("\' '을 쓸 때 사용")
print('\" "을 쓸 때 사용')


print(""),print("")
print("can you feel me 나를 느껴 봐요 \ncan you touch me 나를 붙잡아 줘")
print("can you hold me 나를 꼭 안아 줘 \nI want you pick me up")
print(("pick me "*3 + "up ") * 2)  #\n을 넣을 경우 한칸 더 뛰어져서 보기힘듬...
print("pick me "*4)
print(("pick me "*3 + "up ") * 3)
print("pick me "*4 + "I want you pick me up")


text = "Life is too short, You need Python"
# Life is too short, You need Python
# 0         1         2         3
# 0123456789012345678901234567890123

print("print t:",text[8], text[16], text[-4])
print(text[:4])
print(text[12:17])
print(text[-6:])
print(text[23:27])
print(text[23:-7]) #앞에서 샌것도 뒤에서 새는 것도 혼용해서 사용가능
#시작이 생략되어 있으면 처음부터, 끝이 생략되있으면 끝까지 가져오는 것이다.

print("")
print(text[-6:] + text[4:-6] + text[:4])
print(text[-6:] + text[4:28] + text[:4])



print("")
_class = "warrior"
print("\n" + "="*30, "\nString formatting 1: %")

print("포맷 코드를 이용")
print("class: %s, HP: %d, DPS: %f" % (_class, 100, 1456.23))
#포맷 코드 : 문자열은 %s, 정수형은 %d, 실수형은 %f를 사용
#보통 C에서 많이 사용

print("format 함수를 이용")
print("class: {}, HP: {}, DPS: {}".format(_class, 100, 1456.23))
# 타입에 상관없이 {}와 {}안에 넣을 값을 쓰면 자동으로 입력
# 이방법도 요즘은 많이 사용하지 않음 - 순서를 맞춰줘야함

print("f문자열 포매팅")
print(f"class: {_class}, HP: {100}, DPS: {1459.23}")
#앞에 f를 쳐줘야 한다. = 그래서 f문자열 포매팅
#직관적으로 좋음. 그냥 {}안에 직접 넣으면 자동으로 타입이 변환됨



print("")
print("pick me pick me pick me up".count('pick me'))
text = "pick me pick me pick me up"
print(text.count("pick me"))



print("")
text = "For the python, of the python, by the python"
pyind = text.find("py")
print("where is 'py?", pyind) #처음 py
pyind = text.find("py", pyind + 1)
print("where is 'py?", pyind) #처음 py 다음자리 부터의 py, 즉 2번째 py
pyind = text.find("py", pyind + 1)
print("where is 'py?", pyind) #3번째 py
pyind = text.find("py", pyind + 1)
print("where is 'py?", pyind) #4번째 py, find는 없으면 -1을 반환하기 때문에 -1

print("\nfind f포매팅")
text = "For the python, of the python, by the python"
pyind = text.find("py")
print(f"'py' found at {pyind} in `{text}`")
pyind = text.find("py", pyind+1)
print(f"'py' found at {pyind} in `{text}`")
#f문자열 포매팅을 사용하면 좀더 직관적이다.

print("\nindex f포매팅")
text = "For the python, of the python, by the python"
pyind = text.index("py")
print(f"'py' indexed at {pyind} in `{text}`")
pyind = text.index("py", pyind +1)
print(f"'py' indexed at {pyind} in `{text}`")
pyind = text.index("py", pyind +1)
print(f"'py' indexed at {pyind} in `{text}`")

#여기서 부터 error뜸
#try : 에러가 뜰 것 같은 구간이 있을 때 시도를 해보고 되면 나오고
#에러가 나면 except로 넘어가 그대로 쭉 실행하게 하는 것
try:
    pyind = text.index("py", pyind + 1)
    print(f"'py' indexed at {pyind} in `{text}`")
except  ValueError as ve:
    print(ve)
#index에서는 ValueError가 나온다.
#ValueError이외의 다른 에러가 나는 경우 try에서 죽어도 괜찮다는 말.
#substring not found라는 문구가 뜨며 에러가 났는데 그냥 프린트만 하는 방법임.

pyind = text.index("py")
print(f"'py' indexed at {pyind} in `{text}`")



print("")
mixed = "PYthon"
small = "python"

print(mixed == small)
print(mixed.lower() == small)
print(mixed.lower() == small.lower())
print(mixed.upper() == small.upper())
print(mixed.upper())
print(mixed.lower())
print(mixed.lower() is small.lower())
#객체가 다르기 때문에, 다른 객체이기 때문에 False가 뜬다, 쓸 때 조심



print("")
wise_saying = ' "Walking on water and developing software ' \
              'from a specification are easy if both are frozen..." '
print(wise_saying)
print(wise_saying.strip())
#strip() = 공백, 불필요한 시작/끝의 문자을열을 지우는 것
print(wise_saying.strip("\""))
#양쪽의 공백이 있기 때문에 ""가 지워지지 않음

wise_saying1 = wise_saying.strip()
print(wise_saying1.strip("\""))

print("")
print(wise_saying)
wise_saying1 = wise_saying.strip()
print(wise_saying1)
wise_saying2 = wise_saying1.strip("\"")
print(wise_saying2)
wise_saying3 = wise_saying2.strip(".")
print(wise_saying3)
wise_saying4 = wise_saying2.rstrip(".")
print(wise_saying4)
#그냥 .해도 지워지긴 하지만 앞에껀 납두고 뒤에껏만 지우고 싶을 때 같은 곳에 사용 가능할 듯.
#앞쪽만 지우기 : lstrip
#뒤쪽만 지우기 : rstrip



print("")
Lincoln_said = "for the people, by the people, of the people"
print(Lincoln_said)
We_say = Lincoln_said.replace("people", "python")
print("We_say:", We_say)
#특정 문자열을 지우는 것은 안되지만 replace를 사용하여 교체가능
Simply_say = We_say.replace("the ", "")
print("Simply_say:", Simply_say)

print(We_say.split(" "))
print(We_say.split(","))
#기준이 되는 것들은 들어가지 않음, 구분해주기 위해서.



print("")
marble1 = \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "그간 많은 stress 견뎌내며 비로소 대리암이 되었다네\n" \
    "모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나를 보고 웃기라도 하는 날엔 하루 종일 아무것도 할 수 없네\n" \
    "그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "이것이 염산반응이다\n" \
    "이것이 염산반응이다\n" \
    "Hcl이다 CaCO3다\n" \
    "2Hcl + CaCO3 -> CaCl2 +CO2 + H2O다.\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" \
    "나는 대리암 나는 대리암"

#\ 한줄의 코드를 줄을 나눠주기 위해 사용한 것
print("\n1)“대리암”의 가사를 문자열 연산을 통해 만들어 보세오.")
marble2 = \
    "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" * 2 \
    + "그간 많은 stress 견뎌내며 비로소 대리암이 되었다네\n" \
    + "모든 게 완벽했던 그 어느 날 난 너를 만나게 된 거야\n" \
    + "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" * 2 \
    + "나를 보고 웃기라도 하는 날엔 하루 종일 아무것도 할 수 없네\n" \
    + "그 눈으로 날 똑바로 바라보면 나는 녹아버릴 거야\n" \
    + "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" * 4 \
    + "이것이 염산반응이다\n" * 2 \
    + "Hcl이다 CaCO3다\n" \
    + "2Hcl + CaCO3 -> CaCl2 +CO2 + H2O다.\n" \
    + "나는 대리암 염산과 반응하면 이산화탄소를 내며 녹는 대리암\n" * 2 \
    + "나는 대리암 나는 대리암" \

print(marble2)

print("\n2)가사에서 “대리암”이 몇 번 나오는지, 세 번째로 나오는 위치는 어디인지 찾아보세요.")
print("대리암",marble1.count("대리암"))

Q2_1 = marble1.find("대리암")
print(Q2_1)
Q2_2 = marble1.find("대리암", Q2_1+1)
print(Q2_2)
Q2_3 = marble1.find("대리암", Q2_2+1)
print("3번 째 대리암의 위치 : ", Q2_3)

print("\n3)가사에서 “대리암”을 “현무암”으로 바꿔보세오.")
print(marble1.replace("대리암", "현무암"))
