'''columns = ['name', 'age', 'gender', 'country']
data = {}

for column in columns:
    data[column] = []

print(data)


newdata = {'name': 'tom', 'age': 3, 'gender': 'male', 'country': 'usa'}

print(newdata)
'''
'''
print(list(data.keys()))
print(list(newdata.keys()))
print(list(enumerate((data.keys()))))
print(list(enumerate((data.items()))))
print(list(enumerate(newdata.keys())))
print(list(enumerate(newdata.items())))
'''
'''

data_col_key = list(data.keys())
print(data_col_key)
new_data_col_key = list(newdata.keys())
print(new_data_col_key)

print(len(data_col_key))
print(range(len((data_col_key))))
print(len(new_data_col_key))
print(range(len((new_data_col_key))))


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
    print(data)
'''



'''
print("\n")
data1 = {'name': ['tom', 'lee', 'kim'], 'age': [3, 4, 5]}
names = []

i = 0
print(f"remove {names}")
while i < len(data1['name']):
    #i가 name안에 있는 수를 넘을 수 없게
    if data1['name'][i] in names:
        for key in data1.keys():
            del data1[key][i]
        i = 0
    else:
        i = i + 1

if len(data1['name']) <= 0:
    print("name is empty!")


print(data1)


#tottenham.remove('Moura')
#print("remove moura:", tottenham)
# remove(): 입력한 원소를 삭제
'''


'''
data = {'name': ['tom', 'lee', 'kim'], 'age': [4, 2, 3]}

age_min = 2
age_max = 6


print(f"{age_min} <= age < {age_max}")

query_data={}
for key in data.keys():
    query_data[key] = []
print(query_data)


for query_name in names:
    for i in range(len(data['name'])):
        if query_name == data['name'][i]:
            for key, value in data.items():
                query_data[key].append(value[i])

print("herer",query_data)


print(range(age_min,age_max))
for query_age in range(age_min,age_max):
    for i in range(len(data['age'])):
        if query_age == data['age'][i]:
            for key, value in data.items():
                query_data[key].append(value[i])

print(query_data)
'''

'''
data = {'name': ['tom', 'kim'], 'age': [3, 5]}
other = {'name': ['lee', 'kim', 'kim'], 'age': [4, 7, 8]}

print(f"data : {data} \nother : {other}")
print(f"other값을 data에 추가합니다.")

# if 'other' has the same names with 'data', ignore the duplicated data

for i in range(len(other['name'])):
    if other['name'][i] not in data['name']:
        for key, value in other.items():
            data[key].append(value[i])

    elif other['name'][i] in data['name']:
        print(f"{other['name'][i]}은 이미 있습니다. 추가한 {other['age'][i]}값을 제외합니다. ")

print(data)
'''


data = {'name': ['tom', 'kim','asdfd','assdfsd'], 'age': [3, 5,6, 7], 'cosafdasn': ['asdf', 'adffe', 'efgrgr', 'eewqgww']}




for i in range(len(data)):
#key의 수
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




#merge_data = {name, value for name, value in zip(data, other)}
#print(merge_data)



'''
for newdata_index, new_col_key in enumerate(newdata.keys()):
    print(f"index={newdata_index}, column={new_col_key}")


for data_index, data_col_key in enumerate(data.keys()):
    print(f"index={data_index}, column={data_col_key}")

for newdata_index, new_col_key in enumerate(newdata.keys()):
    print(f"index={newdata_index}, column={new_col_key}")

print(data)

for key in newdata.keys():
    if key not in data:
        print(f"{key}는 없쪙")
        
        
        
    elif key in data:
        data[key] = newdata[key]
        print(data)

print(data)
'''

#for key, value in hero_names.items():
#    print(f"{key} is {value}")


#if list(data_index) == list(newdata_index):
#    print("1st it's ok")
#    if list(data.keys) == list(newdata.keys):
#       for key, value in newdata.items():
#            data[key].append(value)
#            print(list(data))



#    else:
#        print("plz checkk!!!")

#else:
#    print("plz check")


#    assert list(newdata.keys()) in list(data.keys()), f"'{newdata[index]}' is NOT in this database"


#for index, col_key in enumerate(newdata.keys()):
#    print(f"index={index}, column={col_key}")



#assert 'country' in newdata, 'country is not in newdata'

#man_heroes = [hero for hero in marvel_heroes if hero.endswith("man")]
#print("man heroes:", man_heroes)


#for keys in enumerate(list(newdata.keys())):
#    if keys not in enumerate(list(data.keys())):
#        print(f"'{newdata.keys()}' is NOT in this database")
#    else:
#        print("ok")