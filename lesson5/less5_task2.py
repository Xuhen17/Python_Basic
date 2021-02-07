# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_2.txt', 'r', encoding='utf-8') as text_f:
    text = text_f.readlines()
    print(f'Количество строк в файле: {len(text)}\n')

    for i in range(len(text)):
        list_i = text[i].split()
        print(f'Количество слов в {i + 1} строке: {len(list_i) - list_i.count("-")}')
