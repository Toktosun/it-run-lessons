# Аннотация типов
# python - динамически типизирован
x = 5.453
city = str("Bishkek")


def calc_summa(a: int, b: int, c=0) -> int:
    summa = a+b+c
    return summa


summa = calc_summa(5, 6, 10)  # 21


def concatenate_strings(a: str, b: str, optial_param='!') -> str:
    return a + b + optial_param


concatenate_strings(b='guys', a='hello', optial_param='!!!')  # helloguys!!!

# утиная типизация
# Аннотация типов - нужна только для читателя кода и IDE редактора
