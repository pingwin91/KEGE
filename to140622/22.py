for x in range(1, 1000):
    n = x
    a = 0
    b = 10
    while x > 0:
        k = x % 10
        a += k
        if k < b:
            b = k
        x //= 10
    if a == 15 and b == 7:
        print(n)
        break

'''
78
'''