# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    """Возвращает сумму двух наибольших аргументов из трёх."""
    numbers = [num1, num2, num3]
    return sum(numbers) - min(numbers)


print(my_func(117, 8, 25))