result_list = []

index = 1
result = 0
while index <= 10:
    result = result + index
    result_list.append(result)
    index = index+ 1

print(result)
print(result_list)

anser = sum(result_list)
print(anser)


#####
def sum(a, b):
    c = a + b
    return c

index = 1
result = 0
while index <= 10:
    result = result + index
    index = index+ 1

print(result)