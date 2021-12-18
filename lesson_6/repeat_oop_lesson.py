# ООП - парадигма программирования. подход к программирания.
# Три принципа ООП:
# 1. Наследование - это механизм, посредством которого один объект может приобретать свойства другого.

class OneFloorHouse:  # *одноэтажныйдом
    total_square = 100  # атрибут класса
    material = 'block'

    def __init__(self, room_count_param, wall_height_param):  # магический метод - конструктор
        self.room_count = room_count_param  # атрибут экземпляра
        self.wall_height = wall_height_param

    def get_volume(self):
        total_volume = self.total_square * self.wall_height
        return total_volume


class TwoFloorHouse(OneFloorHouse):
    total_square = 165

    def get_volume(self):
        return self.wall_height * self.total_square


house1 = OneFloorHouse(room_count_param=5, wall_height_param=2.80)  # создаем экземпляр класса, посредством конструктора
house2 = OneFloorHouse(room_count_param=7, wall_height_param=3)

print(house1.total_square)  # обращаемся к значению атрибута
print(house1.room_count)
print(house1.wall_height)

house_first_volume = house1.get_volume()
house_second_volume = house2.get_volume()


two_floor_house1 = TwoFloorHouse(room_count_param=8, wall_height_param=3)
print(two_floor_house1.total_square)
print(two_floor_house1.wall_height)

two_floor_house1.get_volume()

# Задание: создаем класс Rectangle, принимает длину и ширину и имеет метод получить площадь.
# Унследуемся от данного класса в класс Paralelipiped принимает длину, ширину и высоту,
# и дополнительно имеет метод получить объем.


class Rectangle:
    type_figure = 'geometric figure'

    def __init__(self, length_param, width_param):
        self.length = length_param
        self.width = width_param

    def get_square(self):
        square = self.length * self.width
        return square


class Parallelepiped(Rectangle):

    def __init__(self, length_param, width_param, height_param):  # переписываем конструктор
        self.length = length_param
        self.width = width_param
        self.height = height_param

    def get_square(self):
        square = 2*(self.width * self.height + self.width * self.length + self.length * self.height)
        return square

    def get_volume(self):
        volume = self.length * self.width * self.height
        return volume


class ObliqueParallelepiped(Parallelepiped):
    pass


class First:
    x = 1


class Second(First):
    x = 8
    y = 4


class Third(Second):
    z = 5
