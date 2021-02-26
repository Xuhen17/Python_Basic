# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    divisible = float(input("Введите делимое: "))
    divisor = float(input("Введите делитель: "))
    if divisor == 0:
        raise OwnExc("Ошибка! На ноль делить нельзя.")
except ValueError:
    print("Введено не число")
except OwnExc as err:
    print(err)
else:
    print(f"Частное от деления равно: {divisible / divisor}")
