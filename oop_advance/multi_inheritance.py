class A:
    value = 'A'


class B:
    value = 'B'


class C:
    value = 'C'


class Z(A, B, C):  # множественное наследование
    pass


instance = Z()
print(instance.value)
