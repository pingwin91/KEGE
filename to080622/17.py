with open('17.txt') as f:
    numbers = []
    for i in f:
        numbers.append(int(i))

count = 0
delta = 0
for i in range(len(numbers) - 1):
    if numbers[i + 1] < numbers[i]:
        count += 1
        delta = max(delta, numbers[i] - numbers[i + 1])

print(count, delta)


'''
2514 963
'''