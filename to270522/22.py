for x in range(479, 1, -1):
    l = x
    m = 132
    if l % 2 != 0:
        m = 64
    while l != m:
        if l > m:
            l -= m
        else:
            m -= l
    if m == 12:
        print(x)
        break

#  468