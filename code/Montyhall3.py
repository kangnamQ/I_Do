import random

length = 100000

list = [random.randrange(0, 3) for i in range(length)]
# print list

o_true_sum = 0
o_false_sum = 0
c_true_sum = 0
c_false_sum = 0

for i in range(length):

    select = random.randrange(0, 3)
    if list[i] == select:
        # true_sum+=1
        temp = random.randrange(1, 3) + list[i]

        if temp == 3:
            temp = 0
        # print list[i], 'correct', temp
        o_true_sum += 1
        c_false_sum += 1

    else:
        # false_sum+=1
        temp = random.randrange(1, 3) + list[i]

        if temp == 3:
            temp = 0
        # print list[i], 'false', temp
        o_false_sum += 1
        c_true_sum += 1

print(100 * o_true_sum / length,"%")
print(100 * c_true_sum / length,"%")

#출처: https: // gongnorina.tistory.com / category / Machine
