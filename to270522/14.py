def to3(x):
    new_number = ''
    while x > 0:
        new_number += str(x % 3)
        x //= 3
    return new_number[::-1]


for x in range(1000000):
    n = 243 ** 5 + 3 ** 7 - 2 - x
    if to3(n).count('2') == 20:
        print(x)
        break

#  2307