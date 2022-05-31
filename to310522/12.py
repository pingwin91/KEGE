string = '1' + '2' * 70

while '12' in string or '1' in string:
    if '12' in string:
        string = string.replace('12', '221', 1)
    elif '1' in string:
        string = string.replace('1', '2', 1)

print(string.count('2'))


#  141