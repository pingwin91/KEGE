for i in range(10):
    for j in range(10):
        n = int('1234' + str(i) + '57' + str(j))
        if n % 17 == 0:
            print(n, n // 17)