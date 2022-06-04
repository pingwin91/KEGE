### тут суперкраткий вариант
f = open('24.txt')
words = f.readline().split()
print(len(max(words, key=len)))


### тут обычный вариант с перебором всех слов
f = open('24.txt')
words = f.readline()

cur_len = 0
max_len = 0
for i in words:
    if i != ' ':
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0

print(max_len)

'''
298 (с ответом не сходится, но оба варианта дают один ответ)
'''