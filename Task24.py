#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
#грядке, причем кусты высажены только по окружности. Таким образом, у каждого
#куста есть ровно два соседних. Всего на грядке растет N кустов.
#Семинар 4 2
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
#выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#Собирающий модуль за один заход, находясь непосредственно перед некоторым
#кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может
#собрать за один заход собирающий модуль, находясь перед некоторым кустом
#заданной во входном файле грядки.

# Читаем N
N = int(input())
# Читаем урожайность кустов
berry_counts = list(map(int, input().split()))
# Инициализируем максимальное число собранных ягод нулем
max_berry_count = 0
# Проходим по всем возможным тройкам кустов
for i in range(N):
    # Обрабатываем случаи для кустов на краях грядки
    if i == N-1:
        # Куст в конце грядки
        berry_count = berry_counts[i] + berry_counts[0] + berry_counts[1]
    elif i == N-2:
        # Куст предпоследний
        berry_count = berry_counts[i] + berry_counts[i+1] + berry_counts[0]
    else:
        berry_count = berry_counts[i] + berry_counts[i+1] + berry_counts[i+2]
    # Обновляем максимальное число собранных ягод
    max_berry_count = max(max_berry_count, berry_count)
# Выводим результат
print(max_berry_count)