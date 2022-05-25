string = open('24.txt').readline().split('D')

max_len = 0
for i in range(len(string) - 1):
    max_len = max(max_len, len(string[i]) + len(string[i + 1]) + 1)

print(max_len)