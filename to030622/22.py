for i in range(1000):
    x = i
    d = 0
    while x > 0:
        d = d * 10 + x % 3
        x //= 3
    if d > 99 and d % 10 == 2:
        print(i)
        break

'''
19
'''