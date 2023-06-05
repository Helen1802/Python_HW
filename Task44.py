# В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI'lst})
#data.head() 


import pandas as pd
import random

# Генерируем исходный датафрейм
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный датафрейм:")
print(data)

# Преобразуем данные в one hot вид
one_hot = pd.get_dummies(data['whoAmI'])
one_hot.columns = ['is_human', 'is_robot']
print("Данные в one hot виде:")
print(one_hot)

# Объединяем исходный датафрейм и one hot датафрейм
result = pd.concat([data, one_hot], axis=1)
print("Результирующий датафрейм:")
print(result)

