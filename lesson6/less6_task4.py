# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} {self.color} цвета поехала.', end=" ") if self.is_police is False else print(
            f'Полицейская машина {self.name} поехала.', end=" ")

    def stop(self):
        print(f'{self.name} остановилась.\n')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.', end=" ")

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed} км/ч.', end=" ")


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч и превысила допустимую скорость!',
              end=" ") if self.speed > 60 else Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч и превысила допустимую скорость!',
              end=" ") if self.speed > 40 else Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


auto_1 = TownCar(75, "белого", "Mazda")
print(
    f'auto_1:\nspeed: {auto_1.speed}, color: {auto_1.color}, name: {auto_1.name}, is_police: {auto_1.is_police}')
auto_1.go(), auto_1.turn(random.choice(['налево', 'направо'])), auto_1.show_speed(), auto_1.stop()

auto_2 = SportCar(300, "красного", "Maserati")
print(
    f'auto_2:\nspeed: {auto_2.speed}, color: {auto_2.color}, name: {auto_2.name}, is_police: {auto_2.is_police}')
auto_2.go(), auto_2.turn(random.choice(['налево', 'направо'])), auto_2.show_speed(), auto_2.stop()

auto_3 = WorkCar(40, "жёлтого", "ГАЗель")
print(
    f'auto_3:\nspeed: {auto_3.speed}, color: {auto_3.color}, name: {auto_3.name}, is_police: {auto_3.is_police}')
auto_3.go(), auto_3.turn(random.choice(['налево', 'направо'])), auto_3.show_speed(), auto_3.stop()

auto_4 = PoliceCar(100, "синего", "Lada")
print(
    f'auto_4:\nspeed: {auto_4.speed}, color: {auto_4.color}, name: {auto_4.name}, is_police: {auto_4.is_police}')
auto_4.go(), auto_4.turn(random.choice(['налево', 'направо'])), auto_4.show_speed(), auto_4.stop()
