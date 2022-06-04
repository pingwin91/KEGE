### для файла А
f = open('27_A.txt')
n = int(f.readline())
duos = []
max_sum = 0
for i in f:
    tuple_two_numbers = tuple(map(int, i.split()))
    max_num = max(tuple_two_numbers)
    max_sum += max_num
    min_num = min(tuple_two_numbers)
    duos.append((max_num - min_num, max_num, min_num))

if max_sum % 4 == 0:
    duos.sort()
    print(duos)
    i = 0
    while duos[i][0] % 4 == 0:
        i += 1
    max_sum -= duos[i][1]
    max_sum += duos[i][2]
print(max_sum)

### для файла В
f = open('27_B.txt')
n = int(f.readline())
duos = []
max_sum = 0
for i in f:
    tuple_two_numbers = tuple(map(int, i.split()))
    max_num = max(tuple_two_numbers)
    max_sum += max_num
    min_num = min(tuple_two_numbers)
    duos.append((max_num - min_num, max_num, min_num))

if max_sum % 4 == 0:
    duos.sort()
    i = 0
    while duos[i][0] % 4 == 0:
        i += 1
    max_sum -= duos[i][1]
    max_sum += duos[i][2]
print(max_sum)