def chet3(x):
    chet = '24680'
    count = 0
    for i in str(x):
        if i in chet:
            count += 1
    return count == 3


def nechet2(x):
    nechet = '13579'
    count = 0
    for i in str(x):
        if i in nechet:
            count += 1
    return count == 2

count = 0
for x in range(1000, 10000):
    n = int(str(x) + '34')
    if chet3(n) or nechet2(n):
        count += 1
print(count)

'''
5500
'''