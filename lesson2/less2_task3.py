# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    month = int(input("Введите мемяц в виде целого числа от 1 до 12: "))

    if month <= 0 or month > 12:
        print("Число должно быть больше нуля и в пределах от 1 до 12")
    else:

        # вариант 1:
        monthes = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        seasons = ["зима", "весна", "лето", "осень"]
        for i in range(len(seasons)):
            if month in monthes[i]:
                print(f"это {seasons[i]}")

        # вариант 2:
        seasons_dict1 = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
        for key in seasons_dict1.keys():
            if month in seasons_dict1[key]:
                print("это", key)
    break
