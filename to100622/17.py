f = open('17.txt')
count = 0
max_num = 0
for i in f:
    if int(i) % 4 == 0:
        if int(i) % 5 != 0 and int(i) % 8 != 0 and int(i) % 31 != 0 and int(i) % 41 != 0:
            count += 1
            max_num = max(max_num, int(i))

print(max_num, count)


'''
9572 381
'''