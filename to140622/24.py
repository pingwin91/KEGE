f = open('24.txt')
string = f.readline()
i = 0
max_len = 0
while i < len(string) - 1:
    acces_str = string[i]
    while string[i] == string[i + 1] and i < len(string) - 1:
        acces_str += string[i + 1]
        i += 1
    max_len = max(max_len, len(acces_str))
    i += 1

print(max_len)

'''
19
'''