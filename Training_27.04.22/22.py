for x in range(1000, 0, -1):
    q = 7
    p = 10
    k1 = 0
    k2 = 0
    n = x
    while x <= 100:
        k1 += 1
        x += p
    while x >= q:
        k2 += 1
        x -= q
    L = x + k1
    M = x + k2
    if L == 11 and M == 20:
        print(n)
        break