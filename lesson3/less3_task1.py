# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return print("На ноль делить нельзя.")
    print(f'Частное от деления {num1} на {num2} равно {num1 / num2}.')


division(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
