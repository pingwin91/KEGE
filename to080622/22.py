for x in range(1000):
    n = x
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 2 != 0:
            b += 1
        x //= 2
    if b == 3 and a == 7:
        print(n)
        break

'''
67
'''