def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return f(x + 1, y) + f(x * 2, y) + f(x * 5, y)

print(f(1, 10) * f(10, 20) * f(20, 38))


#  36