# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
# 001001 -> yes

number = int(input("введите шестизначный номер билета: "))

x = number//1000
x = x%10 + (x%100 - x%10)//10 + x//100 
print (f"Cумма первых чисел в билете: {x}") 
y = number%1000
y = y%10 + (y%100 - y%10)//10 + y//100
print (f"Cумма первых чисел в билете: {y}")
if (x==y):
    print ("yes")
else:
    print ("no")
