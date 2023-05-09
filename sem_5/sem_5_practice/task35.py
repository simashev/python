# 35. Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым

# *Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1  и n(само число)*
# 5 -> Yes (имеет делители: 5, 1)
# 4 -> No (имеет делители: 2, 1, 4)
# 9 -> No (имеет делители: 1, 3, 9)

def is_prime(n: int, divider: int) -> bool:
    """рекурсивная проверка простоты числа"""
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)


n = 11
print(is_prime(n, n//2 + 1))

for i in range(n//2 + 1, 1, -1):
    print(i, n % i)

# def prime_num(num):
#     for i in range(2,num-1):
#         if num%i==0:
#             return('NO')
#     return('YES')



# n=int(input('Введите число: '))
# print(prime_num(n))