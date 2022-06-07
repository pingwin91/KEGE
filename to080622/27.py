### файл А
with open('27_A.txt') as f:
    n = int(f.readline())
    numbers = []
    for i in range(5):
        numbers.append(int(f.readline()))
    min_until_index = min(numbers)
    min_del_3 = min(numbers, key=lambda x: x % 3 == 0)
    min_multiply3 = 99999999
    index = 4
    for i in f:
        index += 1
        numbers.append(int(i))
        if int(i) % 3 == 0:
            min_multiply3 = min(min_multiply3, min_until_index * int(i))
        else:
            min_multiply3 = min(min_multiply3, min_del_3 * int(i))
        min_until_index = min(min_until_index, numbers[index - 4])
        if numbers[index - 4] % 3 == 0:
            min_del_3 = min(min_del_3, numbers[index - 4])

print(min_multiply3, end=' ')


### файл B
with open('27_B.txt') as f:
    n = int(f.readline())
    numbers = []
    for i in range(5):
        numbers.append(int(f.readline()))
    min_until_index = min(numbers)
    min_del_3 = min(numbers, key=lambda x: x % 3 == 0)
    min_multiply3 = 99999999
    index = 4
    for i in f:
        index += 1
        numbers.append(int(i))
        if int(i) % 3 == 0:
            min_multiply3 = min(min_multiply3, min_until_index * int(i))
        else:
            min_multiply3 = min(min_multiply3, min_del_3 * int(i))
        min_until_index = min(min_until_index, numbers[index - 4])
        if numbers[index - 4] % 3 == 0:
            min_del_3 = min(min_del_3, numbers[index - 4])

print(min_multiply3)


'''
108 12420
'''