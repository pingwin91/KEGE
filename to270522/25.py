from math import sqrt, ceil
k = 0
first = 100_000_000
for i in range(50_000_000, 60_000_001):
    count = 0
    if i % 911 == 0:
        for j in range(2, ceil(sqrt(i))):
            if i % j == 0:
                count += 2
            if count > 6:
                break
        if count == 6:
            first = min(first, i)
            k += 1

print(k, first)


#  2489 50_002_057