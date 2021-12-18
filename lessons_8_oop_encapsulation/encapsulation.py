# создайте класс Person, с атрибутами экземпляра name и age.
# Напишите метод  get_info для получения имени вместе с возрастом


# функция
# функция-процедура
# метод

# Инкапсуляция - механизм сокрытия данных.

class Person:
    public_attr = 'имеем доступ везде'
    _protected_attr = 'имеем доступ только в классе и в дочерних классах'
    __private_attr = 'имеем доступ только в классе'

    def __init__(self, name_param, age_param):
        self.name = name_param
        if age_param < 0:
            raise ValueError('Возраст не может быть отрицательным!')  # вызываем ошибку
        self.__age = age_param

    def get_info(self):  # метод функция, *возвращает значение
        info = f'Имя: {self.name}. Возраст: {self.__age}'
        return info

    def show_info(self):  # метод процедура, *ничего не возвращает
        info = f'Имя: {self.name}. Возраст: {self.__age}'
        print(info)

    @property  # декоратор проперти - позволяет работать методу как атрибут (*скобки не ставить)
    def age(self):  # геттер - получатель
        return self.__age

    def set_age(self, new_age):  # сеттер
        if new_age < 0:
            raise ValueError('Возраст не может быть отрицательным!')  # вызываем ошибку
        self.__age = new_age


p1 = Person(name_param='Токтосун', age_param=21)

age = p1.age
print(f'AGE RAVEN {age}')

# задание: создать класс Product с атрибутами экземпляра нейм и прайс,
# и атрибутами класса имя магазина. Инкапсулировать цену,
# чтобы он был числом и не был отрицательным.
# Написать геттер для получения цены, и сеттер для изменения.
