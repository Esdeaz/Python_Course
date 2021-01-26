# -*- coding: utf-8 -*-
import random

my_number = random.randint(0, 100)
print("Случайное число: ", my_number, '\t')
user_number = int(input("Введите свое число: "))

while user_number == my_number:
    user_number = int(input("Введите свое число: "))
    print("Ваше число: ", user_number)
