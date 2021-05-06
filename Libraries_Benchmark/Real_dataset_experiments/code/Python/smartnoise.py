import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import opendp.smartnoise.core as sn
import pandas as pd
epsilon = pd.read_pickle('epsilon.pkl')

#data_path = os.path.join("adult.csv")

NUM_TRIALS = 5
attribute = 'age'



if attribute == 'age':
    #data_path = os.path.join("E:\\MS_Thesis\\publication_stuff\\real_datasets\\adult.csv")
    data_path = "E:\\MS_Thesis\\publication_stuff\\real_datasets\\adult.csv"
    df = pd.read_csv(data_path)
    age = df.iloc[:, 0]
    maximum = 100.0
    minimum = 0.0
    dataset_rows = len(age)
    actual_count = len(age)
    actual_sum = np.sum(age)
    actual_mean = np.mean(age)
    actual_var = np.var(age)
    i=1

if attribute == 'hrs':
    data_path = os.path.join("E:\\MS_Thesis\\publication_stuff\\real_datasets\\adult.csv")
    df = pd.read_csv(data_path)
    df_hrs = df.iloc[:, 12]
    hrs = np.clip(df_hrs, a_max=80, a_min=None)
    maximum = 80.0
    minimum = 0.0
    dataset_rows = len(hrs)
    actual_count = len(hrs)
    actual_sum = np.sum(hrs)
    actual_mean = np.mean(hrs)
    actual_var = np.var(hrs)
    i=2

if attribute == 'absences':
    data_path = os.path.join("E:\\MS_Thesis\\publication_stuff\\real_datasets\\absences_education.csv")
    df = pd.read_csv(data_path)
    absences = df.iloc[:, 0]
    maximum = 93.0
    minimum = 0.0
    dataset_rows = len(absences)
    actual_count = len(absences)
    actual_sum = np.sum(absences)
    actual_mean = np.mean(absences)
    actual_var = np.var(absences)
    i=3

if attribute == 'grade':
    data_path = os.path.join("E:\\MS_Thesis\\publication_stuff\\real_datasets\\grade_education.csv")
    df = pd.read_csv(data_path)
    grade = df.iloc[:, 0]
    maximum = 20.0
    minimum = 0.0
    dataset_rows = len(grade)
    actual_count = len(grade)
    actual_sum = np.sum(grade)
    actual_mean = np.mean(grade)
    actual_var = np.var(grade)
    i=4


###############
### SUM #######
###############
scaled_error_list_sum = []
relative_error_list_sum = []
for eps in epsilon:
    print('calculating results for epsilon = {}'.format(eps))
    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data = sn.Dataset(path=data_path, column_names=var_name)
        d = sn.resize(sn.to_float(data[attribute]), data_lower=minimum, data_upper=maximum, number_rows=dataset_rows)
        samples = []
        for itr in range(NUM_TRIALS):
            samples.append(sn.dp_sum(data=d, privacy_usage={'epsilon': eps}).value)
        analysis.release()
        print(np.mean(samples))
        print(actual_sum)

        scaled_errors_per_itr = []
        relative_errors_per_itr = []
        for sam in samples:
            scaled_errors_per_itr.append(abs((actual_sum - sam) / dataset_rows))
            relative_errors_per_itr.append(abs((actual_sum - sam) / actual_sum))
        scaled_error_list_sum.append(np.std(scaled_errors_per_itr))
        relative_error_list_sum.append(np.mean(relative_errors_per_itr))
        print(relative_error_list_sum)
        print(scaled_error_list_sum)

#sum
guestFile1 = pd.DataFrame(scaled_error_list_sum)
guestFile2 = pd.DataFrame(relative_error_list_sum)

guestFile1.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\sum\\results_dataset_{i}\\std_scaled_error\\DP_std_scaled_error.csv".format(i=i), index=False)
guestFile2.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\sum\\results_dataset_{i}\\mean_relative_error\\DP_mean_relative_error.csv".format(i=i), index=False)


###############
### MEAN ######
###############
scaled_error_list_mean = []
relative_error_list_mean = []
for eps in epsilon:
    print('calculating results for epsilon = {}'.format(eps))
    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data = sn.Dataset(path=data_path, column_names=var_name)
        d = sn.resize(sn.to_float(data[attribute]), data_lower=minimum, data_upper=maximum, number_rows=dataset_rows)
        samples = []
        for itr in range(NUM_TRIALS):
            samples.append(sn.dp_mean(data=d, privacy_usage={'epsilon': eps}).value)
        analysis.release()
        print(np.mean(samples))
        print(actual_mean)

        scaled_errors_per_itr = []
        relative_errors_per_itr = []
        for sam in samples:
            scaled_errors_per_itr.append(abs((actual_mean - sam) / dataset_rows))
            relative_errors_per_itr.append(abs((actual_mean - sam) / actual_mean))
        scaled_error_list_mean.append(np.std(scaled_errors_per_itr))
        relative_error_list_mean.append(np.mean(relative_errors_per_itr))
        print(relative_error_list_mean)
        print(scaled_error_list_mean)

#mean
guestFile3 = pd.DataFrame(scaled_error_list_mean)
guestFile4 = pd.DataFrame(relative_error_list_mean)

guestFile3.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\mean\\results_dataset_{i}\\std_scaled_error\\DP_std_scaled_error.csv".format(i=i), index=False)
guestFile4.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\mean\\results_dataset_{i}\\mean_relative_error\\DP_mean_relative_error.csv".format(i=i), index=False)


###############
### Var #######
###############
scaled_error_list_var = []
relative_error_list_var = []
for eps in epsilon:
    print('calculating results for epsilon = {}'.format(eps))
    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data = sn.Dataset(path=data_path, column_names=var_name)
        d = sn.resize(sn.to_float(data[attribute]), data_lower=minimum, data_upper=maximum, number_rows=dataset_rows)
        samples = []
        for itr in range(NUM_TRIALS):
            samples.append(sn.dp_variance(data=d, privacy_usage={'epsilon': eps}).value)
        analysis.release()
        print(np.mean(samples))
        print(actual_var)

        scaled_errors_per_itr = []
        relative_errors_per_itr = []
        for sam in samples:
            scaled_errors_per_itr.append(abs((actual_var - sam) / dataset_rows))
            relative_errors_per_itr.append(abs((actual_var - sam) / actual_var))
        scaled_error_list_var.append(np.std(scaled_errors_per_itr))
        relative_error_list_var.append(np.mean(relative_errors_per_itr))
        print(relative_error_list_var)
        print(scaled_error_list_var)

#var
guestFile5 = pd.DataFrame(scaled_error_list_var)
guestFile6 = pd.DataFrame(relative_error_list_var)

guestFile5.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\var\\results_dataset_{i}\\std_scaled_error\\DP_std_scaled_error.csv".format(i=i), index=False)
guestFile6.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\var\\results_dataset_{i}\\mean_relative_error\\DP_mean_relative_error.csv".format(i=i), index=False)

###############
### Count #####
###############
scaled_error_list_count = []
relative_error_list_count = []
for eps in epsilon:
    print('calculating results for epsilon = {}'.format(eps))
    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data = sn.Dataset(path=data_path, column_names=var_name)
        d = sn.to_float(data[attribute])
        samples = []
        for itr in range(NUM_TRIALS):
            samples.append(sn.dp_count(data=d, privacy_usage={'epsilon': eps}).value)
        analysis.release()
        print(np.mean(samples))
        print(actual_count)

        scaled_errors_per_itr = []
        relative_errors_per_itr = []
        for sam in samples:
            scaled_errors_per_itr.append(abs((actual_count - sam) / dataset_rows))
            relative_errors_per_itr.append(abs((actual_count - sam) / actual_count))
        scaled_error_list_count.append(np.std(scaled_errors_per_itr))
        relative_error_list_count.append(np.mean(relative_errors_per_itr))
        print(relative_error_list_count)
        print(scaled_error_list_count)

#count
guestFile7 = pd.DataFrame(scaled_error_list_count)
guestFile8 = pd.DataFrame(relative_error_list_count)

guestFile7.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\var\\results_dataset_{i}\\std_scaled_error\\DP_std_scaled_error.csv".format(i=i), index=False)
guestFile8.to_csv("E:\\MS_Thesis\\publication_stuff\\refactored_code\\micro\\smartnoise\\var\\results_dataset_{i}\\mean_relative_error\\DP_mean_relative_error.csv".format(i=i), index=False)
