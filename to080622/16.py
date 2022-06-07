def f(n):
    if n < 3:
        return 2
    if n % 3 != 0:
        return 3 * f(n - 3)
    return n + 2 * f(n - 1)

print(f(27))

'''
26271
'''