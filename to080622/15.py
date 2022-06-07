def sumbigger(x, y):
    return x + y > 0


for z in range(-100, 100):
    for x in range(-100, 100):
        f = (not(sumbigger(x, z + 1))) or (sumbigger(x, -7) or (not sumbigger(x, 7)))
        if f == 0:
            break
    else:
        print(z)

'''
-8
'''