for i in range(128, 256):
    n = bin(i)[2:]
    new_n = ''
    for j in n:
        if j == '0':
            new_n += '1'
        else:
            new_n += '0'
    n = int(new_n, 2)
    if i - n == 105:
        print(i)