import json
import csv
import re


def first_task():
    with open('traders.txt', 'r') as source:
        inn_list = source.readlines()
        inn_list = [inn.strip() for inn in inn_list]

    with open('traders.json', 'r') as source:
        data = json.load(source)
        data = {dct['inn']: dct for dct in data}

    # Создать множество из значений ИНН из inn_list
    innens_set = set(inn_list)

    # Перебрать значения ИНН в data и проверить, есть ли они в множестве
    with open('traders.csv', 'w') as source:
        writer = csv.writer(source)
        writer.writerow(['inn', 'ogrn', 'address'])
        for inn in data:
            if inn in innens_set:
                dct = data[inn]
                row = [dct['inn'], dct['ogrn'], dct['address']]
                writer.writerow(row)


first_task()
with open('traders.csv', 'r') as f:
    print(f.read())


def second_task():
    email = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')

    with open('1000_efrsb_messages.json', 'r') as source:
        data = json.load(source)

    result = {}
    for i in data:
        inn = i.get('publisher_inn')
        text = i.get('msg_text')
        email_list = list(set(re.findall(email, text)))
        if email_list:
            result[inn] = email_list
    with open('emails.json', 'w') as source:
        json.dump(result, source, indent=2)


second_task()
with open("emails.json", "r") as f:
    print(f.read())
