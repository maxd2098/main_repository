import matplotlib.pyplot as plt
import pandas as pd

#%matplotlib inline

data = pd.read_csv('stud_Portug.csv', delimiter=',')
print(data)
'''print(data.head(6))
print(data.tail())
print(data.shape)'''
#print(data.columns)

#выводим таблицу без последней колонки
#print(data.drop(data.columns[-1], axis='columns').head())

#проверяем есть ли в данных пропуски
#print(data.isnull().any().any())

#выводим статистику по значениям признаков
#print(data.sort_index(axis=1))

#Какая причина выбора школы была самой частой? В качестве ответа приведите соответствующее значение признака.
#print((data['reason'].value_counts())[0:1], '\n\n')

#Какие значения принимает признак guardian?
#print('\n', data['guardian'].unique())

#Подсчитайте количество учащихся с различными типами признака guardian
#print(data['guardian'].value_counts())

#Выделите только тех студентов, у которых опекуном является мать и которая работает учителем или на дому. 
#Подсчитайте общее количество таких студентов.
stud_mother = data['guardian'].isin(['mother'])
mother_homeTeach = data['Mjob'].isin(['teacher', 'at_home'])
#print(data[stud_mother & mother_homeTeach])
#print(data[stud_mother & mother_homeTeach].shape[0])

#Найдите количество студентов, у родителей которых нет никакого образования.
not_fedu = data['Fedu'].isin([0])
not_medu = data['Medu'].isin([0])
#print(data[not_fedu | not_medu].shape[0])

#общее употребление алкоголя в течение недели по формуле
data['alc'] = (5 * data['Dalc'] + 2 * data['Walc'])/7
#print(data)

#plt.figure(figsize=(10,7))
#data['alc'].hist()
#plt.xlabel('weekly alcohol consumption')
#plt.ylabel('number of students')
#plt.show()

#print(data['alc'].mean())

plt.figure(figsize=(10,7))
plt.title('Absences distribution')
data['absences'].hist()
plt.xlabel('absences')
plt.ylabel('number of students')
plt.show()
mean_abs = data['absences'].mean()
#print(mean_abs)

stud_nabs = data[data['absences'] < mean_abs]
stud_abs = data[data['absences'] >= mean_abs]
'''print(stud_nabs.shape[0])
print(stud_abs.shape[0])

print(stud_nabs['G3'].mean())
print(stud_abs['G3'].mean())'''

rom_yes = data['romantic'].isin(['yes'])
rom_yes = data[rom_yes]
mean_yresult = rom_yes['G3'].mean()
rom_no = data['romantic'].isin(['no'])
rom_no = data[rom_no]
mean_nresult = rom_no['G3'].mean()
#print('Result minus =', mean_nresult - mean_yresult)

data_by_school = data.groupby('school')
#print(data_by_school.describe())
#print(data_by_school.mean())

#Определить самое частое значение наличия внеклассных активностей (да или нет).
activate = data['activities'].isin(['yes'])
activate = data[activate]
nactivate = data['activities'].isin(['no'])
num_absence = activate.groupby('absences').count()['school']
num_absence = num_absence.drop([0])
max_absence = num_absence.idxmax()
#print('\n\n', num_absence, sep='')
#print('\n', 'Number absences at max stud = ', max_absence, sep='')




















