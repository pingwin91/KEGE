for x in range(10000):
    n = x
    k = 0
    r = 9
    y = x % 10
    while x > 0:
        k += 1
        if r > x % 10:
            r = x % 10
        x //= 10
    r = y - r
    if k == 4 and r == 3:
        print(n)
        break


'''
1003
'''