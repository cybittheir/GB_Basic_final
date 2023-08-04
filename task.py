#
# Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
#

import math

from random import randint

array_len = int(input("Введите размер массива: "))
max_num = int(input("Введите максимальную длину слова в массиве: "))

new_array=list()
result = list()

for i in range(array_len):
    word = ""
    for j in range(randint(1, max_num + 1)):
        select_ascci_range = randint(0,3);
        match select_ascci_range:
            case 1:
                word += chr(randint(65,90))
            case 2:
                word += chr(randint(97,122))
            case _:
                word += chr(randint(48,57))

    new_array.append(word)
    
print ("Полный список для контроля: ", new_array)

for j in range(len(new_array)):
    if len(new_array[j]) <= 3:
        result.append(new_array[j])

print("Выборка/результат: ", result)
