# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = (input('Введите целое положительное число:'))
i = len(user_number)
max_number = 0
user_number = int(user_number)
while i > 0:
    number = user_number % 10
    user_number //= 10
    i -= 1
    if number >= user_number % 10 and number >= max_number:
        max_number = number
print('Максимальная цифра в числе: ', max_number)
