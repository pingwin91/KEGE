with open('24.txt') as f:
    string = f.readline()
print(string)
count = 1
max_count = 0
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)


#  120