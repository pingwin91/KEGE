def f(n):
    if n == 1:
        return 3
    if n % 2 == 0:
        return n + f(n // 2)
    else:
        return 3 * f(n - 1)


print(f(115))

'''
1791
'''