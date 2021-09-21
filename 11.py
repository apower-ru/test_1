run = True
while run:
    number = input('Введите число в двоичном коде: ')
    digit = len(number)
    result = 0
    for rank in number:
        digit -= 1
        if int(rank) == 1:
            a = 2 ** digit
            result += a
    print('Результат в десятичном виде: ', result)
