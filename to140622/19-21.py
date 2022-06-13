### 19 -> 28
def f(x, y, n):
    if x + y >= 90 or n > 1:
        return n == 1
    return any([f(x + 1, y, n + 1), f(x * 3, y, n + 1), f(x, y + 1, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 82):
    if f(8, s, 0):
        print(s)
        break


### 20 -> 9 17 26
def f(x, y, n):
    if x + y >= 90 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 1, y, n + 1), f(x * 3, y, n + 1), f(x, y + 1, n + 1), f(x, y * 3, n + 1)])
    return any([f(x + 1, y, n + 1), f(x * 3, y, n + 1), f(x, y + 1, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 82):
    if f(8, s, 0):
        print(s)


### 21 -> 27
def f(x, y, n):
    if x + y >= 90 or n > 4:
        return n == 2 or n == 4
    if n % 2 == 0:
        return all([f(x + 1, y, n + 1), f(x * 3, y, n + 1), f(x, y + 1, n + 1), f(x, y * 3, n + 1)])
    return any([f(x + 1, y, n + 1), f(x * 3, y, n + 1), f(x, y + 1, n + 1), f(x, y * 3, n + 1)])


for s in range(1, 82):
    if f(8, s, 0):
        print(s)
        break