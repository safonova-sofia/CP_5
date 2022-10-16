import random


def check_array_len(number):
    if number.isdigit() and number[0] != '0':
        return True


def enter_array():
    while True:
        array_len = input('Введите размерность массива: ')
        if check_array_len(array_len):
            return (array_len)
        else:
            print("Ошибка при вводе данных. Повторите ввод.")


def full_array(array_len):
    array_len = int(array_len)
    array = [0] * array_len
    for i in range(array_len):
        array[i] = float(format(random.triangular(-7, 9), '.1f'))
    print("Массив:", array)
    return (array)


def maximum_f(array):
    maximum = -10 ** 10
    for i in range(len(array)):
        if array[i] > maximum:
            index = i
            maximum = array[i]
    print("Максимальный элемент:", maximum, "\nИндекс максимального элемента:", index)
    return (index)


def mod_array(ind_maximum, array):
    for i in range(ind_maximum + 1, len(array)):
        array[i] = 0
    print("Преобразованный массив:", array)
    return (array)


array = full_array(enter_array())
mod_array(maximum_f(array), array)