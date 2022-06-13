string = '1' * 80
while '2121' in string or '111' in string:
    if '2121' in string:
        string = string.replace('2121', '2', 1)
    else:
        string = string.replace('111', '12', 1)
print(string)

'''
121
'''