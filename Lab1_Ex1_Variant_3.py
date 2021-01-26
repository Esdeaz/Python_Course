import math

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