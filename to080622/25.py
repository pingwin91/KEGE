from math import ceil

for x in range(105000, 135201):
    for i in range(2, ceil(x ** (1 / 3)) + 1):
        j = 3
        while i ** j < x:
            j += 1
        if i ** j == x:
            print(f'{x}\t{i}\t{j}')


'''
110592	48	3
117649	7	6
117649	49	3
125000	50	3
130321	19	4
131072	2	17
132651	51	3
'''