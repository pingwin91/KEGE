for x in range(1000):
    n = x
    a = 0
    b = 0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 10
        x //= 10
    if a == 3 and b == 14:
        print(n)
        break
