# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. Он 
# задумывает два натуральных числа X и Y (X,Y≤1000), а 
# Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите 
# Кате отгадать задуманные Петей числа.

# Пример
# Ввод: 5 6 -> Вывод: 2 3

s_sum = int(input('sum: '))
p_mult = int(input('mult: '))
flag = True
for x in range(s_sum):
    if x * (s_sum - x) == p_mult:
        print(f'result: {x} {s_sum - x}')
        flag = False
        break
if flag:
    print('No results: ')

# import math

# S = int(input())
# P = int(input())

# D = S**2 - 4*P

# if D < 0:
#     print("No solution")
# elif D == 0:
#     X = Y = S/2
#     if X.is_integer() and Y.is_integer():
#         print(int(X), int(Y))
#     else:
#         print("No solution")
# else:
#     X1 = (S + math.sqrt(D))/2
#     X2 = (S - math.sqrt(D))/2
#     Y1 = S - X1
#     Y2 = S - X2
#     if X1.is_integer() and Y1.is_integer():
#         print(int(X1), int(Y1))
#     elif X2.is_integer() and Y2.is_integer():
#         print(int(X2), int(Y2))
#     else:
#         print("No solution")
