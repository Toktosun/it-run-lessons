def calculate_summa(x, y, c):
    summa = x + y + c
    return summa


def square_rectangle(length, width):
    return length * width


first = int(input('Ввеите длину прямоугольника'))
second = int(input('введите ширину прямоугольника'))

square = square_rectangle(first, second)


def calculate_ariph_operation(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    elif operation == '-':
        return x - y


def calculate_discriminate(a, b, c):
    discriminant = b**2 - 4 * a * c
    return discriminant


x = calculate_discriminate(3, -7, 4)
print(x)

# задание: Программа рещающая квадратное уравнение.
# написать функцию принимающая a,b,c.
# Возвращает корни уравнения

# пример:
# коэфициенты: (3, -14, -5)
# корни: 5 и -1/3

from math import sqrt, ceil


def nayti_korni_uravnenya(a, b, c):
    discriminat = b**2 - 4 * a * c
    x1 = (-b + sqrt(discriminat)) / (2*a)
    x2 = (-b - sqrt(discriminat)) / (2*a)
    return x1, x2


koren1, koren2 = nayti_korni_uravnenya(3, -14, -5)
print('первый корень равен ' + str(koren1))
print('второй корень равен ' + str(koren2))


my_number = int(input())
print(f'The {my_number} is {my_number+1}.')
print(f'The  {my_number} is {my_number+1}.')
city = 'Bishkek'
stroka = f'{city} is capital of Kyrgyzstan'
diferent_stroka = city + 'is capital of Kyrgyzstan'


first_cab = int(input())
second_cab = int(input())
third_cab = int(input())

first_table_count = ceil(first_cab / 2)
second_table_count = ceil(second_cab / 2)
third_table_count = ceil(third_cab / 2)
print(first_table_count + second_table_count + third_table_count)
