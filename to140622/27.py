### 27A
f = open('27_A.txt')
n = int(f.readline())

duo = []
max_sum = 0
for i in f:
    n1, n2 = map(int, i.split())
    maximum = max(n1, n2)
    minimum = min(n1, n2)
    duo.append((maximum - minimum, maximum, minimum))
    max_sum += maximum

if max_sum % 2 == 0:
    duo.sort()
    i = 0
    while duo[i][0] % 2 == 0:
        i += 1
    max_sum -= duo[i][0]

print(max_sum, end='\t')


### 27B
f = open('27_B.txt')
n = int(f.readline())

duo = []
max_sum = 0
for i in f:
    n1, n2 = map(int, i.split())
    maximum = max(n1, n2)
    minimum = min(n1, n2)
    duo.append((maximum - minimum, maximum, minimum))
    max_sum += maximum

if max_sum % 2 == 0:
    duo.sort()
    i = 0
    while duo[i][0] % 2 == 0:
        i += 1
    max_sum -= duo[i][0]

print(max_sum, end='\t')