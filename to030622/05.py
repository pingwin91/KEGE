for x in range(100):
    n = x
    x = bin(x)[2:]
    if n % 2 == 0:
        x += '00'
    else:
        x += '10'
    if int(x, 2) > 130:
        print(n)
        break

'''
33
'''