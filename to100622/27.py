###  файл А
f = open('27_A.txt')
n, d = map(int, f.readline().split())
results = {}
for i in f:
    id, *tr = map(int, i.split())
    if id in results:
        results[id].append(max(tr))
    else:
        results[id] = [max(tr)]
mid_max = 0
mid_min = 10000
for id, value in results.items():
    length = len(value)
    if length > d:
        mid_max = max(mid_max, sum(value) / length)
        mid_min = min(mid_min, sum(value) / length)
print(round(mid_max - mid_min, 2), end='\t')


###  файл В
f = open('27_B.txt')
n, d = map(int, f.readline().split())
results = {}
for i in f:
    id, *tr = map(int, i.split())
    if id in results:
        results[id].append(max(tr))
    else:
        results[id] = [max(tr)]
mid_max = 0
mid_min = 10000
for id, value in results.items():
    length = len(value)
    if length > d:
        mid_max = max(mid_max, sum(value) / length)
        mid_min = min(mid_min, sum(value) / length)
print(round(mid_max - mid_min, 2))

'''
3.35	4.96
'''