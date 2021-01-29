dict_std =  {1: ["Иванов Иван Иванович", "23", "БО-111111"],
             2: ["Аваакумов Антон Антонович", "21", "БО-111111"],
             3: ["Измаилов Радмир Викторович", "22", "БО-222222"]}

def add_new_student(): #Добавление нового студента
    dict_length = len(dict_std)
    full_name = input("Введите полное ФИО студента: ")
    age = input("Введите возраст студента: ")
    group_num = input("Введите номер группы студента: ")
    dict_std.update({dict_length + 1: [full_name, age, group_num]})
    dict_length = dict_length + 1
    
def edit_stduent_info():#Изменение инфы о студенте
    num_st = int(input("Введите номер студента: "))
    if num_st > len(dict_std) or num_st < 1:
        print("Введите корректное значение!")
        edit_stduent_info()
    else:
        full_name = input("Введите полное ФИО студента: ")
        age = input("Введите возраст студента: ")
        group_num = input("Введите номер группы студента: ")
        dict_std.update({num_st: [full_name, age, group_num]})

def delete_student_info(): #Удаление данных о студенте
    num_st = int(input("Введите номер студента: "))
    if num_st > len(dict_std) or num_st < 1:
        print("Введите корректное значение!")
        delete_student_info()
    else:
        dict_std.pop(num_st)
def output_student():#Выводит инфу о студенте
    num_st = int(input("Введите номер студента: "))
    if num_st > len(dict_std) or num_st < 1:
        print("Введите корректное значение!")
        output_student()
    else:
        for el in dict_std[num_st]:
            print(el, ' ', end = '')


output_student()