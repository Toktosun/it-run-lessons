

def custom_decorator(function):
    def wrapper():
        print('Начало нашей функции')
        function()
        print('Конец нашей функции')
    return wrapper


@custom_decorator
def print_triple_hello():
    print('Hello world')
    print('Hello world')
    print('Hello world')


NUMBER_PI = 3.14  # пишется с большими буквами потому что константа. (значение не меняется)
