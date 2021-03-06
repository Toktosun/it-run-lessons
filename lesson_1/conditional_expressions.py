# Условные выражения

# Ряд операций представляют условные выражения. Все эти операции принимают два операнда и возвращают логическое значение, которое в Python представляет тип boolean. Существует только два логических значения - True (выражение истинно) и False (выражение ложно).
#
# Операции сравнения
# Простейшие условные выражения представляют операции сравнения, которые сравнивают два значения. Python поддерживает следующие операции сравнения:
# == Возвращает True, если оба операнда равны. Иначе возвращает False.
# != Возвращает True, если оба операнда НЕ равны. Иначе возвращает False.
# > (больше чем) Возвращает True, если первый операнд больше второго.
# < (меньше чем) Возвращает True, если первый операнд меньше второго.
# >= (больше или равно) Возвращает True, если первый операнд больше или равен второму.
# <= (меньше или равно) Возвращает True, если первый операнд меньше или равен второму.
# Примеры операций сравнения:
a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True

bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2

# Логические операции

# and (логическое умножение) Возвращает True, если оба выражения равны True
age = 22
weight = 58
result = age > 21 and weight == 58
print(result)  # True

# or (логическое сложение) Возвращает True, если хотя бы одно из выражений равно True
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)  # True, так как выражение age > 21 равно True

# not (логическое отрицание) Возвращает True, если выражение равно False
age = 22
isMarried = False
print(not age > 21)  # False
print(not isMarried)  # True
