### 19
def f(x, y, n):
    if x + y >= 808 or n > 2:
        return n == 2
    return any([f(x + 2, y, n + 1), f(x * 3, y, n + 1), f(x, y + 2, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 301):
    if f(35, s, 0):
        print(s)
        break


### 20
def f(x, y, n):
    if x + y >= 808 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 2, y, n + 1), f(x * 3, y, n + 1), f(x, y + 2, n + 1), f(x, y * 3, n + 1)])
    return any([f(x + 2, y, n + 1), f(x * 3, y, n + 1), f(x, y + 2, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 301):
    if f(35, s, 0):
        print(s)


### 21
def f(x, y, n):
    if x + y >= 808 or n > 4:
        return n == 2 or n == 4
    if n % 2 == 0:
        return all([f(x + 2, y, n + 1), f(x * 3, y, n + 1), f(x, y + 2, n + 1), f(x, y * 3, n + 1)])
    return any([f(x + 2, y, n + 1), f(x * 3, y, n + 1), f(x, y + 2, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 301):
    if f(35, s, 0):
        print(s)
        break
'''
19 -> 86
20 -> 234 255
21 -> 232
'''