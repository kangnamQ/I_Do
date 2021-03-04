def init_columns(col_names):
    print(f"\n다음과 같은 columns를 추가합니다:\n{col_names}")

    data = {}
    for column in col_names:
        data[column] = []

    return data

"""
    col_names: list of column titles (string) e.g.=['name', 'age']
    return: empty database e.g.={'name': [], 'age': []}
"""



def append(data, newdata):
    print(f"\nnewdata값을 data에 추가합니다.")
    print(f"data : {data} \nnewdata : {newdata}\n")



    data_col_key = list(data.keys())
    new_data_col_key = list(newdata.keys())
    if data_col_key != new_data_col_key:
        if len(data_col_key) != len(new_data_col_key):
            for i in range(len(new_data_col_key)):
                if new_data_col_key[i] not in data_col_key:
                    print(f"'{new_data_col_key[i]}' is NOT in this database")
            for j in range(len(data_col_key)):
                if data_col_key[j] not in new_data_col_key:
                    print(f"'{data_col_key[j]}' is NOT in this newdata")
        else:
            for i in range(len(new_data_col_key)):
                if new_data_col_key[i] not in data_col_key:
                    print(f"'{new_data_col_key[i]}' is NOT in this database")

    else:
        for key, value in newdata.items():
            data[key].append(value)

    return data
    #data에 직접 관여해야 한다고 생각해 data로 반환

"""
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee'], 'age': [3, 4]}
    newdata: new data to be appended (dict) e.g.={'name': 'kim', 'age': 5}
    return: appended database e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}

    [Note] if one of keys of 'newdata' is NOT in 'data', print WARNING message
    e.g. newdata={'name': 'kim', 'gender': 'male'}
        -> print("'gender' is NOT in this database")

    [Note] if 'newdata' does NOT have all keys in 'data', raise error using assert
    e.g. newdata={'name': 'kim'}
        assert 'age' in newdata, "'age' is NOT in newdata"
"""

def print_data(data):
    print(f"\ndata를 출력합니다.\n")

    for i in range(len(data)):
        # key의 수
        print(f"{list(data)[i]}".ljust(15), end=" ")
    print("")

    for j in range(len(data)):
        num_of_letter = int((len(list(data.keys())[j])))
        num_of_dash = ("-" * num_of_letter)
        print(num_of_dash.ljust(15), end=" ")
    print("")

    for k in range(len(data['name'])):
        for key in data:
            print(f"{data[key][k]}".ljust(15), end=" ")
        print("")
    print("")

    """
    data: database object (dict of lists) e.g.={'name': ['tom', 'kim'], 'age': [3, 5]}
    print database vertically
    e.g.
    name    age
    ----    ---
    tom     3
    kim     5
    """



def query_by_name(data, names):
    print(f"\n다음의 이름을 가진 데이터를 가져옵니다:\n{names}")

    query_data = {}
    for key in data.keys():
        query_data[key] = []
    #query_data = init_columns(list(data) 로 단축가능
    #def속에 def를 쓸경우 오류의 여부가 불확실하여 안전하게 풀어서 작성.

    for query_name in names:
        for i in range(len(data['name'])):
            if query_name == data['name'][i]:
                for key, value in data.items():
                    query_data[key].append(value[i])
    return query_data
    #정렬, 찾기라고 생각해서 기존 data에 병합하지 않고 새로운 query_data 생성하고 값을 반환.

"""
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    names: list of names e.g.=['kim', 'tom']
    return: extracted database e.g.={'name': ['kim', 'tom'], 'age': [5, 3]}
"""



def query_by_age(data, age_min, age_max):
    print(f"\n다음의 범위안의 나이를 가진 데이터를 불러옵니다:\n{age_min} <= age < {age_max}")

    query_data = {}
    for key in data.keys():
        query_data[key] = []
    #query_data = init_columns(list(data) 로 단축가능
    #def속에 def를 쓸경우 오류의 여부가 불확실하여 안전하게 풀어서 작성.

    for query_age in range(age_min, age_max):
    # range특성상 끝 숫자(age_max)는 해당 범위에 포함되지 않음.
        for i in range(len(data['age'])):
            if query_age == data['age'][i]:
                for key, value in data.items():
                    query_data[key].append(value[i])
    return query_data
    #정렬, 찾기라고 생각해서 기존 data에 병합하지 않고 새로운 query_data 생성하고 값을 반환.

"""
    extract database of which age_min <= age < age_max
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    age_min: minimum age e.g.=2
    age_max: maximum age e.g.=5
    return: extracted database e.g.={'name': ['tom', 'lee'], 'age': [3, 4]}
"""



def merge(data, other):
    print(f"\nother값을 data에 추가합니다.")
    print(f"data : {data} \nother : {other}")


    for i in range(len(other['name'])):
        if other['name'][i] not in data['name']:
            for key, value in other.items():
                data[key].append(value[i])
        elif other['name'][i] in data['name']:
            print(f"{other['name'][i]}은 이미 있습니다. 추가한 {other['age'][i]}값을 제외합니다. ")
    return data

"""
    data: database object (dict of lists) e.g.={'name': ['tom', 'kim'], 'age': [3, 5]}
    other: database object (dict of lists) e.g.={'name': ['lee'], 'age': [4]}
    return: merged database e.g.={'name': ['tom', 'kim', 'lee'], 'age': [3, 5, 4]}
    [Note] if 'other' has the same names with 'data', ignore the duplicated data
    e.g. data={'name': ['tom', 'kim'], 'age': [3, 5]}
        other={'name': ['lee', 'kim'], 'age': [4, 6]}
        -> {'name': ['tom', 'kim', 'lee'], 'age': [3, 5, 4]}
"""



def remove_by_name(data, names):
    print(f"remove : {names}")
    i = 0
    while i < len(data['name']):
        # i가 name안에 있는 수를 넘을 수 없게
        if data['name'][i] in names:
            for key in data.keys():
                del data[key][i]
            i = 0
            #이름이 동일 하다면, 삭제하고 다른 삭제할 것이 있나 초반으로 다시 복귀
        else:
            i = i + 1
            #이름이 동일한 것이 없으면 +1을 계속 받아 len(data['name'])을 넘어 while에서 나옴.
    if len(data['name']) <= 0:
        print("name is empty!")
        #만약 이름칸에 없을 경우를 대비한 if문
    return data
    #data에 직접 관여해야 한다고 생각해 data로 반환

"""
    data: database object (dict of lists) e.g.={'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
    names: list of names e.g.=['kim', 'tom']
    return: reduced database e.g.={'name': ['lee'], 'age': [4]}
"""

