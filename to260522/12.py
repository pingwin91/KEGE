string = '1' + '0' * 80

while '10' in string or '1' in string:
    if '10' in string:
        string = string.replace('10', '001', 1)
    else:
        if '1' in string:
            string = string.replace('1', '000', 1)

print(string.count('0'))