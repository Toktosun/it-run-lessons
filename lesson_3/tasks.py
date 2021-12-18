# функция которая печатает hello world 3 раза
def calculate_sum(a, b):
    summa = a + b
    return summa


def triple_hello_world():
    print('Hello world!')
    print('Hello world!')
    print('Hello world!')
    print('Hello world!')


laptop_list = ['asus', 'samsung', 'lenovo', 'apple']
position = 0
# for item in laptop_list:
#     position = position + 1
#     print(f'close: {item}')
# print(f'Всего ноутбуков пройдено {position}')

# создайте список с 4 вашими любимыми блюдами,
# добавьте дополнительно 5 блюдо это пицца.
# в цикле когда блюдо будет пиццой
# напечатайте пицца найдена.

dishes = ['pizza', 'lagman']
dishes.append('sushi')
for dish in dishes:
    if dish == 'pizza':
        print('пицаа найдена')

# напишите функцию которая принимает лист
# с интежерами,
# и возвращает общее произведение элементов листа
l = [5, 6, 2, 4]


def calc_summa_of_list(number_list):
    summa = 0
    for number in number_list:
        summa = summa + number
    return summa


s = calc_summa_of_list(l)

print(s)

x = 1
y = 2
old_x = x
x = y

city_list = ['bishkek', 'moscow', 'ny']
item = ''
i = 0
while item != 'moscow':
    item = city_list[i]
    i = i + 1
iteration = 0
while iteration != 3:
    print('Hellow world')
    iteration = iteration + 1
