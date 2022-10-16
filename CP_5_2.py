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


def enter_down():
    while True:
        a = input("Введите нижнюю целую границу допустимых значение в массиве: ")
        if len(a) == 1 and a.isdigit():
            return (a)
        elif len(a) > 1:
            if a[0] == '-' and a[1:].isdigit() or a.isdigit():
                return (a)
        print("Ошибка при вводе данных. Повторите ввод.")


def enter_up():
    while True:
        b = input("Введите верхнюю целую границу допустимых значение в массиве: ")
        if len(b) == 1 and b.isdigit():
            return (b)
        elif len(b) > 1:
            if b[0] == '-' and b[1:].isdigit() or b.isdigit():
                return (b)
        print("Ошибка при вводе данных. Повторите ввод.")


def full_array(array_len, a, b):
    array_len = int(array_len)
    array = [0] * array_len
    for i in range(array_len):
        array[i] = random.randint(a, b)
    print("Массив:", array)
    return (array)


def in_both_array(array_A, array_B, array_both):
    for i in range(len(array_A)):
        for j in range(len(array_B)):
            if ((array_A[i] == array_B[j]) and (array_both[array_A[i] - a] == False)):
                array_both[array_A[i] - a] = True
    return (array_both)


def print_array_both(array_both):
    for i in range(len(array_both)):
        if array_both[i] == True:
            print("Элемент общий для A и B:", i + a)


a = int(enter_down())
b = int(enter_up())
print("Массив A:")
array_len_A = int(enter_array())
print("Массив B:")
array_len_B = int(enter_array())

array_A = [0] * array_len_A
array_B = [0] * array_len_B

array_A = full_array(array_len_A, a, b)
array_B = full_array(array_len_B, a, b)

array_both = [0] * (b - a + 1)
array_both = in_both_array(array_A, array_B, array_both)
print_array_both(array_both)
