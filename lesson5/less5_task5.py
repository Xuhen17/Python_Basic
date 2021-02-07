# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("text_5.txt", 'w+', encoding='utf-8') as text:
    for i in range(5):
        print(randint(1, 10), end=' ', file=text)

    text.seek(0)
    num_str = text.read()
    print(f'Числа: {num_str}')
    num_int = [int(el) for el in num_str.split()]
    print(f'Сумма чисел: {sum(num_int)}')
