# In the process of learning, I created a simple calculator in python
first_num = float(input('Введите значение 1: '))
second_num = float(input('Введите значение 2: '))

# I ask the user to enter the numbers with which actions will be performed in the future
print('Какое действие вы хотите сделать?')
print('варианты ответа: +', 'сложение', '-', 'вычитание' '*','умножение', '/', 'деление')

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
# print(result)  Здесь лишний принт, т.к. в условных выражениях у тебя уже прописаны принты
print('давайте продолжим, введите второе значение помимо полученного...')
final_num = float(input('Введите значение: '))
print('Какое действие вы хотите сделать?')

operator2 = str(input("Введите оператор: "))

# We ask the user to enter the following number to continue the action
if operator2 == '+':
    print(result + final_num)
if operator2 == '-':
    print(result - final_num)
if operator2 == '*':
    print(result * final_num)
if operator2 == '/':
    print(result / final_num)

# all actions of the calculator are performed through the function if
