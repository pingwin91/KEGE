def f(x, y, n):
    if x * y >= 144 or n > 3:
        return n == 3
    if n % 2 == 1:
        return all([f(x + 1, y, n + 1),
                    f(x * 2, y, n + 1),
                    f(x, y + 1, n + 1),
                    f(x, y * 2, n + 1)])
    return any([f(x + 1, y, n + 1),
                f(x * 2, y, n + 1),
                f(x, y + 1, n + 1),
                f(x, y * 2, n + 1)])


for s in range(1, 142):
    if f(1, s, 0):
        print(s)