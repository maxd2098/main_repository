import pandas as pd
import math

#1 ---------------------------------------
#arr = []
with open('input (2).txt', 'r') as data:
    arr = data.readlines()
#print(*arr, sep='')
string = arr[-1]
string = string[:-2] + '\n'
arr.pop()
arr.append(string)
arr.reverse()
#print(*arr, sep='', end='\n')

#2 ---------------------------------------
arr = []
with open('input (3).txt', 'r') as data:
    for int_str in data:
        arr.append(int_str.split())

sum_arr = []
for i in range(len(arr)):
    summ = 0
    for j in range(len(arr[i])):
        summ += int(arr[i][j])
    sum_arr.append(summ)
#print(*sum_arr)

#3 ----------------------------------------
with open('input.txt', 'r') as data:
    arr = data.read()
arr = arr.split()
#print(len(set(arr)))

#4 ----------------------------------------
data = pd.read_csv('input.csv', sep=';', names = ['Company', 'Money'])
#print(data)
str_arr = data['Company'].apply(lambda x: ';' + str(x))
data['Company'] = str_arr
tmp_str = data.Company
data = data.drop('Company', axis='columns')
data['Company'] = tmp_str
data = data.sort_values(by = ['Money', 'Company'], ascending = [False, True])
#print(data)

#5 -----------------------------------------
data = pd.read_csv('input (1).csv', sep=';', index_col=0)
data_min = data.describe()
data_min = data_min.loc['min']
data_min = data_min.sort_index().sort_values()
data_min = data_min[[0]]
min_shop = data[data[data_min.index] == data_min[0]]
min_shop = min_shop.dropna(how='all', axis=1).dropna(how='all', axis=0)
#print(min_shop.columns[0], '\t',  min_shop.index[0])
#print(data_min)

#6 -----------------------------------------
data_gui = pd.read_excel('trekking2.xlsx', sheet_name = 'Справочник', index_col = 0)
data_lay = pd.read_excel('trekking2.xlsx', sheet_name = 'Раскладка', index_col = 0)
data = pd.concat([data_gui, data_lay], axis=1, copy = False) #объединяем таблицы по столбцам
data = data.dropna(axis=0, subset = [data.columns[-1]]) #удаляем строки где нет веса в граммах
sum_cal = ((data[data.columns[0]] * data[data.columns[-1]])/100).sum()
bel_100 = ((data[data.columns[1]] * data[data.columns[-1]])/100).sum()
zhi_100 = ((data[data.columns[2]] * data[data.columns[-1]])/100).sum()
ugl_100 = ((data[data.columns[3]] * data[data.columns[-1]])/100).sum()
#pd.set_option('display.max_columns', None) #показать все столбцы
#print(data)
#print(data[data.columns[0]].sum()) #сумм калорийность всех продуктов на 100
print(math.ceil(sum_cal), math.ceil(bel_100), math.ceil(zhi_100), math.ceil(ugl_100))
















        
