import re

string_in = input("Введите ваше сообщение: ")
string_out = ''
words = re.split(r'\s+', re.sub(r'[.,\-!?]', ' ', string_in).strip())

for i in words:
    for c in i:
        if len(i) >=5 or len(i) <= 1:
            string_out+= i+' '
            break
print(string_out)