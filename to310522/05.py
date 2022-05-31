for x in range(1, 60):
    x = bin(x)[2:]
    new_x = ''
    for i in x:
        new_x += i * 2
    x = int(new_x, 2)
    if x > 32:
        print(x)
        break


#  48