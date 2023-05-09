#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
def find_indexes_in_range(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes