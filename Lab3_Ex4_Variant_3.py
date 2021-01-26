import re

my_string = """Пусть дана строка произвольной длины. Выведите информацию о том,
сколько в ней символов и сколько слов."""
words = len(re.split(r'\s+', re.sub(r'[;.,\-!?]', ' ', my_string).strip()))

print('количество слов: ',words)
print('Длина строки: ',len(my_string))