for x in range(50):
    for y in range(50):
        for z in range(50):
            string = '0' + '2' * x + '4' * y + '6' * z
            while '02' in string or '04' in string or '06' in string:
                if '02' in string:
                    string =string.replace('02', '6404', 1)
                if '04' in string:
                    string =string.replace('04', '2206', 1)
                if '06' in string:
                    string =string.replace('06', '440', 1)
            if string.count('2') == 30 and string.count('4') == 54 and string.count('6') == 10:
                print(string.count('6'))
                break

#  10