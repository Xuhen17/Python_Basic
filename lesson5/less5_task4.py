# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.txt', 'r', encoding='utf-8') as text:
    rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = ''
    for line in text:
        new_line = line.split(' ')
        for key in rus:
            if key == new_line[0]:
                new_line[0] = rus.get(key)
                new_text += ' '.join(new_line)
with open('text_4_rus.txt', 'w', encoding='utf-8') as text_n:
    text_n.write(new_text)
