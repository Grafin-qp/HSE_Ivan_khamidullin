"""Напишите функцию для валидации ИНН (идентификационного номера налогоплательщика), которая принимает в качестве
аргумента строку, содержащую ИНН или просто набор цифр, похожий на ИНН.
"""
your_number = str(input(f'Введите инн:\n').strip())


def num_check_10():
    global your_number
    coef = (2, 4, 10, 3, 5, 9, 4, 6, 8)
    summ = 0
    for index, i in enumerate(coef):
        summ += (int(i) * int(your_number[index]))
    contr_number = summ % 11
    if contr_number > 9:
        contr_number %= 10
        if contr_number == int(your_number[9]):
            return True
        else:
            return False
    else:
        if contr_number == int(your_number[9]):
            return True
        else:
            return False


def num_check_12():
    global your_number
    coef = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    summ = 0
    for index, i in enumerate(coef):
        summ += (int(i) * int(your_number[index]))
    contr_num_1 = summ % 11
    if contr_num_1 > 9:
        contr_num_1 %= 10
    coef = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    summ = 0
    for index, i in enumerate(coef):
        summ += (int(i) * int(your_number[index]))
    contr_num_2 = summ % 11
    if contr_num_2 > 9:
        contr_num_2 %= 10
    if (contr_num_1 == int(your_number[10])) and (contr_num_2 == int(your_number[11])):
        return True
    else:
        return False


def inn_check():
    global your_number
    if len(your_number) == 10:
        print(num_check_10())
    elif len(your_number) == 12:
        print(num_check_12())
    else:
        print(False)
        return False


inn_check()
