chars = 'КОМ'

count = 0
for _1 in chars:
    for _2 in chars:
        for _3 in chars:
            for _4 in chars[1:]:
                for _5 in chars[1:]:
                    for _6 in chars[1:]:
                        word = _1 + _2 + _3 + _4 + _5 + _6
                        if word.count('К') < 3:
                            count += 1
print(count)

'''
208
'''