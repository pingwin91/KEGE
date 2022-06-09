from math import sqrt, ceil

for x in range(3954, 8980):
    count_del = 2
    for i in range(2, ceil(sqrt(x))):
        if x % i == 0:
            count_del += 2
    if sqrt(x) - ceil(sqrt(x)) == 0:
        count_del += 1
    if 41 <= count_del <= 45:
        print(f'{x}\t{count_del}')

'''
4032	42
4800	42
6336	42
7056	45
7488	42
8100	45
'''
