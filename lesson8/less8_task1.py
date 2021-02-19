# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def numbers(cls, data_list):
        data = [int(i) for i in data_list.split('-')]
        return cls(data)

    @staticmethod
    def check_num(obj):
        d, m, y = obj.data[0], obj.data[1], obj.data[2]
        if y < 1 or y > 9999:
            print("Дата некорректна")
        elif m > 12 or m < 1:
            print("Дата некорректна")
        elif d < 1:
            print("Дата некорректна")
        elif m == 2:
            if y % 4 == 0:
                print("Дата некорректна") if d > 29 else print("Дата корректна")
            else:
                print("Дата некорректна") if d > 28 else print('Дата корректна')
        elif m in [4, 6, 9, 11]:
            print("Дата некорректна") if d > 30 else print('Дата корректна')
        elif d > 31:
            print("Дата некорректна")
        else:
            print('Дата корректна')


d1 = Data.numbers("14-02-2021")
print(d1.data)
Data.check_num(d1)
