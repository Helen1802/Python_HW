#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no
n=int(input("input n - ")) 
m=int(input("input m - ")) 
k=int(input("input k - "))

# проверяем, что количество долек, которые нужно отломить, меньше или равно общему количеству долек в шоколадке
if k <= n * m:
    # проверяем, можно ли отломить k долек, сделав один разлом по прямой между дольками
    if k % n == 0 or k % m == 0:
        print('yes')
    else:
        print('no')
else:
    print('no')

