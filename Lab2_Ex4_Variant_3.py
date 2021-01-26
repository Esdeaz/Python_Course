string_1 = input("Введите сообщение, используя кириллицу: ")
string_2 = ''

for i in string_1:
    if i == 'л' or i == 'Л':
        string_2+= i

print(string_2)