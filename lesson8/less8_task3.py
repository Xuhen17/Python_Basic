# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.#
# Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный список выводится на экран.

class OwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
el = 0
while el != 'stop':
    el = input("Введите элемент списка (выход - 'stop'): ")
    if el == 'stop':
        break
    else:
        try:
            if el.isdigit() or (el[1:].isdigit() and el[0] == '-'):
                user_list.append(int(el))
            elif el.count('.', 1, -1) == 1 and el[1:].replace('.', '').isdigit() and (
                    el[0] == '-' or el[0].isdigit()) and el[-1].isdigit():
                user_list.append(float(el))
            else:
                raise OwnExc("Введено не число.")
        except OwnExc as err:
            print(err)
print(user_list)
