"""Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1+2+3)
100 -> 1 (1+0+0)"""

num = int(input("Введите трехзначное число: "))
print(num//100 +num//10%10 +num%10)