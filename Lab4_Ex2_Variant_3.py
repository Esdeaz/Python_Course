import random

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

