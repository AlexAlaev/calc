def calc():
    first_num = float(input('Введите значение 1: '))
    second_num = float(input('Введите значение 2: '))

    # I ask the user to enter the numbers with which actions will be performed in the future
    print('Какое действие вы хотите сделать?')
    print('варианты ответа: +', 'сложение', '-', 'вычитание' '*', 'умножение', '/', 'деление')

    operator = str(input("Введите оператор: "))

    if operator == '+':
        print(first_num + second_num)
        result = first_num + second_num
    elif operator == '-':
        print(first_num - second_num)
        result = first_num - second_num
    elif operator == '*':
        print(first_num * second_num)
        result = first_num * second_num
    elif operator == '/':
        print(first_num / second_num)
        result = first_num / second_num
    else:
        print('Вы выбрали непредусмотренное действие')

    # all actions of the calculator are performed through the function if

    start = 'start'
    while start != 'stop':
        print('Если хотите завершить программу, то напишите "stop", если хотите продолжить, то введите что угодно')
        stopper = str(input("Ввод: "))
        if stopper == 'stop':
            print('Программа завершена')
            break
        print('давайте продолжим, введите второе значение помимо полученного...')
        final_num = float(input('Введите значение: '))
        operator2 = str(input('Введите оператор: '))

        # We ask the user to enter the following number to continue the action
        
        if operator2 == '+':
            print(result + final_num)
            result += final_num
        if operator2 == '-':
            print(result - final_num)
            result -= final_num
        if operator2 == '*':
            print(result * final_num)
            result *= final_num
        if operator2 == '/':
            print(result / final_num)
            result /= final_num

        # all actions of the calculator are performed through the function if

calc()

#31