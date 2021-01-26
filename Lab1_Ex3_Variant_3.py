list = [4, 10, -4, 6, 3, 5, 20]
S = 1

for x in list:
    if x < 10:
        S *= x
    else:
        continue
print(S)