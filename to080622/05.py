for x in range(150):
    n = bin(2 * x)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    if int(n, 2) > 123:
        print(x)
        break

'''
16
'''