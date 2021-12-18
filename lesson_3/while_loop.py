# Циклы позволяют повторять некоторое действие в зависимости от соблюдения некоторого условия.
#
# Цикл while
# Первый цикл, который мы рассмотрим, это цикл while. Он имеет следующее формальное определение:
#
# while условное_выражение:
#    инструкции

# После ключевого слова while указывается условное выражение, и пока это выражение возвращает значение True, будет выполняться блок инструкций, который идет далее.
# Все инструкции, которые относятся к циклу while, располагаются на последующих строках и должны иметь отступ от начала строки.

counter = 1
while counter <= 3:  # цикл с предусловием
    counter = counter + 1


numbers_range = range(1, 11)

for num in numbers_range:
    if num % 2 == 0:
        pass
        # print(f'chetnoe num = {num}')

count = int(input())
summa_kubov = 0
for num in range(1, count+1):
    summa_kubov += num ** 3

print(summa_kubov)


stroka = input()

probel_count = stroka.count(' ')
word_count = probel_count + 1
print(word_count)
