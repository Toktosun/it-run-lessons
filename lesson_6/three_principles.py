# Принципы ООП
# 1.Наследование
# 2.
# 3.


# Наследование

class Person:
    skin_color = 'white'
    hands_count = 2
    foot_count = 2
    gender = None

    def say_hello(self):
        print(f'Hello! My skin color is {self.skin_color}')

    def get_info(self):
        print(f'{self.skin_color=}')
        print(f'{self.hands_count=}')
        print(f'{self.foot_count=}')
        print(f'{self.gender=}')

    def __str__(self):
        return f'Это наш мужчина c цветом волос {self.skin_color}'


class Man(Person):
    gender = 'муж'


class Woman(Person):
    gender = 'жен'


man1 = Man()
print(man1)
