class Person:
    """Класс человек"""

    def __init__(self, name, age, salary):
        self.name = name
        if age in range(1, 100):
            self.__age = age
        else:
            raise ValueError('Недопустимый возраст')
        self.salary = salary

    def info(self):
        print(f'name: {self.name}')
        print(f'age: {self.__age}')
        print(f'salary: {self.salary}')

    @property
    def age(self):
        return self.__age


class Employee(Person):
    """Класс работник"""
    __boss = None  # будет привязан к одному начальнику

    @property
    def boss(self):
        return self.__boss

    def set_boss(self, boss_pm):
        if isinstance(boss_pm, Boss):
            self.__boss = boss_pm
        else:
            raise ValueError('Не является экземпляром класса Boss')

    def info(self):
        super().info()
        print(f'boss: {self.__boss}')

    def __repr__(self):
        return f'Работник: {self.name}'

    def __str__(self):  # метод строкового представления, вызывается когда печатается сам экземпляр
        return f'Работник: {self.name}'


class Boss(Person):
    """Класс начальника"""

    employers = []  # множество сотрудников

    def __str__(self):
        return f'Начальник: {self.name}'

    def info(self):
        super().info()
        print(f'employers: {self.employers}')


first_worker = Employee(name='Работник-1', age=20, salary=35000)
second_worker = Employee(name='Работник-2', age=28, salary=40000)
first_boss = Boss(name='Начальник-1', age=97, salary=50000)

print('До привязки: ', second_worker.boss)
second_worker.set_boss(boss_pm=first_boss)
print('После привязки: ', second_worker.boss)

# для класса Boss напишите метод add_employee
# который принимает параметр employee_pm,
# и в если employee_pm является экземпляром класса Employee
# то добавляет в список employers

# Сделаем ооп паттерн как в инстаграме.
# Реализуем классы User, Article (*публикация), ArticleStatData (статистические данные по публикации)
# Обязательные Атрибуты для пользователя: username, articles, birthday.
# Обязательные Атрибуты для Article: image, user, stat (прикреплен к статистическим данным).
# Обязательные Атрибуты для ArticleStatData: article, see_count, like_count.
