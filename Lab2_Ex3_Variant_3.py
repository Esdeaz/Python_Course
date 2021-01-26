import random
 
l = [str(random.randint(0,9)) for i in range(5)]
l.insert(random.randint(0,5), '3')
print(''.join(l))