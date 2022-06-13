chars = 'ЕДОНК'
count = 0
for _1 in chars:
    for _2 in chars:
        for _3 in chars:
            for _4 in chars:
                word = _1 + _2 + _3 + _4
                if word.count('О') == 2:
                    count += 1

print(count)

'''
96
'''