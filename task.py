#
# Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
#

import math

from random import randint

def genArray(array_len, max_num):
    for i in range(array_len):
        word = ""
        for j in range(randint(1, max_num)):
            select_ascii_range = randint(0,3)
            match select_ascii_range:
                case 1:
                    word += chr(randint(65,90)) # A - Z
                case 2:
                    word += chr(randint(97,122)) # a - z
                case _:
                    word += chr(randint(48,57)) # 0 - 9

        new_array.append(word)
    return new_array

def select(array, param):
    for j in range(len(array)):
        if len(array[j]) <= param:
            result.append(array[j])
    return result


array_len = int(input("Введите размер массива (10): ") or 10)
max_num = int(input("Введите максимальную длину слова в массиве (6): ") or 6)
max_result_word = int(input("Введите максимальную длину слова в результате (3): ") or 3)

new_array=list()
result = list()

new_array = genArray(array_len, max_num)

print ("Полный список для контроля: ", new_array)

result = select(new_array, max_result_word)

print("Выборка/результат: ", result)
