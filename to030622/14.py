def to5(x):
    n = ''
    while x > 0:
        n += str(x % 5)
        x //= 5
    return n[::-1]


x = 125 ** 300 * 5 ** 300 - 25 ** 70 - 100
print(to5(x).count('4'))


'''
1196
'''