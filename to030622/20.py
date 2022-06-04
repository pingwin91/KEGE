def f(x, y, n):
    if x + y >= 77 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 1, y, n + 1), f(x + y * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y + x * 2, n + 1)])
    return any([f(x + 1, y, n + 1), f(x + y * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y + x * 2, n + 1)])


for s in range(1, 67):
    if f(9, s, 0):
        print(s)


'''
7 22
'''