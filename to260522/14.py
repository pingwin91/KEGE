def to6(x):
    new_number = ''
    while x > 0:
        new_number += str(x % 6)
        x //= 6
    return new_number[::-1]


for x in range(1000):
    n = 216 ** 5 + 6 ** 3 - 1 - x
    if to6(n).count('5') == 12:
        print(x)
        break