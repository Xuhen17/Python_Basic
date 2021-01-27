# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Вариант 1:
seconds = int(input('Введите время в секундах: '))

if seconds / 3600 >= 1:
    hours = seconds // 3600
    seconds -= hours * 3600
    if seconds / 60 >= 1:
        minutes = seconds // 60
        seconds -= minutes * 60
    else:
        minutes = 0
else:
    hours = 0
    if seconds / 60 >= 1:
        minutes = seconds // 60
        seconds -= minutes * 60
    else:
        minutes = 0
print('%.2d' % hours, ':', '%.2d' % minutes, ':', '%.2d' % seconds)

# Вариант 2:
seconds = int(input('Введите время в секундах: '))

if seconds / 60 < 1:
    minutes = 0
    hours = 0
elif seconds / 3600 < 1:
    hours = 0
    minutes = seconds // 60
    seconds -= minutes * 60
else:
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
print('%.2d' % hours, ':', '%.2d' % minutes, ':', '%.2d' % seconds)
