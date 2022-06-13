def to7(x):
    _7 = ''
    while x > 0:
        _7 += str(x % 7)
        x //= 7
    return _7

x = 49 ** 1010 + 7 ** 1000 - 7 ** 250
print(to7(x).count('6'))

'''
750
'''