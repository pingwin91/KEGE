for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= y) and (y or z) and w
                if f:
                    print(x, y, z, w)


'''
yzxw
'''