string = '7' * 112

while '111' in string or '7777' in string:
    if '111' in string:
        string = string.replace('111', '7', 1)
    else:
        string = string.replace('7777', '1', 1)

print(string)

'''
77
'''