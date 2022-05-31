for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not ((x == y) or (x == z))) or w or (not (y <= z))
                if f == 0:
                    print(x, y, z, w)


#  xwyz