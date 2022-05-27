'''with open('24.txt') as f:
    string = f.readline().split('AD')
print(string)
count = {'A': 0,
         'B': 0,
         'C': 0,
         'D': 0}

for i in range(len(string) - 1):
    if len(string[i]) == 0:
        count['D'] += 1
    else:
        count[string[i][-1]] += 1

print(max(count) + str(count[max(count)]))'''


#  D1582


with open('24.txt') as f:
    string = f.readline()

count_A = 0
count_B = 0
count_C = 0
count_D = 0
for i in range(1, len(string) - 1):
    if string[i] == 'A' and string[i + 1] == 'D':
        if string[i - 1] == 'A':
            count_A += 1
        if string[i - 1] == 'B':
            count_B += 1
        if string[i - 1] == 'C':
            count_C += 1
        if string[i - 1] == 'D':
            count_D += 1

print(f'A: {count_A}')
print(f'B: {count_B}')
print(f'C: {count_C}')
print(f'D: {count_D}')