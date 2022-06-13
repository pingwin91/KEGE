f = open('26.txt')
value, n = map(int, f.readline().split())
sells = sorted(int(i) for i in f)
summa = 0
i = 0
while summa + sells[i] <= value:
    summa += sells[i]
    i += 1
print(i, sells[0])

'''
329 10
'''