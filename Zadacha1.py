# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = input("Введите текст: ")
my_text = del_words(text)
print(my_text)


