symbols = 'АБВГДЕ'
count = 0
for _1 in symbols:
    for _2 in symbols:
        for _3 in symbols:
            for _4 in symbols:
                word = _1 + _2 + _3 + _4 + 'Е'
                for i in range(2, 5):
                    if word[i] == word[i - 2] or 'А' not in word:
                        break
                else:
                    count += 1
print(count)

'''
430
'''