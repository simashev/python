# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

# A = list(map(int, input("Введите первый список: ").split())) 
# B = list(map(int, input("Введите второй список: ").split())) 
# print (A)
# print (B)
# C = []
# # i=0
# for i in A:
#     for k in B:
#         if i == k:
#             result = [i]
#             print (*result)

# --
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')