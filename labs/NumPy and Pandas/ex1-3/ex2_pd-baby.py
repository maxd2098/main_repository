import pandas as pd
import numpy as np
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt

rnames = ['Name', 'Gender', 'Number']
babynames = pd.read_table('yob1880.txt', delimiter = ',', names=rnames, header=None, engine='python')
babynames['Year'] = 1880
#print(babynames)

baby_prop = babynames.groupby(['Gender', 'Name', 'Year']).sum()[['Number']]
#print(baby_prop)

#1 - Вывести общее число младенцев каждого пола
baby = pd.pivot_table(babynames,
                          index = ['Gender'],
                          values = ['Number'],
                          aggfunc = np.sum)
#print(baby, '\n\n')

#2 - Собрать все данные в один DataFrame, добавить столбец year
baby_all = []
ye = []
for filename in glob.glob('*.txt'):
    year = int(filename[3:7])
    ye.append(year)
    baby = pd.read_table(filename, delimiter=',', names=rnames, header=None, engine='python')
    baby['Year'] = year
    baby_all.append(baby)
baby_all = pd.concat(baby_all)
#baby_sum_gender = baby_all.groupby(['Gender']).sum()[['Number']]

#3 - Получить сумму родившихся младенцев по полу, для каждого года, построить графики
baby_sum_gender = pd.pivot_table(baby_all,
                          index = ['Year'],
                          columns = ['Gender'],
                          values = ['Number'],
                          aggfunc = np.sum)
#baby_plot = baby_all.Year
#print(baby_sum_gender.Number['F'])
#fig = plt.figure()
'''plt.plot(baby_sum_gender.index, baby_sum_gender.Number['F'])
plt.plot(baby_sum_gender.index, baby_sum_gender.Number['M'])
plt.title('Baby')
plt.xlabel('Year')
plt.ylabel('Number')
plt.grid(True)
plt.show()'''
#print('\n\n', baby_all)
#baby_sum_gender.plot()

#4 - Добавить столбец proportion, содержащий долю младенцев данного имени, относительно общего числа
sum_all = pd.pivot_table(baby_all,
                          index = ['Year'],
                          values = ['Number'],
                          aggfunc = np.sum)
sum_all = sum_all['Number'].sum()
baby_all['Properties'] = baby_all['Number'] / sum_all
#print(sum_all)
#print('\n\n', baby_all)

#5 - Графики для общего числа и относительной доли младенцев получавших след. имена:
graph = pd.pivot_table(baby_all,
                        index = ['Name', 'Year'],
                        values = ['Properties'])
johnny = graph.loc['Johnny']
natalie = graph.loc['Natalie']
bob = graph.loc['Bob']
maxim = graph.loc['Max']
#print('\n\n', natalie)
'''plt.plot(johnny.index, johnny)
plt.plot(natalie.index, natalie)
plt.plot(bob.index, bob)
plt.plot(maxim.index, maxim)

plt.title('Graph')
plt.xlabel('Year')
plt.ylabel('Properties')
plt.grid(True)
plt.show()'''

#6 - найти самые популярные в каждом году имена
popular_name = baby_all.groupby(['Year'])
print(popular_name.first())
popular_name = popular_name.apply(lambda x: x.sort_values(by='Number', ascending=False)[:1])
del popular_name['Properties'], popular_name['Gender']
#print(popular_name)













