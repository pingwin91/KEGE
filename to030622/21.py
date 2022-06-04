def f(x, y, n):
    if x + y >= 77 or n > 4:
        return n == 2 or n == 4
    if n % 2 == 0:
        return all([f(x + 1, y, n + 1), f(x + y * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y + x * 2, n + 1)])
    return any([f(x + 1, y, n + 1), f(x + y * 2, y, n + 1), f(x, y + 1, n + 1), f(x, y + x * 2, n + 1)])


for s in range(1, 68):
    if f(9, s, 0):
        print(s)
        break


'''
21
'''