def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

a = int(input())  # число, которое нужно возвести в степень
b = int(input())  # степень, в которую нужно возвести число

result = power(a, b)
print(result)  # выводим результат возведения числа A в степень B
