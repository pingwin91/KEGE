f = open('17.txt')
count = 0
min_have6 = 1_000_000

for i in f:
    if '6' in i:
        count += 1
        min_have6 = min(min_have6, int(i))

print(count, min_have6)

'''
935 -496
'''