my_len = [['БО-331101',['Пакулова Алена', 'Бабушкина Ксения']],['БОВ-421102',['Глад Валакас', 'Портуев Андрей']],['БО-331103',['Борисов Алексей', 'Алекс Борисов', 'Куртка Бейна)0']]]
for i in my_len:
    for el in i[1]:
        surname, name = el.split()
        if surname.startswith('П') and name.startswith('А'):
            print(i[0] + ': ' + el)