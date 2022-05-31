for x in range(100, 1, -1):
    n = x
    p = 0
    s = 5 * (x - x % 21)
    i = 1
    while p < s:
        s = s - 3 * i
        p = p + i
        i += 1
    if s == 42 and p == 91:
        print(n)
        break


#  83
