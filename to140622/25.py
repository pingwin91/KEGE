from math import sqrt, ceil

for x in range(64930, 65051):
    delit = []
    for i in range(2, ceil(sqrt(x))):
        _1 = i
        _2 = x // i
        if x % i == 0 and i % 6 == 0:
            delit.append(i)
        if x % (x // i) == 0 and x // i % 6 == 0:
            delit.append(x // i)
        if len(delit) > 3:
            break
    if sqrt(x) - ceil(sqrt(x)) == 0:
        delit.append(ceil(sqrt(x)))
    if len(delit) == 3:
        print(x, *sorted(delit), sep='\t')

'''
64938	6	474	822
64956	6	12	32478
65004	6	12	32502
65028	6	12	32514
65034	6	18	21678
65046	6	222	1758
'''