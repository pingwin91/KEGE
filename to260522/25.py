from math import ceil, sqrt


for i in range(201455, 201471):
    delit = [1, i]
    for j in range(2, ceil(sqrt(i))):
        if i % j == 0:
            delit.append(j)
            delit.append(i // j)
        if len(delit) > 4:
            break
    if len(delit) == 4:
        print(*sorted(delit))