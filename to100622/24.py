f = open('24.txt')
string = f.readline()
length = len(string)
i = 0
max_len = 0
strings = []
while i < len(string):
    if string[i] == string[i + 1]:
        start_index = i
        while string[i] == string[start_index]:
            i += 1
        end_index = i - 1
        if string[start_index - 1] == string[end_index + 1]:
            max_len = max(max_len, end_index - start_index + 1)
    i += 1
print(max_len)