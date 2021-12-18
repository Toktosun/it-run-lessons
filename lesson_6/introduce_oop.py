# ВВЕДЕНИЕ В ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ

class Car:
    wheels_count = 4  # атрибуты класса
    manufacture_country = 'Germany'

    def __init__(self, brand, color, price, speed):  # конструктор
        """магический метод, два нижних подчеркивания"""
        self.brand = brand  # атрибуты экземпляра
        self.color = color
        self.price = price
        self.speed_value = speed


first_car = Car(brand='BMW', color='red',
                price='12000$', speed=120)
second_car = Car(brand='Mercedes', color='black',
                 price='12000$', speed=240)

print(first_car.color)  # red
first_car.color = 'blue'
print(first_car.color)  # blue


# Задание: создайте класс прямоугольник (Rectangle). который
# в конструкторе будет принимать значение длины и ширины.
# и задайте атрибут класса количество сторон со значением
# И создайте два прямоугольника со значениями 10 и 20; 5 и 17;

# class Rectangle:
#     side_count = 4  # атрибут класса
#
#     def __init__(self, length, width):
#         self.length = length  # атрибут экземпляра
#         self.width = width
#
#     def calculate_square(self):
#         square = self.length * self.width
#         return square
#
#     def calculate_perimeter(self):
#         perimeter = (self.length + self.width) * 2
#         return perimeter
#
#
# first_rectangle = Rectangle(length=10, width=20)
# ploshad = first_rectangle.calculate_square()  # 200
# print(first_rectangle.length)  # 10
# print(first_rectangle.width)  # 20
# # пишем метод для вычисления периметра
#
#
# def calculate_right_triangle_square(length, width):
#     square = (length * width) / 2
#     return square
#
#
# class RightTriangle:
#
#     def __init__(self, length_param, width_param):
#         self.length = length_param
#         self.width = width_param
#
#
# first_triangle = RightTriangle(length_param=5, width_param=6)
