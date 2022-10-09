# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

# text = 'авб абв бав абв вба бав вба абв абв абв авб бав вба бав вба'

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = input("Введите текст: ")
my_text = del_words(text)
print(my_text)


