string = '>' + 15 * '1' + 16 * '4' + 20 * '6'
while '>1' in string or '>4' in string or '>6' in string:
    if '>1' in string:
        string = string.replace('>1', '4161>')
    if '>4' in string:
        string = string.replace('>4', '1611>')
    if '>6' in string:
        string = string.replace('>6', '414>')
summ = 0
for i in string:
    if i != '>':
        summ += int(i)
print(summ)


'''
767
'''