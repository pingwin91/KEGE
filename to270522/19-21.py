# 19 -> 5
def f(s, n):
    if s >= 78 or n > 2:
        return n == 2
    return any([f(s + 1, n + 1), f(s + 3, n + 1), f(s * 4, n + 1)])


for s in range(1, 77):
    if f(s, 0):
        print(s)
        break


# 20 -> 1618
def f(s, n):
    if s >= 78 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(s + 1, n + 1), f(s + 3, n + 1), f(s * 4, n + 1)])
    return any([f(s + 1, n + 1), f(s + 3, n + 1), f(s * 4, n + 1)])


for s in range(1, 77):
    if f(s, 0):
        print(s)


# 21 -> 15
def f(s, n):
    if s >= 78 or n > 4:
        return n == 4 or n == 2
    if n % 2 == 0:
        return all([f(s + 1, n + 1), f(s + 3, n + 1), f(s * 4, n + 1)])
    return any([f(s + 1, n + 1), f(s + 3, n + 1), f(s * 4, n + 1)])


for s in range(1, 77):
    if f(s, 0):
        print(s)
        break