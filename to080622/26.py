with open('26.txt') as f:
    n, value = map(int, f.readline().split())
    points = []
    for i in f:
        points.append(int(i))
    points.sort(reverse=True)

if points[value - 1] > points[value]:
    max_point = points[value - 1]
else:
    for i in range(value - 1, 0, -1):
        if points[i] > points[value - 1]:
            max_point = points[i]
            break
index_out = value
while points[index_out] == points[value]:
    index_out += 1
sum_out = 0
for i in range(index_out, n):
    sum_out += points[i]
middle_out = round(sum_out / (n - index_out))

print(max_point, middle_out)