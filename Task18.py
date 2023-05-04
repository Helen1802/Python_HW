#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    6
#    -> 5

n = int(input())
a = list(map(int, input().split()))
x = int(input())

min_diff = 10**9
ans = a[0]

for i in range(n):
    diff = abs(a[i] - x)
    if diff < min_diff:
        min_diff = diff
        ans = a[i]

print(ans)