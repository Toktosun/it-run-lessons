# Типы Алгоритмов:
# Линейные
# Алгоритм с вветвлиниями  (*алгоритм с условием)
# Циклические алгоритмы


# Создайте класс Point,
# с атрибутами экземпляра x  и y.
# и поменяйте значения атрибутов местами.
# Примечание:значения атрибутов задается пользователем
# Написать метод выводит значение максимального атрибута,
# добавить опциональный параметр для третьего атриба z,
# если не передаем записывается None

class Point:

    def __init__(self, x_param, y_param, z_param=None):
        self.x = x_param
        self.y = y_param
        self.z = z_param

    def replace_coord_values(self):  # линейный алгоритм
        tmp = self.y
        self.y = self.x
        self.x = tmp

    def get_max_atr_value(self):  # алгоритм с вветвлиниями
        if self.x >= self.y and self.x >= self.z:
            return self.x
        elif self.y >= self.z and self.y >= self.x:
            return self.y
        else:
            return self.z


x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))

p1 = Point(x_param=x, y_param=y)


my_list = [-2, -6, -1, 534, 243]
max_number = my_list[0]
for number in my_list:
    if number > max_number:
        max_number = number

print(f'Max number is {max_number}')


# Найдите максимальный элемент

# Сравнить два числа и выдать максимальный.
a = 5
b = 6
if a > b:
    max_value = a
else:
    max_value = b
print(f'Max is {max_value}')


# 5! = 1*2*3*4*5

