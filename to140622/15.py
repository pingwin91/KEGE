def delit(x, y):
    return x % y == 0

for a in range(1, 100):
    for x in range(1, 1000):
        f = delit(x, a) <= ((not delit(x, 35)) or delit(x, 49))
        if f == 0:
            break
    else:
        print(a)
        break


'''
29
'''