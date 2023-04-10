from lesson_2_data import repondents, courts
# Задание 1
"""
Создайте ряд функций для проведения математических вычислений:

1. функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
Принимает в качестве аргумента число, возвращает его факториал;
"""


def factorial(n):
    start = 1
    result = 1
    while start <= n:
        result *= start
        start += 1
    print(f'Факториал числа {n} = {result}')


"""
2. поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из трёх 
чисел, возвращает наибольшее из них;
"""


def search_for_max(m):
    max_number = max(m)
    print(f'Самое большое число кортежа:{max_number}')


"""
3. расчёт площади прямоугольного треугольника. Принимает в качестве аргумента размер
двух катетов треугольника. Возвращает площадь треугольника.
"""


def triangle_area(leg_first, leg_second):
    area = (leg_first * leg_second) / 2
    print(f'Площадь вашего прямоуглоьного треугольника: {area}')


# Задание 2
"""Создайте функцию для генерации текста с адресом суда.

Функция должна по шаблону генерировать шапку для процессуальных документов с реквизитами сторон для отправки.
"""


def head_for_court(case_num):
    claimant = 'Ivan'
    inn_cl = '111111111111'
    sp_num_cl = '1313131313131131'
    add_cl = 'Kaluga, 13 b'
    for i in repondents:
        if 'case_number' in i:
            if case_num == i['case_number']:
                defendant = i['short_name']
                inn_def = i['inn']
                sp_num_def = i['ogrn']
                add_def = i['address']
    for i in courts:
        if case_num[0:3] == i['court_code']:
            court = i['court_name']
            court_address = i['court_address']
            header = f'''В {court}
Адрес: {court_address}

Истец: {claimant}
ИНН {inn_cl} ОГРНИП {sp_num_cl}
Адрес: {add_cl}
                        
Ответчик: {defendant}
ИНН {inn_def} ОГРН {sp_num_def}
Адрес: {add_def}
                        
Номер дела {case_num}'''
            print(header)
