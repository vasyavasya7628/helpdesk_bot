"""data = [
    (10, 26, 18346208, 'Калькулятор сломался, сижу с петуха в деревне', None, 'https://t.me/luciferthelight',
     'https://t.me/i0x3141', '01.02.2024, 10:09', None, None, 'в работе', 1623218378),
    (9, 26, 18628322, 'Мой кампуктер убил вирус, сижу с калькулятора!', None, 'https://t.me/luciferthelight', None,
     '01.02.2024, 10:06', None, None, 'ожидает реакции', None),
    (8, 26, 16928346, 'fwqfqwfwqfq', None, 'https://t.me/i0x3141', None, '01.02.2024, 10:05', None, None,
     'ожидает реакции', None),
    (7, 26, 11528395, 'АИС не работает', None, 'https://t.me/kostromina_nyu', None, '01.02.2024, 09:57', None, None,
     'ожидает реакции', None),
    (6, 26, 17233135, 'НЕ РАБОТАЕТ МОЗГ', None, 'https://t.me/luciferthelight', None, '01.02.2024, 09:53', None, None,
     'ожидает реакции', None),
    (5, 26, 19750465, 'Есть проблема', None, 'https://t.me/luciferthelight', None, '01.02.2024, 09:52', None, None,
     'ожидает реакции', None),
    (4, 26, 19299995, 'wkgvwegvewngvew', None, 'https://t.me/i0x3141', None, '01.02.2024, 09:51', None, None,
     'ожидает реакции', None),
    (3, 26, 17940288, 'fwqfqwfq\\[fk\\[wqfkwq', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:33', None, None,
     'ожидает реакции', None),
    (2, 26, 12460491, 'Список заявок', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:32', None, None,
     'ожидает реакции', None),
    (1, 26, 18963443, 'йцвцйвцйвцй', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:15', None, None,
     'ожидает реакции', None)
]


def generate_table_output(result):
    formatted_message = f"Список заявок:\n"
    for i in range(len(result)):
        message = ("______________________________\n"
                   f"Номер заявки: {result[i][2]} \n"
                   f"От кого: {result[i][5]}\n"
                   f"Исполнитель: {result[i][6]} \n")
        message += f"   - Сообщение: {result[i][3]}\n"
        message += f"   - Время: {result[i][7]}\n"
        message += f"   - Статус: {result[i][10]}\n"
        message += f"   КНОПКА КНОПКА \n"
        formatted_message += message
    return formatted_message


tuple_data = generate_table_output(data)
print(tuple_data)"""
"""
in_str = f"close|{824194214}|{12421412421}"
if in_str.startswith("close"):
    my_list = in_str.split("|")"""

response = [
    (10, 26, 18346208, 'Калькулятор сломался, сижу с петуха в деревне', None, 'https://t.me/luciferthelight',
     'https://t.me/i0x3141', '01.02.2024, 10:09', None, None, 'в работе', 1623218378),
    (9, 26, 18628322, 'Мой кампуктер убил вирус, сижу с калькулятора!', None, 'https://t.me/luciferthelight', None,
     '01.02.2024, 10:06', None, None, 'ожидает реакции', None),
    (8, 26, 16928346, 'fwqfqwfwqfq', None, 'https://t.me/i0x3141', None, '01.02.2024, 10:05', None, None,
     'ожидает реакции', None),
    (7, 26, 11528395, 'АИС не работает', None, 'https://t.me/kostromina_nyu', None, '01.02.2024, 09:57', None, None,
     'ожидает реакции', None),
    (6, 26, 17233135, 'НЕ РАБОТАЕТ МОЗГ', None, 'https://t.me/luciferthelight', None, '01.02.2024, 09:53', None, None,
     'ожидает реакции', None),
    (5, 26, 19750465, 'Есть проблема', None, 'https://t.me/luciferthelight', None, '01.02.2024, 09:52', None, None,
     'ожидает реакции', None),
    (4, 26, 19299995, 'wkgvwegvewngvew', None, 'https://t.me/i0x3141', None, '01.02.2024, 09:51', None, None,
     'ожидает реакции', None),
    (3, 26, 17940288, 'fwqfqwfq\\[fk\\[wqfkwq', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:33', None, None,
     'ожидает реакции', None),
    (2, 26, 12460491, 'Список заявок', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:32', None, None,
     'ожидает реакции', None),
    (1, 26, 18963443, 'йцвцйвцйвцй', None, 'https://t.me/i0x3141', None, '30.01.2024, 09:15', None, None,
     'ожидает реакции', None)
]
# сделать кнопку окно в формате DD
data = [(18346208, 1623218378),
        (18346208, 1623218378)]
data = list(data)
print(data)
