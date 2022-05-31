def to4(x):
    new = ''
    while x > 0:
        new += str(x % 4)
        x //= 4
    return new[::-1]


x = 4 ** 100 - 4 ** 65 + 16 ** 15 - 64
print(to4(x).count('3'))


#  62