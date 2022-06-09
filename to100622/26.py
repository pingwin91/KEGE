f = open('26.txt')
n, m = map(int, f.readline().split())
checks = [int(i) for i in f]
checks.sort(reverse=True)
s1 = sum(checks[:m])
checks_with_out = sorted(list(set(checks[:m])))
s2 = s1
for i in checks_with_out:
    if (s2 - i) / s1 < 0.9:
        break
    else:
        s2 -= i
print(s1, s2)

'''
252136 228184
'''