f = open('26.txt')
value, n = map(int, f.readline().split())
files = []
for i in f:
    files.append(int(i))
files.sort()

count_in = 0
count_out = 0
i = 0
summ = 0
for i in range(len(files)):
    summ += files[i]
    i += 1
    if summ > value:
        summ -= files[i] + files[i - 1]
        count_in = i - 1
        break


delta = value - summ
i = len(files) - 1
while files[i] > delta:
    count_out += 1
    i -= 1
print(count_in, count_out)

'''
509 188
'''