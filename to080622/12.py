string = '>' + '2' * 10 + '4' * 11 + '7' * 12

while '>2' in string or '>4' in string or '>7' in string:
    if '>2' in string:
        string = string.replace('>2', '72>')
    if '>4' in string:
        string = string.replace('>4', '4>22')
    if '>7' in string:
        string = string.replace('>7', '24>2')

print(4 * string.count('4') + 2 * string.count('2') + 7 * string.count('7'))

'''
512
'''