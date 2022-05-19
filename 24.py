with open('24.txt') as f:
    string = f.readline()

i = 0
max_count = 0
while i < len(string) - 1:
    count = 0
    while string[i] != 'A' and string[i + 1] == 'A':
        count += 1
        max_count = max(max_count, count)
        i += 2
    i += 1
print(max_count)