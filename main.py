# In the process of learning, I created a simple calculator in python
x = float(input('Введите значение 1:'))
y = float(input('Введите значение 2:'))
# I ask the user to enter the numbers with which actions will be performed in the future
print('Какое действие вы хотите сделать?')
print('варианты ответа: +','сложение', '-', 'вычитание' '*','умножение', '/', 'деление')
z = str(input())
if z == '+':
    print(x+y)
    i = x+y
elif z == '-':
    print(x-y)
    i = x-y
elif z == '*':
    print(x*y)
    i = x*y
elif z == '/':
    print(x/y)
    i = x/y
else:
    print('Вы выбрали непредусмотренное действие')
# all actions of the calculator are performed through the function if
print(i)
print('давайте продолжим, введите второе значение помимо полученного...')
c = float(input('Введите значение:'))
print('Какое действие вы хотите сделать?')
k = str(input())
# We ask the user to enter the following number to continue the action
if k == '+':
    print(i+c)
if k == '-':
    print(i-c)
if k == '*':
    print(i*c)
if k == '/':
    print(i/c)
# all actions of the calculator are performed through the function if