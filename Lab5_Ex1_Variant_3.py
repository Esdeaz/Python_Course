import os

path = os.getcwd()#получение текущей директории
#Подсчет файлов, которые находятся в текущей директории
num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
print(num_files)
