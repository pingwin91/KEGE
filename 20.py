def f(x, n):
    if x >= 40 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 2, n + 1), f(x * 2, n + 1)])
    return any([f(x + 2, n + 1), f(x * 2, n + 1)])


for s in range(1, 39):
    if f(16, 0):
        print(s)