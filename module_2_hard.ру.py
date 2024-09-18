def pairs_of_numbers(rand_number):
    pairs_numb = list()
    limit_first_numb = (rand_number + 1) // 2
    for i in range(1, limit_first_numb):
        j = i + 1
        while i + j <= rand_number:
            if rand_number % (i + j) == 0:
                tuple_numbers = (i, j)
                pairs_numb.append(tuple_numbers)
            j += 1
    return pairs_numb


fl = True
while fl:
    first_number = int(input('Введите число из первого поля: '))
    if first_number in range(3, 21):
        fl = False
    else:
        print('Введено число за пределами интервала [3, 20]')
        print('Повторите ввод')
print('Для числа', first_number, 'подходят пароли:', pairs_of_numbers(first_number))