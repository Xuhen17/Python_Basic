# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("text_1.txt", 'w', encoding='utf-8') as text:
    while True:
        new_line = (input('введите данные: '))
        if new_line != "":
            text.write(f'{new_line}\n')
        else:
            break
