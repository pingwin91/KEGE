with open('26.txt') as f:
    value, n = map(int, f.readline().split())
    numbers = []
    for i in f:
        numbers.append(int(i))
    numbers.sort()

count = 0
summa = 0
i = 0
while summa <= value:
    summa += numbers[i]
    count += 1
    i += 1
else:
    print(count - 1, end=' ')
    summa -= numbers[i] + numbers[i - 1]
    i -= 2

max_el = 0
while summa + numbers[i] <= value:
    if summa + numbers[i] <= value:
        max_el = max(max_el, numbers[i])
    i += 1

print(max_el)


#  3082 76