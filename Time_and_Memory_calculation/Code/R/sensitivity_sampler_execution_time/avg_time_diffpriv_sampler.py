import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path_to_micro_folder = 'E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\micro_13April_2021'
diffpriv_simple_2 = pd.read_csv(path_to_micro_folder + '\\diffpriv_simple\\mean\\results_dataset_0\\execution_time.csv')
diffpriv_simple_3 = pd.read_csv(path_to_micro_folder + '\\diffpriv_simple\\mean\\results_dataset_1\\execution_time.csv')
diffpriv_simple_4 = pd.read_csv(path_to_micro_folder + '\\diffpriv_simple\\mean\\results_dataset_2\\execution_time.csv')

diffpriv_2 = pd.read_csv(path_to_micro_folder + '\\diffpriv\\mean\\results_dataset_0\\execution_time.csv')
diffpriv_3 = pd.read_csv(path_to_micro_folder + '\\diffpriv\\mean\\results_dataset_1\\execution_time.csv')
diffpriv_4 = pd.read_csv(path_to_micro_folder + '\\diffpriv\\mean\\results_dataset_2\\execution_time.csv')

print('Scale = 1000')
print('diffpriv (without sampler) = {}'.format(np.mean(diffpriv_simple_2.iloc[:,0])))
print('diffpriv (with sampler) = {}'.format(np.mean(diffpriv_2.iloc[:,0])))
print('Difference = {}'.format(np.mean(diffpriv_2.iloc[:,0] - np.mean(diffpriv_simple_2.iloc[:,0]))))
print('Division = {}'.format(np.mean(diffpriv_2.iloc[:,0] / np.mean(diffpriv_simple_2.iloc[:,0]))))

print('Scale = 10000')
print('diffpriv (without sampler) = {}'.format(np.mean(diffpriv_simple_3.iloc[:,0])))
print('diffpriv (with sampler) = {}'.format(np.mean(diffpriv_3.iloc[:,0])))
print('Difference = {}'.format(np.mean(diffpriv_3.iloc[:,0] - np.mean(diffpriv_simple_3.iloc[:,0]))))
print('Division = {}'.format(np.mean(diffpriv_3.iloc[:,0] / np.mean(diffpriv_simple_3.iloc[:,0]))))

print('Scale = 100000')
print('diffpriv (without sampler) = {}'.format(np.mean(diffpriv_simple_4.iloc[:,0])))
print('diffpriv (with sampler) = {}'.format(np.mean(diffpriv_4.iloc[:,0])))
print('Difference = {}'.format(np.mean(diffpriv_4.iloc[:,0] - np.mean(diffpriv_simple_4.iloc[:,0]))))
print('Division = {}'.format(np.mean(diffpriv_4.iloc[:,0] / np.mean(diffpriv_simple_4.iloc[:,0]))))
