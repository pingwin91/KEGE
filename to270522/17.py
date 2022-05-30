with open('17.txt') as f:
    numbers = [int(i) for i in f]

count = 0
max_sum = 0
for i in range(len(numbers) - 1):
    if numbers[i] % 5 == numbers[i + 1] % 5 == 0:
        count += 1
        max_sum = max(max_sum, numbers[i] + numbers[i + 1])

print(count, max_sum)

# 213 965