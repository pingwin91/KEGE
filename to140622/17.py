f = open('17.txt')
numbers_filter = sorted([int(i) for i in f if (int(i) % 2 == 0) and (int(i) % 3 != 0)], reverse=True)
print(len(numbers_filter), numbers_filter[1])
