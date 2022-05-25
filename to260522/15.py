for A in range(1, 111):
    flag = 0
    for x in range(111):
        for y in range(111):
            f = (x > A) or (y > A) or (2 * y + x < 110)
            if f == 0:
                flag = 1
                break
        if flag == 1:
            break
    else:
        print(A)