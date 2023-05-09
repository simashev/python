# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Решение циклом:
# def Pow (number: int,rank: int) -> None:
#     "Возведение в степень B числа A"
#     result = 1
#     if (rank==0):
#         print(result)
#     for i in range (rank):
#         result = result * number
#         i = i + 1 
#     print (result)

# Pow(A,B)

# Решение рекурсией
def Pow (number: int,rank: int):
    "Возведение в степень (rank) числа (number)"
    if (rank==0): 
        return 1
    result = number * Pow (number,rank-1)
    return result

print (Pow (A,B))