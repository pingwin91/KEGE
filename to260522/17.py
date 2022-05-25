f = open('17.txt')
numbers = []
for i in f:
    numbers.append(int(i))

count = 0
max_sum = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] * numbers[j] % 62 == 0:
            count += 1
            max_sum = max(max_sum, numbers[i] + numbers[j])

print(count, max_sum)