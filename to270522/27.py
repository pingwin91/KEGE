# 27_A
with open('27_A.txt') as f:
    n = int(f.readline())
    ost = [[], [], [], []]
    for i in range(n):
        digit = int(f.readline())
        ost[digit % 4].append(digit)
summa = 0
for i in ost:
    summa += max(i)

print(summa)


# 27_B
with open('27_B.txt') as f:
    n = int(f.readline())
    ost = [[], [], [], []]
    for i in range(n):
        digit = int(f.readline())
        ost[digit % 4].append(digit)
summa = 0
for i in ost:
    summa += max(i)

print(summa)