with open('24.txt') as f:
    string = f.readline().split('AD')

count = {'A': 0,
         'B': 0,
         'C': 0,
         'D': 0}

for i in range(len(string) - 1):
    if len(string[i]) == 0:
        count['D'] += 1
    else:
        count[string[i][-1]] += 1

print(max(count) + str(count[max(count)]))


#  D1582