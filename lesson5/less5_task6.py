# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

with open('text_6.txt', 'r', encoding='utf-8') as text:
    list_text = [line.split() for line in text]
    keys = []
    values = []

    for el in list_text:
        value = []
        for i in range(len(el)):
            if i == 0:
                keys.append(el[i].replace(":", ""))
            else:
                if el[i] == "-":
                    value.append(0)
                else:
                    value.append(int(''.join(symbol for symbol in el[i] if symbol.isdigit())))
        values.append(value)
    my_dict = {keys[i]: sum(values[i]) for i in range(len(keys))}
    print(my_dict)
