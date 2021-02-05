# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

with open('text_7.txt', 'r', encoding='utf-8') as text:
    total_profit = 0
    count_firm = 0
    firm_dict = {}
    average_profit = {}
    for line in text:
        new_line = line.rstrip().split()
        profit = int(new_line[2]) - int(new_line[3])
        firm_dict[new_line[0]] = profit
        if profit > 0:
            total_profit += profit
            count_firm += 1
    average_profit['average_profit'] = total_profit / count_firm
    total_list = [firm_dict, average_profit]
print(f'Итоговый список: {total_list}')

with open('text_7js.json', 'w', encoding='utf-8') as text_json:
    json.dump(total_list, text_json, indent=4, ensure_ascii=False)
