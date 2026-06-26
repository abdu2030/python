def arabic_to_geez(num):
    ones = {
        1: '፩', 2: '፪', 3: '፫', 4: '፬', 5: '፭',
        6: '፮', 7: '፯', 8: '፰', 9: '፱'
    }

    tens = {
        10: '፲', 20: '፳', 30: '፴', 40: '፵', 50: '፶',
        60: '፷', 70: '፸', 80: '፹', 90: '፺'
    }

    if num == 0:
        return "0"

    result = ""

    if num >= 10000:
        ten_thousands = num // 10000
        result += arabic_to_geez(ten_thousands) + "፼"
        num %= 10000

    if num >= 100:
        hundreds = num // 100
        if hundreds == 1:
            result += "፻"
        else:
            result += arabic_to_geez(hundreds) + "፻"
        num %= 100

    if num >= 10:
        t = (num // 10) * 10
        result += tens[t]
        num %= 10

    if num > 0:
        result += ones[num]

    return result