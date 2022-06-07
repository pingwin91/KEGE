with open('24.txt') as f:
    string = f.readline()
count_withA = 0
count_withoutA = 0
for i in range(len(string) - 2):
    triple = set(string[i:i + 3])
    if len(triple) == 3:
        if 'a' in triple:
            count_withA += 1
        else:
            count_withoutA += 1

print(abs(count_withA - count_withoutA))