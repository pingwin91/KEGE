# part A
f = open('27A.txt')
n = int(f.readline())
numbers = []
for i in f:
    numbers.append(int(i))

R = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (numbers[i] + numbers[j]) % 3 == 0:
            R = max(R, numbers[i] + numbers[j])
if R > 0:
    print(R)
else:
    print(1)


# part B
f = open('27B.txt')
n = int(f.readline())
numbers = []
for i in f:
    numbers.append(int(i))

R = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (numbers[i] + numbers[j]) % 3 == 0:
            R = max(R, numbers[i] + numbers[j])
if R > 0:
    print(R)
else:
    print(1)