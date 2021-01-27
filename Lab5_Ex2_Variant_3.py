import re

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