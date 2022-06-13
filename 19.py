for _1 in range(10, 100):
    for _2 in range(10, 100):
        for _3 in range(10, 100):
            string = '0' + _1 * '1' + _2 * '2' + _3 * '3' + '0'
            while '00' not in string:
                string = string.replace('01', '21022', 1)
                string = string.replace('02', '310', 1)
                string = string.replace('03', '230112', 1)

            if (string.count('1') == 520 and
                    string.count('2') == 195 and
                    string.count('3') == 415):
                print(f'1:{_1}  2:{_2}  3:{_3} = {_1 + _2 + _3 + 2}')
                break