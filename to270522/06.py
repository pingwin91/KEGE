for n in range(100000):
    x = 0
    p = 0
    a = n
    while p + x < 1050:
        p += a
        x += 1
    if x == 19:
        print(n)
        break

#  19