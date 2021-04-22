import opendp.smartnoise.core as sn
import sys
import math
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from needed_functions import *
epsilon = pd.read_pickle('~/publication/files/epsilon.pkl')
#epsilon = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 20.0]
library_name = 'smartnoise'

def smartnoise_real_dataset(dataset_folder_path, attribute, query_name, number_of_experiments):

    # adult dataset
    if attribute == 'age':
        df_adult = pd.read_csv(dataset_folder_path+"adult.data", sep=',', header=None)
        df = df_adult.iloc[:,0]
        maximum = 100.0
        minimum = 0.0
        i = 1
    if attribute == 'hrs':
        df_adult = pd.read_csv(dataset_folder_path+"adult.data", sep=',', header=None)
        df_hrs = df_adult.iloc[:,12]
        df = np.clip(df_hrs, a_max=80, a_min=None)
        maximum = float(max(df))
        minimum = 0.0
        i = 2

    # education dataset
    if attribute == 'absences':
        df1 = pd.read_csv('~/publication/files/real_datasets/student-mat.csv', sep=';')
        df2 = pd.read_csv('~/publication/files/real_datasets/student-por.csv', sep=';')
        frames = [df1, df2]
        df_education = pd.concat(frames)
        #df_education = pd.read_csv(dataset_folder_path+"education.csv", sep=";")

        df = df_education.absences
        maximum = 93.0
        minimum = 0.0
        i = 3
    if attribute == 'grade':
        df1 = pd.read_csv('~/publication/files/real_datasets/student-mat.csv', sep=';')
        df2 = pd.read_csv('~/publication/files/real_datasets/student-por.csv', sep=';')
        frames = [df1, df2]
        df_education = pd.concat(frames)
        #df_education = pd.read_csv(dataset_folder_path+"education.csv", sep=";")

        df = df_education.G3
        maximum = 20.0
        minimum = 0.0
        i = 4


    for eps in epsilon:
        if query_name == 'count': 
            print("COUNT QUERY Smartnoise results for attribute, saving in result_dataset {i} and for epsilon = {eps}".format(i=i, eps=eps))
            smartnoise_count(library_name=library_name, dataset_folder_path=dataset_folder_path, attribute=attribute, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i)
        if query_name == 'sum': 
            print("SUM QUERY {library} results for attribute, saving in result_dataset {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
            smartnoise_sum(library_name=library_name, dataset_folder_path=dataset_folder_path, attribute=attribute, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i, minimum=minimum, maximum=maximum)
        if query_name == 'mean': 
            print("MEAN QUERY {library} results for attribute, saving in result_dataset {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
            smartnoise_mean(library_name=library_name, dataset_folder_path=dataset_folder_path, attribute=attribute, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i, maximum=maximum, minimum=minimum)
        if query_name == 'var': 
            print("VAR QUERY {library} results for attribute, saving in result_dataset {i} for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
            smartnoise_var(library_name=library_name, dataset_folder_path=dataset_folder_path, attribute=attribute, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name='variance', i=i, maximum=maximum, minimum=minimum)
     
#smartnoise_real_dataset(dataset_folder_path= '~/publication/files/real_datasets/', attribute='grade', query_name='sum', number_of_experiments=50)
