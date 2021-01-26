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