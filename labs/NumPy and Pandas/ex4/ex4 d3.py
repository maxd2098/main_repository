import pandas as pd
import numpy as np

#1 -------------------------------------
with open('input.txt', 'r') as data:
    data = data.read()
data = set(data.split())
#print(len(data))

#2 -------------------------------------
with open('input (1).txt', 'r') as data:
    data = data.read()
data = data.replace('\n', ' ')
data = data.split()
#print(data)
data_dict = dict()
for i in data:
    if i in data_dict:
        data_dict[i] = data_dict[i] + 1
    else:
        data_dict[i] = 1
#print(data_dict)
data_list = list(data_dict.items())
data_list = [(i[1], i[0]) for i in data_list]

#data_list = set(data_list)
#print(data_list)
#data_list.sort()
#data_list.sort(key=lambda x: x[0], reverse=True)
#data_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
#for i in range(len(data_list)):
    #print(data_list[i][1], end=' ')

#3 --------------------------------------
with open('input (4).txt', 'r') as data:
    data = data.readlines()
#print(len(data[0]))
max_str = max(len(i) for i in data)
#print(max_str)
'''for string in data:
    if len(string)==max_str:
        print(string)'''

#4 -------------------------------------
with open('input (6).txt', 'r') as data:
    data = data.read()
#print(data)
data = data.split('\n')
data.pop()
arr = []
for i in range(len(data)):
    string = data[i]
    string = string[::-1]
    arr.append(string)
arr = '\n'.join(arr[::-1])
#print(arr)

#5 --------------------------------------
data = pd.read_csv('input.csv', sep = ';', names = ['Company', 'Money'])
data = pd.pivot_table(data, index=['Company'], values=['Money'], aggfunc=np.mean)
data = data.sort_index(axis=0)
#print(data)
data = data.sort_values(by = 'Money')
#print(*data.index, sep='\n')

#6 ---------------------------------------
pd.set_option('display.max_columns', 4) #показать все столбцы
data = pd.read_excel('trekking1.xlsx')
data = data.rename(columns={data.columns[0]:'Название'})
data = data.sort_values(by=[data.columns[0]])
data = data.sort_values(by=[data.columns[1]], ascending=False, kind='mergesort')
#mergesort для того, чтобы сохранить начальную последовательность элементов с одинаковым columns[1]
#print(*data[data.columns[0]], sep='\n')













    