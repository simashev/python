# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

N = int (input('Введите число N '))
for k in range(N):
    if 2 ** k <= N:
        print(2 ** k, end = ', ')


right_side = int(input('rigth side: '))
degree = 0
while 2**degree <= right_side: 
    print(2**degree, end=" ")
    degree += 1

right_side = int(input('rigth side: '))
degree = 0
num = []
while 2**degree<= right_side:
    num.append(2**degree)
    degree += 1
print(num)

