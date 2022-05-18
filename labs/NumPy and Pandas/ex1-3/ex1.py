import numpy as np

marks = np.loadtxt("data_lab1.txt")

#Сколько студентов в группе семинариста?
num_studs = len(marks[:, 0])
print("Number of students:", num_studs)

#Каков максимальный балл за первую проверочную?
max_mark = np.max(marks[:, 0])
print("Max mark =", max_mark)
marks[:, 0] = (marks[:, 0] / max_mark) * 10

#Вычислите накопленные оценки и добавьте их в последний столбец
weights = [0.3, 0.4, 0.3]
mean_verif = np.mean(marks[:, :3], axis=1) * weights[0]
mean_home = np.mean(marks[:, 3:6], axis=1) * weights[1]
mean_coll = marks[:, 6] * weights[2]
accum = (mean_verif + mean_home + mean_coll).reshape(-1, 1)
marks = np.hstack((marks, accum))
#print(accum)
#print(mean_verif, mean_home, mean_coll, accum, sep='\n')
#print(marks)

#Сколько в группе студентов с накопленной оценкой 0?
stupid = np.sum(marks[:, 7] == 0)
#print(stupid)

#Автомат получат студенты, у которых накопленная оценка больше 7
auto = (np.multiply(marks[:, 7] > 7, 1)).reshape(-1, 1)
marks = np.hstack((marks, auto))
#print(marks[:, 6:9])

#Студенты, которые будут освобождены от задач на экзамене
sort_marks = np.argsort(-marks[:, 7])
new_arr = marks[sort_marks]
new_arr = new_arr[0:int(num_studs/2), :]
#print(new_arr)

#Сложность заданий
weights = np.array([1.]*7+[2.]*4+[3.]*7+[4.]*(marks.shape[0]-18))
weights = weights/np.sum(weights)
weights = weights.reshape(-1, 1)
#print(weights)
weights_exercise = np.sum(marks * weights, axis=0)

print(weights_exercise)


