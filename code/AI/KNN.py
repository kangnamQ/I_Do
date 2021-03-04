from math import sqrt

#유클리드 거리
#2개 벡터 사이의 거리를 계산한다.
def cal_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)


#[x좌표, y좌표, class 번호]
dataset = [[1.78, 1.76, 0],
           [1.46, 0.34, 0],
           [2.76, 3.14, 0],
           [1.89, 1.99, 0],
           [1.46, 0.34, 0],
           [7.55, 8.77, 1],
           [6.25, 7.12, 1],
           [9.15, 6.34, 1],
           [6.77, 8.54, 1],
           [6.23, 5.82, 1]]

some_row = dataset[0]
for row in dataset:
    distance = cal_distance(some_row, row)
    print(distance)
    
    
#가장 유사한 이웃을 찾는다.
#(학습 데이터, 새로운데이터, k와 동일한 개념)
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    #리스트 생성자 ()
    for train_row in train:
        #모든 row에 대해서 학습데이터와 새로운 데이터의 거리 계산
        dist = cal_distance(test_row, train_row)
        #거리와 함께 학습데이터 까지 넣어가지고 리스트에 추가
        distances.append((train_row, dist))
        #튜플로 만들어서 넣는다는것에 주의
        
    distances.sort(key=lambda tup: tup[1])
    #list에서 내장함수 및 sort라는 메소드를 사용하여 정렬하는 방법
    #사용하면 영구적으로 변경
    #키가 중요하며 lambda식은 함수에 이름을 주지 않으며 빠르게 만들 수 있는 방법
    #tup라는 것이 함수이며 tup의 두번째 인수 [1] (0,1)을 사용하여 정렬하는 방법
    #즉 dist를 기준으로 정렬하라는 뜻임.
    
    neighbors = list()
    for i in range(num_neighbors):
        #num neighbors 만큼 반복
        neighbors.append(distances[i][0])
        #distances에서 처음 k개를 추 려내서 반환하기 위함
        #정렬 = 작은 순으로 되어있기 때문에 k개를 추려내는 것
    return neighbors



dataset = [[1.78, 1.76, 0],
           [1.46, 0.34, 0],
           [2.76, 3.14, 0],
           [1.89, 1.99, 0],
           [1.46, 0.34, 0],
           [7.55, 8.77, 1],
           [6.25, 7.12, 1],
           [9.15, 6.34, 1],
           [6.77, 8.54, 1],
           [6.23, 5.82, 1]]

neighbors = get_neighbors(dataset, dataset[0], 3)
for neighbor in neighbors:
    print(neighbor)
    
    
    
#예측합수
def predict(train, test_row, num_neighbors):
    #가장 근접한 k개의 이웃을 얻을 수 있음
    neighbors = get_neighbors(train, test_row, num_neighbors)
    
    #neighbors로 들어온 모든 행에 대해서 맨 마지막 번째
    #맨 마지막 번째에 클래스 넘버가 들어가 있기 때문
    #그 클래스 넘버만 들어가있는 리스트를 만들음
    output_values = [row[-1] for row in neighbors]
    
    #output_values를 집합으로 만든다. 
    # -> 리스트를 집합으로 만들면 중복되는 것은 다 없어진다.
    # ex) [0,0,1] -> [0,1]
    
    #max 최대값을 구하는 연산에서 key가 기준이 되는 것이다.
    #output values의 count를 기준으로 하겠다. 
    #리스트에서 카운트를 부른다면 해당 숫자가 몇 번 나오는지 값이 나온다.
    #즉 0은 2개, 1은 1개로 보인다는 것이다.

    prediction = max(set(output_values), key=output_values.count)
    #max연산은 0이 나오기 떄문에 prediction은 0이되는 것이다.
    return prediction


list1 = [2, 3, 4, 3, 10, 3, 5, 6, 3]
##리스트의 카운트라는 method를 부르면은
# 3이 몇번이나 반복이 되는지 구할 수 있다.
elm_count = list1.count(3)
print('The count of element : 3 is', elm_count)


dataset = [[1.78, 1.76, 0],
           [1.46, 0.34, 0],
           [2.76, 3.14, 0],
           [1.89, 1.99, 0],
           [1.46, 0.34, 0],
           [7.55, 8.77, 1],
           [6.25, 7.12, 1],
           [9.15, 6.34, 1],
           [6.77, 8.54, 1],
           [6.23, 5.82, 1]]

prediction = predict(dataset, dataset[0], 3)
print("정답 %d, 예측값 %d." %(dataset[0][-1], prediction))