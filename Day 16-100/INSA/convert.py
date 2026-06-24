def geez_to_arabic(geez):
    values = {
        '፩': 1, '፪': 2, '፫': 3, '፬': 4, '፭': 5,
        '፮': 6, '፯': 7, '፰': 8, '፱': 9,
        '፲': 10, '፳': 20, '፴': 30, '፵': 40,
        '፶': 50, '፷': 60, '፸': 70, '፹': 80,
        '፺': 90
    }

    total = 0
    group = 0

    for ch in geez:
        if ch in values:
            group += values[ch]

        elif ch == '፻':
            if group == 0:
                group = 1

            total += group * 100
            group = 0

        elif ch == '፼':
            if group == 0:
                group = 1

            total += group * 10000
            group = 0

    return total + group
print(geez_to_arabic("፲፫"))
print(geez_to_arabic("፪፯"))
print(geez_to_arabic("፳፭"))
print(geez_to_arabic("፻፳፭"))
print(geez_to_arabic("፪፻፶"))
print(geez_to_arabic("፲፪፼፫፻፵፭"))