# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod
from pprint import pprint


class OwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    dict_storage = {'принтеры': [], 'сканеры': [], 'ксероксы': []}

    @staticmethod
    def reception(technic, quantity, rack):
        technic[1].update(
            {'общее количество': quantity, 'место хранения на складе': rack, 'количество на складе': quantity,
             'передано в подразделения': []})
        if technic[0] == 'принтер':
            Storage.dict_storage['принтеры'].append(technic[1])
        elif technic[0] == 'сканер':
            Storage.dict_storage['сканеры'].append(technic[1])
        else:
            Storage.dict_storage['ксероксы'].append(technic[1])
        return Storage.dict_storage

    @staticmethod
    def transfer(technic, quantity, division):
        for key, value in Storage.dict_storage.items():
            for i in value:
                if technic[1]['параметры'] in i.values():
                    try:
                        if i['количество на складе'] < quantity:
                            raise OwnExc(f'На складе нет нужного количества {key[0:-1]}ов!')
                    except OwnExc as err:
                        print("\033[31m{}\033[0m".format(err))
                    else:
                        if i['количество на складе'] == quantity:
                            i['количество на складе'] = 0
                            i['место хранения на складе'] = ''
                            i['передано в подразделения'] = {division: quantity}
                        else:
                            i['количество на складе'] -= quantity
                            i['передано в подразделения'].append({division: quantity})

        return Storage.dict_storage


class OfficeEquipment(ABC):

    def __init__(self, brand, model, cost, form):
        self.brand = brand
        self.model = model
        self.form = form
        self.cost = cost

    @abstractmethod
    def description(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, brand, model, cost, form, print_tech, colors):
        super().__init__(brand, model, cost, form)
        self.print_tech = print_tech
        self.colors = colors

    @property
    def description(self):
        return ['принтер', {'параметры': [self.brand, self.model, self.form, self.print_tech, self.colors],
                            'цена': self.cost}]

    def __str__(self):
        return f"Принтер {self.brand} модель {self.model} {self.form}, {self.print_tech}, {self.colors}, " \
               f"цена: {self.cost} руб."


class Scanner(OfficeEquipment):

    def __init__(self, brand, model, cost, form, dpi):
        super().__init__(brand, model, cost, form)
        self.dpi = dpi

    @property
    def description(self):
        return ['сканер', {'параметры': [self.brand, self.model, self.form, self.dpi], 'цена': self.cost}]

    def __str__(self):
        return f'Сканер {self.brand} модель {self.model} {self.form}, {self.dpi} dpi, цена: {self.cost} руб.'


class Xerox(OfficeEquipment):

    def __init__(self, brand, model, cost, form, colors):
        super().__init__(brand, model, cost, form)
        self.colors = colors

    @property
    def description(self):
        return ['ксерокс', {'параметры': [self.brand, self.model, self.form, self.colors], 'цена': self.cost}]

    def __str__(self):
        return f'Ксерокс {self.brand} модель {self.model} {self.form}, {self.colors}, цена: {self.cost} руб.'


sr = Storage()
p1 = Printer('RICOH', 'SP 6430DN', 128490, 'A3', 'лазерный', 'черно-белый')
p2 = Printer('EPSON', 'L805', 24000, 'A4', 'струйный', 'цветной')
s1 = Scanner('Canon', 'Canoscan LIDE300', 5150, 'A4', '2400x2400')
s2 = Scanner('EPSON', 'WorkForce DS-70', 16500, 'A4', '600x600')
x1 = Xerox('Canon', 'imageRUNNER C3025i', 31000, 'A3', 'цветной')
x2 = Xerox('XEROX', '3025', 12490, 'A4', 'черно-белый')

print(p1)
print(p2)
print(s1)
print(s2)
print(x1)
print(x2)

sr.reception(p1.description, 2, 1)
sr.reception(p2.description, 3, 1)
sr.transfer(p2.description, 1, 'отдел снабжения')
sr.reception(s1.description, 1, 2)
sr.reception(s2.description, 1, 3)
sr.transfer(s2.description, 1, 'отдел рекламы')
sr.reception(x1.description, 2, 7)
sr.reception(x2.description, 1, 6)
sr.transfer(x2.description, 2, 'бухгалтерия')
pprint(sr.dict_storage, width=160, sort_dicts=False)
