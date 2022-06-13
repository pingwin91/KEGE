count = 0
for x in range(1000):
    n = 10
    while x < 500:
        x += n
        n += 6
    if n == 40:
        count += 1
print(count)

'''
34
'''