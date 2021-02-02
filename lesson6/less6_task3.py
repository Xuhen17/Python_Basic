# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}


class Position(Worker):
    def __init__(self, n, s, w, b):
        self.name = n
        self.surname = s
        self._income = {"wage": w, "bonus": b}

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f'Доход с учётом премии: {total_income}\n')


human_1 = Position("Иван", "Иванов", 50000, 7000)
print(human_1)
print(f'name: {human_1.name}')
print(f'surname: {human_1.surname}')
print(f'income:{human_1._income}\n')
human_1.get_full_name()
human_1.get_total_income()

human_2 = Position("Пётр", "Петров", 45000, 5000)
print(human_1)
print(f'name: {human_2.name}')
print(f'surname: {human_2.surname}')
print(f'income:{human_2._income}\n')
human_2.get_full_name()
human_2.get_total_income()
