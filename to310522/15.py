def f(x, y, a):
    return (x < a) and (y < a) and (x * y > 601)


for a in range(1000):
    flag = 0
    for x in range(1000):
        for y in range(1000):
            if f(x, y, a) == 1:
                flag = 1
                break
        if flag:
            break
    else:
        print(a)


#  25