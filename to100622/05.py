for x in range(100):
    x = bin(x)[2:]
    x += str(x.count('1') % 2)
    x += str(x.count('1') % 2)
    if int(x, 2) <= 57:
        print(int(x, 2))

'''
54
'''