# 19
def f(x, y, n):
    if x + y >= 62 or n > 2:
        return n == 2
    return any([f(x + 1, y, n + 1), f(x * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y * 2, n + 1)])

for s in range(52):
    if f(10, s, 0):
        print(s)
        break


# 20
def f(x, y, n):
    if x + y >= 62 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 1, y, n + 1), f(x * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y * 2, n + 1)])
    return any([f(x + 1, y, n + 1), f(x * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y * 2, n + 1)])

for s in range(52):
    if f(10, s, 0):
        print(s)


# 21
def f(x, y, n):
    if x + y >= 62 or n > 4:
        return n == 4 or n == 2
    if n % 2 == 0:
        return all([f(x + 1, y, n + 1), f(x * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y * 2, n + 1)])
    return any([f(x + 1, y, n + 1), f(x * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y * 2, n + 1)])

for s in range(52):
    if f(10, s, 0):
        print(s)