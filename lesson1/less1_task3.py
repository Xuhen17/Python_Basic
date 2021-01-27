# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

n = input('Введите любое целое положительное число ')
i = 1
result = 0
while i <= 3:
    result += int(n * i)
    i += 1
print(result)
