# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "".join(["".join([f'{el[i]}\t' if i < len(el) - 1 else f'{el[i]}\n' for i in range(len(el))]) for el in
                        self.matrix])

    def __add__(self, other):
        while len(self.matrix) != len(other.matrix):
            self.matrix.append([]) if len(self.matrix) < len(other.matrix) else other.matrix.append([])
        for i in range(len(self.matrix)):
            while len(self.matrix[i]) < len(other.matrix[i]):
                self.matrix[i].append(0)
        for i in range(len(self.matrix)):
            for i_ in range(len(other.matrix[i])):
                self.matrix[i][i_] += other.matrix[i][i_]
        return Matrix(self.matrix)


m1 = Matrix([[4, 3], [2, 1], [5, 5]])
m2 = Matrix([[1, 2], [3, 4]])
m3 = Matrix([[4, 3, 10], [2, 1, 10], [5, 5, 10], [10, 10, 10]])

print(m1)
print(m2)
print(m3)
print(m1 + m2)
print(m1 + m2 + m3)
