# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print("текущий рейтинг:", my_list)
while True:
    number = int(input("Введите новый элемент рейтинга (натуральное число): "))
    if number <= 0:
        print("Число должно быть больше нуля, введите новый вариант.")
    else:
        if number in my_list:
            i = my_list.index(number) + my_list.count(number)
            my_list.insert(i, number)
        else:
            i = 0
            for el in my_list:
                if number < el:
                    i = my_list.index(el) + 1
            my_list.insert(i, number)
        print("Обновлённый рейтинг", my_list)
        break
