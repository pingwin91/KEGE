def prost(x, y):
    for i in range(2, max(x, y) // 2 + 1):
        if x % i == 0 and y % i == 0:
            return False
    return True


for a in range(1000):
    for x in range(1, 1000):
        f = (prost(x, 360) <= prost(x, a)) and (prost(x, a) <= prost(x, 240))
        if f == 0:
            break
    else:
        print(a)
        break

'''
30
'''