from math import sqrt, ceil


ans = set()
for i in range(450_001, 500_000):
    for j in range(i - 1, 0, -1):
        if i % j == 0:
            for k in range(2, ceil(sqrt(j))):
                if j % k == 0:
                    ans.add((i, j))
            break
    if len(ans) > 5:
        break
print(sorted(ans))

#  (450002, 225001), (450004, 225002), (450006, 225003), (450007, 26471), (450008, 225004), (450009, 150003)