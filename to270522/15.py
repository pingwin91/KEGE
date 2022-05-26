def f(x, a1, a2):
    return (54 <= x <= 150) <= (((not (12 <= x <= 93)) and (not (a1 <= x <= a2))) <= (not(54 <= x <= 150)))

z = []
for a1 in range(150):
    for a2 in range(150):
        for x in range(150):
            if f(x, a1, a2) == 0:
                break
        else:
            z.append(a2 - a1)

print(min(z))

#  55