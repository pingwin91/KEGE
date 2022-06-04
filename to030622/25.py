from math import sqrt, ceil


for x in range(153222, 153271):
    duo = []
    for i in range(1, ceil(sqrt(x)) - 1):
        if len(duo) > 1:
            break
        for j in range(i + 1, ceil(sqrt(x))):
            if x == (i ** 2 + j ** 2):
                duo.append((i, j))
                break
    if len(duo) == 1:
        print(*duo)

'''
(255, 297)
(52, 388)
(34, 390)
(90, 381)
(122, 372)
(263, 290)
'''

