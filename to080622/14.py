x = 5 ** 200 + 25 ** 1000 - 5 ** 50
x_to5 = ''
while x > 0:
    x_to5 += str(x % 5)
    x //= 5
print(x_to5.count('0'))