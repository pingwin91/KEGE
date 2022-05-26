count = 0
for x in range(350):
    n = bin(x)[2:]
    if x % 2 == 0:
        n += '00'
    else:
        n += '10'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    n = int(n, 2)
    if 130 <= n <= 350:
        count += 1

print(count)

#  27