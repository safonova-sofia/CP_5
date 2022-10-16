def format_10(number, ss):
    number = int(number)
    ss = int(ss)
    number_ss = ''
    while (number > 0):
        number_ss = str(number % ss) + number_ss
        number //= ss
    return ("Перевели из 10СС в " + str(ss)  + ": " + str(number_ss))


def check_number_10(number_10):
    if number_10.isdigit():
        return True

def check_ss(ss):
    if ss == "2" or ss == "8":
        return True

while True:
    number_10 = input('Исходное число в 10 СС: ')
    if check_number_10(number_10):
        while True:
            ss = input('В какую систему счисления переводим: ')
            if check_ss(ss):
                print(format_10(number_10, ss))
                break
            else:
                print("Ошибка при вводе данных. Повторите ввод.")
        break
    else:
        print("Ошибка при вводе данных. Повторите ввод.")

print("Двоичная:            ", format(int(number_10), 'b'))
print("Восьмеричная:        ", format(int(number_10), 'o'))