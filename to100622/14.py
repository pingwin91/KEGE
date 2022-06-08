x = 9 ** 1700+ 3 ** 1300 - 3 ** 350 + 2
new_x = ''
while x > 0:
    new_x += str(x % 3)
    x //= 3
print(new_x.count('2'))

'''
951
'''