import math, random, re, os, sys

def lab1ex1():
    def is_digit(string):
        if string.isdigit():
           return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False
    
    def dig_input():
        x = input("Введите число: ")
        if is_digit(x)!= True :
            print("Ошибка! Ведите число!")
            dig_input()
        else: 
            return float(x)
    def zero_checker(a, b, c):
        if a == c or (c < 0 and b == 0):
            print("Число С не должно равняться числу А или быть отрицательным. Пожалуйста, введите число С заново: ")
            c = dig_input()
            zero_checker(a, c)
        else:
            return c
        return c
    
    a = dig_input()
    b = dig_input()
    c = dig_input()
    
    zero_checker(a, b, c)
    
    result = math.fabs(1.0 - (a * b ** c) - a * (b ** 2 - c ** 2) + (b - c + a) * (12.0 + b) / (c - a))
    print("Результат вычисления:", result)
    continue_program()
def lab1ex2():
    list = ["s", 4, "adb", 10, -4, 6, 3, '']
    
    def is_digit(string):
        try:
            int(string)
            return True
        except ValueError:
            try:
                float(string)
                return True
            except ValueError:
                return False
    
    for x in list:
        if is_digit(x):
            if x % 2 == 0:
                print(x, ' ', end = '')
        else:
            continue
    continue_program()
def lab1ex3():
    list = [4, 10, -4, 6, 3, 5, 20]
    S = 1
    
    for x in list:
        if x < 10:
            S *= x
        else:
            continue
    print(S)
    continue_program()
def lab1ex4():
    list = [10, -5, 8, -2, 1, 64, 1000, 5]
    S = 0
    k = 0
    
    for x in list:
        S += x
        k += 1
    S = S / k
    print(S)
    continue_program()

def lab2ex1():
    my_number = random.randint(0, 100)
    print("Случайное число: ", my_number, '\t')
    user_number = int(input("Введите свое число: "))
    
    while user_number == my_number:
        user_number = int(input("Введите свое число: "))
        print("Ваше число: ", user_number)
    continue_program()
def lab2ex2():
    list = ['sdadar', 'sdfghj', 'RT', 'LOWDr', 'rtyuio']
    
    for i in list:
        for c in i:
            if c == 'r' or c == 'R':
                print(i)
                break
    continue_program()
def lab2ex3():
    l = [str(random.randint(0,9)) for i in range(5)]
    l.insert(random.randint(0,5), '3')
    continue_program()
    print(''.join(l))
def lab2ex4():
    string_1 = input("Введите сообщение, используя кириллицу: ")
    string_2 = ''
    
    for i in string_1:
        if i == 'л' or i == 'Л':
            string_2+= i
    
    print(string_2)
    continue_program()

def lab3ex1():
    string_in = input("Введите ваше сообщение: ")
    string_out = ''
    words = re.split(r'\s+', re.sub(r'[.,\-!?]', ' ', string_in).strip())
    
    for i in words:
        for c in i:
            if len(i) >=5 or len(i) <= 1:
                string_out+= i+' '
                break
    print(string_out)
    continue_program()
def lab3ex2():
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
    continue_program()
def lab3ex3():
    my_string = """ФИО;Возраст;Категория;_Иванов Иван Иванович;23года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов ЯрославНаумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_ПетровВсеволод Борисович;21 год;Студент 2 курса"""
    k = 1
    for i in my_string.split('_'):
        if re.search(r'\bгода\b', i):
            print(i)
            k+= 1
    continue_program()
def lab3ex4():
    my_string = """Пусть дана строка произвольной длины. Выведите информацию о том,
    сколько в ней символов и сколько слов."""
    words = len(re.split(r'\s+', re.sub(r'[;.,\-!?]', ' ', my_string).strip()))
    
    print('количество слов: ',words)
    print('Длина строки: ',len(my_string))
    continue_program()
    
def lab4ex1():
    n = int(input('Введите число N для размера квадратной матрицы: '))
    a_list = [[0] * n for i in range(n)] #создание матрицы
    s = 0
    
    for i in range(n): #заполнение матрицы случайными числами и их суммирование
        for j in range(n):
            a_list[i][j] = random.randint(0, 100)
            s += a_list[i][j]
        
    print(a_list)
    print("Сумма чисел в матрице: ", s)
    continue_program()
def lab4ex2():
    list_a = [random.randint(0, 100) for i in range(10)]
    print(list_a)
    
    k = len(list_a) - 2
    
    while k > 3 and k < len(list_a):
    #удаление элементов с 4 по 8 и добавление двух новых в конец
        list_a.pop(k)
        k -= 1
        if k == 5 or k == 4:
            list_a.append(random.randint(0, 100))
            
    print(list_a)
    continue_program()
def lab4ex3():
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102',['Глад Валакас', 'Belle Delphine']],['БО-331103',['Борисов Алексей', 'Алекс Борисов', 'Куртка Бейна)0']]]
    for i in my_len:
        print('' * 2, i[0])
        for el in i[1]:
            print(el)
    continue_program()
def lab4ex4():
    my_len = [['БО-331101',['Пакулова Алена', 'Бабушкина Ксения']],['БОВ-421102',['Глад Валакас', 'Портуев Андрей']],['БО-331103',['Борисов Алексей', 'Алекс Борисов', 'Куртка Бейна)0']]]
    for i in my_len:
        for el in i[1]:
            surname, name = el.split()
            if surname.startswith('П') and name.startswith('А'):
                print(i[0] + ': ' + el)
    continue_program()            
def lab5ex1():
    path = os.getcwd()#получение текущей директории
    #Подсчет файлов, которые находятся в текущей директории
    num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
    print(num_files)
    continue_program()
def lab5ex2():
    f = open('students.txt', 'r', encoding = "UTF-8")
    list_st = f.readlines()
    f.close()
    list_form = []
    
    for el in list_st:
        list_form.append(re.split(r'\s+', re.sub(r'[;.,\-!?]', ' ', el).strip()))
    
    for list_a in list_form:
        for el in list_a:
            if el.endswith('111'):
                print('БО-111111: ', end = '')
                for elem in list_a:
                    if elem != '111111' and not elem.endswith('О'):
                        print(elem, ' ', end = '')
            if el.endswith('222'):
                print('БО-222222: ', end = '')
                for elem in list_a:
                    if elem != '222222' and not elem.endswith('О'):
                        print(elem, ' ', end = '')
    continue_program()
def lab5ex3():
    age_param1 = int(input('Задайте параметр для группы БО-111111: '))
    age_param2 = int(input('Задайте параметр для группы БО-222222: '))
    
    
    f = open('students.txt', 'r+', encoding = "UTF-8")
    list_st = f.readlines()
    f.close()
    list_form = []
    
    for el in list_st:
        list_form.append(re.split(r'\s+', re.sub(r'[;.,\-!?]', ' ', el).strip()))
    
    for list_a in list_form:
        for el in list_a:
            if el.endswith('111'):
                print('БО-111111: ', end = '')
                for elem in list_a:
                    if elem != '111111' and not elem.endswith('О'):
                        if list_a.index(elem) == 4 or list_a.index(elem) == 9:
                            elem = str(int(elem) + age_param1)
                            print(elem, ' ', end = '')
                        else:
                            print(elem, ' ', end = '')
            if el.endswith('222'):
                print('БО-222222: ', end = '')
                for elem in list_a:
                    if elem != '222222' and not elem.endswith('О'):
                        if list_a.index(elem) == 4:
                            elem = str(int(elem) + age_param2)
                            print(elem, ' ', end = '')
                        else:
                            print(elem, ' ', end = '')
    continue_program()
    
    
def startlab():
    print("0 - Выход из программы\n", 
          "1 - lab1ex1\n",
          "2 - lab1ex2\n",
          "3 - lab1ex3\n",
          "4 - lab1ex4\n",
          "5 - lab2ex1\n",
          "6 - lab2ex2\n",
          "7 - lab2ex3\n",
          "8 - lab2ex4\n",
          "9 - lab3ex1\n",
          "10 - lab3ex2\n",
          "11 - lab3ex3\n",
          "12 - lab3ex4\n",
          "13 - lab4ex1\n",
          "14 - lab4ex2\n",
          "15 - lab4ex3\n",
          "16 - lab4ex4\n",
          "17 - lab5ex1\n",
          "18 - lab5ex2\n",
          "19 - lab5ex3\n")
    arg = int(input('Введите число для выбора функции: '))
    if arg > 19 and arg < 0:
        print("Введите корректное значение!")
        startlab()
    if arg == 0:
       sys.exit()
    if arg == 1:
        lab1ex1()
    if arg == 2:
        lab1ex2()
    if arg == 3:
        lab1ex3()
    if arg == 4:
        lab1ex4()
    if arg == 5:
        lab2ex1()
    if arg == 6:
        lab2ex2()
    if arg == 7:
        lab2ex3()
    if arg == 8:
        lab2ex4()
    if arg == 9:
        lab3ex1()
    if arg == 10:
        lab3ex2()
    if arg == 11:
        lab3ex3()
    if arg == 12:
        lab3ex4()
    if arg == 13:
        lab4ex1()
    if arg == 14:
        lab4ex2()
    if arg == 15:
        lab4ex3()
    if arg == 16:
        lab4ex4()
    if arg == 17:
        lab5ex1()
    if arg == 18:
        lab5ex2()
    if arg == 19:
        lab5ex3()
def continue_program():
    arg = str(input("Продолжить?\nДа - yes/Y/1\nНет - no/N/0\nВаш ответ: "))
    if arg == 'yes' or 'Y' or arg == "1":
        startlab()
    if arg == 'no' or 'N' or arg == "0":
        sys.exit()
    else:
        print('Введите допустимое значение!')
        continue_program()

startlab()






















