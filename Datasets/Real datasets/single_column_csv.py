import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import operator
import numbers
import csv
import matplotlib.pyplot as plt


df = pd.read_csv('~/publication/files/real_datasets/adult.csv', sep=',')

age_list = []
for a in df.iloc[:,0]:
    age_list.append(a)

print(len(age_list))
'''
hrs_list = []
for g in df.iloc[:,12]:
    hrs_list.append(g)
clipped_hrs_list = np.clip(hrs_list, a_max=80, a_min=None)
df_age = pd.DataFrame(age_list, columns=['age'])
df_hrs = pd.DataFrame(clipped_hrs_list, columns=['hrs'])

df_age.to_csv('~/publication/real_dataset_analysis/chorus_main_real_datasets/real_datasets/age_adult.csv', index=False)
df_hrs.to_csv('~/publication/real_dataset_analysis/chorus_main_real_datasets/real_datasets/hrs_adult.csv', index=False)


df_age.to_csv('~/publication/files/real_datasets/age_adult.csv', index=False)
df_hrs.to_csv('~/publication/files/real_datasets/hrs_adult.csv', index=False)
'''
'''
df1 = pd.read_csv("~/publication/files/real_datasets/student-mat.csv", sep=";")
df2 = pd.read_csv("~/publication/files/real_datasets/student-por.csv", sep=";")
frames = [df1, df2]
df = pd.concat(frames)

#df = pd.read_csv('~/publication/files/real_datasets/education.csv', sep=',')

abs_list = []
for a in df.absences:
    abs_list.append(a)

grade_list = []
for g in df.G3:
    grade_list.append(g)

df_abs = pd.DataFrame(abs_list, columns=['absences'])
df_grade = pd.DataFrame(grade_list, columns=['grade'])

print(len(abs_list))
df_abs.to_csv('~/publication/real_dataset_analysis/absences_education.csv', index=False)
df_grade.to_csv('~/publication/real_dataset_analysis/grade_education.csv', index=False)
'''
