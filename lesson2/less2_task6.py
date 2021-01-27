# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

keys = ["название", "цена", "количество", "ед."]
while True:
    num = int(input("Введите количество товаров в матрице: "))
    if num < 1:
        print("Необходимо ввести хотя минимум 1 товар, повторите ввод данных.")
    else:
        user_list = []

        for i in range(num):
            product = input(f"Введите название товара №{i + 1} ")
            price = int(input(f"Введите цену товара №{i + 1} "))
            quantity = int(input(f"Введите количество товара №{i + 1} "))
            unit = input(f"Введите ед. изм. товара №{i + 1} ")

            values = [product, price, quantity, unit]
            prod_dict = dict(zip(keys, values))
            user_list.append(prod_dict)

        summary = []

        for i, el in enumerate(user_list, 1):
            tuple_prod = (i, el)
            summary.append(tuple_prod)

        print(f'Товары:\n {summary}')
        print('Товары:', *summary, sep="\n")

        # Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
        # например название, а значение — список значений-характеристик, например список названий товаров.

        analytics = {}
        ind = 0

        while ind < len(keys):
            values = []
            for i in range(num):
                dict_item = summary[i][1]
                value = dict_item.get(keys[ind])
                values.append(value) if value not in values else None
            analytics[keys[ind]] = list(values)
            ind += 1

        print(f'Аналитика:\n {analytics}')
        break
