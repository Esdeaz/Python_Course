import random

n = int(input('Введите число N для размера квадратной матрицы: '))
a_list = [[0] * n for i in range(n)] #создание матрицы
s = 0

for i in range(n): #заполнение матрицы случайными числами и их суммирование
    for j in range(n):
        a_list[i][j] = random.randint(0, 100)
        s += a_list[i][j]
    
print(a_list)
print("Сумма чисел в матрице: ", s)