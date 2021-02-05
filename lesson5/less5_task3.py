# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as text:
    list_text = [line.split() for line in text]
    less_20 = [el[0] for el in list_text if float(el[1]) < 20000]
    print("Оклад менее 20 тыс.:", *less_20, sep='\n', end='\n\n')

    salary = [float(el[1]) for el in list_text]
    print(f'Средняя величина дохода сотрудников: {sum(salary) / len(salary)}')
