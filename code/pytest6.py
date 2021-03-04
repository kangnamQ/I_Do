print("로봇공학 4주차-1")
print("")


#파이썬은 다중 입력과 다중 출력을 지원하고 입력이나 출력이 없을 수도 있다.
def add(n1, n2):
    return n1+n2
#함수 정의 방법 : def를 쓰고 이름 (인수) 리턴값 (얻고싶은, 사용하고싶은 값)

print(add(1, 2))
print(add(4, 5))

#average_list는 이름 그대로 리스트의 평균을 구하는 함수인데
# 시작 인덱스(start)와 끝 인덱스(end)를 지정할 수 있고
# 중간에 빠져야할 인덱스(skip)를 지정할 수 있다.

def average_list(data, start, end, skip):
    if end is None:
        avg_data = data[start:]
        #end값이 없을때, 끝까지 선택
    else:
        avg_data = data[start:end]
        # 아니라면 지정된 값

    sum = 0
    for ind, num in enumerate(avg_data):
        #ind는 skip떄문에 받는다.
        if ind not in skip:
            sum += num
            #skip이 안들어가 있다면 더해라.

    dlen = len(avg_data) - len(skip)
    #avg 데이터에서 skip을 뺴고 넣은 것.  데이터의 갯수를 알기 위해 사용
    average = sum / dlen
    print(f"average {start}~{end} with skipping {skip} = {average}")
    return average

foo = [1, 2, 3, 4, 5, 6, 7]
print(average_list(foo, 0, 5, [2]))
#0번부터 5번 인덱스 전까지 평균
#2번 인덱스인 3은 뺴고(스킵합) 평균을 낸것임.


print("")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
avg = average_list(data, 2, 7, [4])
#코드만 보고 이해하기 어렵다.

avg = average_list(data, 2, end=7, skip=[4])
avg = average_list(data=data, start=2, end=7, skip=[4])
#입력 값이 어느 입력인자로 들어가야 하는지 명시적으로 보여줄 수 있다.
#이렇게 입력하는 인자를 keyword argument (키워드 인자)라 한다.
#위치 인자와 섞어 쓸 경우 키워드 인자는 반드시 위치 인자 뒤에 나와야 한다
#기존 방식대로 순서에 의해 할당되는 입력 인자를 positional argument (위치 인자)라 한다.

print("")
avg = average_list(end=7, start=2, skip=[4], data=data)
#키워드 인자끼리는 순서를 섞어도 실행이 된다.


print("\n")
def average_list_with_default(data, start=0, end=None, skip=None):
    if skip is None:
        skip = []
        #비어있는 리스트는 문법적으로 기본인자로 넣을 수 없음.
    return average_list(data, start, end, skip)

print("function default arguments")
avg = average_list_with_default(data)
avg = average_list_with_default(data, 3)
avg = average_list_with_default(data, end=5)
avg = average_list_with_default(data, skip=[3, 4])


print("\n")
if True:
    var_created = "created"
print("variable created inside block:", var_created)

if False:
    var_not_created = "not created"  #잘못된 코드라고 알려준다.
try:
    print("variable NOT created inside block:", var_not_created)
except NameError as ne:
    print(ne)
#단락 밖에서도 사용이 가능하기 때문에 그 단락이 돌지 않는다면 변수가 살아나지 않는 것을 주의



print("\n전역변수와 지역변수")
#함수 안에서 나오는 지역 변수
#함수 밖에서 나오는 전역 변수

global_var = 10
#전역 변수
def add_ten_local():
    local_var = global_var + 10
    #지역 변수
    print("add_ten_local:", local_var)

def add_ten_global():
    try:
        global_var = global_var + 10
        #이경우 내부에서 만들어진 로컬 변수로 인식이 된다.
        #지역 변수가 새롭게 만들어 졌는데 값이 없는 값을 그대로 썻기 때문에 에러가 뜬다.
        print("add_ten_global:", global_var)
    except NameError as ne:
        print(ne)

#데이터 값을 가지고 와서 사용하는 것은 글로벌 변수로 인식되지만
#데이터 값을 바꾸려 한다면 새로운 로컬 변수로 인식한다.

def add_ten_global_two_steps():
    try:
        local_var = global_var + 10
        global_var = local_var
        print("add_ten_global_two_steps:", global_var)
    except NameError as ne:
        print(ne)
#함수 내부에서 어떤 위치건 myvariable=value처럼 변수에 값을 넣는 코드가 있으면
# 그 변수는 모두 지역 변수로 인식하게 된다.
#즉 눈으로 보면 문제 없어보이지만 에러가 뜬다.

def add_ten_global_use_global():
    global global_var
    global_var = global_var + 10
    print("add_ten_global_use_global:", global_var)
#함수 내부에서 전역 변수의 값을 바꾸고 싶다면 함수 내부에서 global var_name을 선언해줘야 한다.

#글로벌 변수는 변하지 않는 상수 값일 때 쓰지 보통 값을 변경시키지는 않는다.

add_ten_local()
add_ten_global()
add_ten_global_two_steps()
add_ten_global_use_global()
print("global_var=", global_var)
add_ten_global_use_global()
print("global_var=", global_var)
#변수에 10을 더했지 때문


print("\n")
#함수 밖에 생성된 변수들은 모두 전역 변수(global variable)로 인식되어
#함수 내부 변수들과 섞여서 버그를 유발할 가능성이 높다.

#따라서 모든 코드는 함수 안에 있어야한다.

#스크립트에서 실행될 메인 함수를 먼저 만들고 함수 밖에는 메인 함수를 호출하는 코드만 넣는다.
#메인 함수를 먼저 쓰고 메인 함수 안에서는 코드를 기능별로 묶어서 세부 함수로 나누어 세부 함수들을 호출한다.
#불러내는 순서순으로 코드를 배치하는게 좋다.

def main():
    print("function default arguments")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    avg = average_list_with_default(data)
    avg = average_list_with_default(data, 3)

def average_list_with_default(data, start=0, end=None, skip=None):
    if skip is None:
        skip = []
    return average_list(data, start, end, skip)

def average_list(data, start, end, skip):
    if end is None:
        avg_data = data[start:]
    else:
        avg_data = data[start:end]

    sum = 0
    skip_count = 0
    for ind, num in enumerate(avg_data):
        if ind in skip:
            skip_count += 1
        else:
            sum += num
    dlen = len(avg_data) - skip_count
    average = sum / dlen
    print(f"average {start}~{end}, skip={skip} over {len(data)} numbers = {average}")
    return average

if __name__ == '__main__':
    main()
#이 스크립트 파일이 직접 실행이 된 것인지를 확인하는 것이다.
#이게 없으면 그냥 함수 선언만 한 것이기 떄문에 사용이 불가능하다.

#호출하는 함수는 호출 받는 함수 위에 있어야 위에서부터 아래로 코드를 쉽게 읽을 수 있다.
# 신문처럼 자연스럽게 읽을 수 있는 코드가 좋은 코드다.
