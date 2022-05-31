f = open('17.txt')

numbers = []
count = 0
max_sq = 0
for i in f:
    numbers.append(int(i))
    if len(numbers) > 1 and (numbers[-1] > 700 or numbers[-2] > 700):
        count += 1
        max_sq = max(max_sq, numbers[-1] ** 2 + numbers[-2] ** 2)

print(count, max_sq)


#  3902 197073925