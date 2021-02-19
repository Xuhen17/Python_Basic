# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.a + other.a == 0:
            return f'Сумма: {self.b + other.b}j'
        elif self.b + other.b < 0:
            return f'Сумма: {self.a + other.a}{self.b + other.b}j'
        else:
            return f'Сумма: {self.a + other.a}+{self.b + other.b}j'

    def __mul__(self, other):
        if self.a * other.a - self.b * other.b == 0:
            return f'Произведение: {self.a * other.b + self.b * other.a}j'
        elif self.a * other.b + self.b * other.a < 0:
            return f'Произведение: {self.a * other.a - self.b * other.b}{self.a * other.b + self.b * other.a}j'
        else:
            return f'Произведение: {self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}j'

    def __str__(self):
        if self.a == 0:
            return f'{self.b}j'
        elif self.b < 0:
            return f'{self.a}{self.b}j'
        else:
            return f'{self.a}+{self.b}j'


num1 = Complex(-2, 6)
num2 = Complex(2, -3)
print(num1)
print(num2)
print(num1 + num2)
print(num1 * num2)
