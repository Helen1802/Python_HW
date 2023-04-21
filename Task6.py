"""Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no"""
ticket_number = '689423'
# разбиваем номер билета на цифры и суммируем первые три и последние три цифры
first_half = sum([int(digit) for digit in ticket_number[:3]])
second_half = sum([int(digit) for digit in ticket_number[3:]])
if first_half == second_half:                         # проверяем, равны ли суммы первой и второй половин билета
    print(ticket_number, '-> yes')
else:
    print(ticket_number, '-> no')