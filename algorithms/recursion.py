n = int(input())  # 4! = 1*2*3*4

result = 1
for number in range(1, n+1):
    result *= number  # result = result * number

print(f'Факториал {result}')


def calculate_factorial(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n-1)


calculate_factorial(5)
