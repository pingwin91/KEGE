###### 27.A ######
f = open('27a.txt')
n = int(f.readline())

duo = []
max_sum = 0
for i in f:
    i1, i2 = map(int, i.split())
    duo.append((max(i1, i2), min(i1, i2), max(i1, i2) - min(i1, i2)))
    max_sum += max(i1, i2)

if max_sum % 43 != 0:
    print(max_sum)

###### 27.B ######
f = open('27b.txt')
n = int(f.readline())

duo = []
max_sum = 0
for i in f:
    i1, i2 = map(int, i.split())
    duo.append((max(i1, i2), min(i1, i2), max(i1, i2) - min(i1, i2)))
    max_sum += max(i1, i2)

if max_sum % 43 != 0:
    print(max_sum)
else:
    duo.sort(key=lambda x: x[2])
    i = 0
    while duo[i][2] % 43 == 0:
        i += 1
    else:
        max_sum -= duo[i][0]
        max_sum += duo[i][1]
        print(max_sum)