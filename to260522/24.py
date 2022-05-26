# через split()
'''string = open('24.txt').readline().split('D')
print(string)
max_len = 0
for i in range(len(string) - 1):
    max_len = max(max_len, len(string[i]) + len(string[i + 1]) + 1)

print(max_len)'''


#через перебор строки (долго, т.к. перебирает )
f = open('24.txt')
string = f.readline()
max_len = 0

for i in range(len(string)):
    count_D = 0
    len_D = 0
    while count_D < 2 and i < len(string):
        if string[i] != 'D':
            len_D += 1
            i += 1
            max_len = max(max_len, len_D)
        else:
            count_D += 1
            len_D += 1
            i += 1
print(max_len)