import re

my_string = """ФИО;Возраст;Категория;_Иванов Иван Иванович;23года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов ЯрославНаумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_ПетровВсеволод Борисович;21 год;Студент 2 курса"""
k = 1
for i in my_string.split('_'):
    if re.search(r'\bгода\b', i):
        print(i)
        k+= 1