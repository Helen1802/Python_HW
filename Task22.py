#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются
#в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы
#множеств.

#Для решения этой задачи можно использовать множества (set) в Python. 
# Множества не содержат повторяющихся элементов, поэтому мы можем создать два множества 
# из введенных пользователем элементов и использовать операцию пересечения множеств для получения общих элементов.


n = int(input())  # количество элементов первого множества
set_a = set(map(int, input().split()))  # первое множество

m = int(input())  # количество элементов второго множества
set_b = set(map(int, input().split()))  # второе множество

common_elements = sorted(list(set_a & set_b))  # пересечение множеств и сортировка элементов

for element in common_elements:
    print(element)  # выводим общие элементы по порядку возрастания
