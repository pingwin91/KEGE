for x in range(1000, 10000):
    n = x
    x = str(x)
    summs = sorted([int(x[0]) + int(x[1]), int(x[1]) + int(x[2]), int(x[2]) + int(x[3])])
    ans_x = str(summs[1]) + str(summs[0])
    if ans_x == '127':
        print(n)

'''
9934
'''