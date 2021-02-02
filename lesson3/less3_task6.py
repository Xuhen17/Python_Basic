# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(text):
    text_copy = text
    for i in range(len(text_copy)):
        if ord(text_copy[i]) >= ord("z") or ord(text_copy[i]) <= ord("a"):
            text = ""
    return text.title()


print(int_func(input("Введите слово из строчных латинских букв ")))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

sentence = "nice авп ъghj jапро hjjпаро вапрghgh cool"
result = []
words = sentence.split()
for ind in range(len(words)):
    word = int_func(words[ind])
    if word != "":
        result.append(word)
result = " ".join(result)
print(result)
