#shitcode_mode = shit(True)
my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
str_info = ''

words = my_string.replace('_', '').split(';')

for x in words:
    #Ищет ФИО
    if len(x) == 1 and x.isupper():
        str_info+= x + '             '

str_info+= 'О студенте'
print(str_info)
swap1 = ''
swap2 = ''

for word in words:
    if words[5] == word or words[6] == word or words[7] == word:
        print(word, ' '*8, end = '')
    if words[8] == word:
        swap1 = word
    if words[9] == word:
        swap2 = word
        swap1, swap2 = swap2, swap1
        print(swap1, ' ', swap2)
    if words[10] == word or words[11] == word or words[12] == word:
        print(word, ' '*8, end = '')
    if words[13] == word:
        swap1 = word
    if words[14] == word:
        swap2 = word
        swap1, swap2 = swap2, swap1
        print(swap1, ' ', swap2)