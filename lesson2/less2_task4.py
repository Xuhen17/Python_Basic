# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input("Введите строку из нескольких слов, разделенных пробелами: ")
user_list = str.split(user_str)
print(user_list)
for i, el in enumerate(user_list, 1):
    print(i, el[0:10])