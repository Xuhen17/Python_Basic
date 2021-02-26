# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def comment(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.size = v

    def comment(self):
        return f"Расход ткани на {self.name}:"

    def consumption(self):
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.height = h

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height % 1 == 0:
            self.__height = height / 100
        else:
            self.__height = height

    def comment(self):
        return f"Расход ткани на {self.name}:"

    def consumption(self):
        return round((2 * self.height + 0.3), 2)


order = int(input("Ввведите количество вещей в заказе: "))
list_obj = []
total_consumption = 0

for i in range(order):
    while True:
        c = input('Выберете вид одежды (1 - пальто, 2 - костюм) ')
        if c == "1":
            list_obj.append(Coat(input('Введите название '), int(input('Введите размер '))))
            break
        elif c == "2":
            list_obj.append(Suit(input('Введите название '), float(input('Введите рост '))))
            break
        else:
            print("Ошибка ввода. Уточние Ваш выбор.")
    total_consumption += list_obj[i].consumption()
    print(f'\n{list_obj[i].comment()} {list_obj[i].consumption()} \n')

print(f'Общий расход ткани: {total_consumption}')
