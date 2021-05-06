from pydp.algorithms import laplacian as dp
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from utils import *
epsilon = pd.read_pickle('~/publication/files/epsilon.pkl')

library_name = 'pydp'

def openmind_pydp_real_dataset(dataset_folder_path, attribute, query_name, number_of_experiments):

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
        maximum = max(df)
        minimum = 0.0
        i = 2

    # education dataset
    if attribute == 'absences':
        df1 = pd.read_csv(dataset_folder_path+"student-mat.csv", sep=";")
        df2 = pd.read_csv(dataset_folder_path+"student-por.csv", sep=";")
        frames = [df1, df2]
        df_education = pd.concat(frames)
        df = df_education.absences
        maximum = 93.0
        minimum = 0.0
        i = 3
    if attribute == 'grade':
        df1 = pd.read_csv(dataset_folder_path+"student-mat.csv", sep=";")
        df2 = pd.read_csv(dataset_folder_path+"student-por.csv", sep=";")
        frames = [df1, df2]
        df_education = pd.concat(frames)
        df = df_education.G3
        maximum = 20.0
        minimum = 0.0
        i = 4


    for eps in epsilon:
         if query_name == 'count':
            print("Count results for dataset = {i} and for epsilon = {eps}".format(i=i, eps=eps))
            pydp_count(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i)
         else:
            print("{query} {library} results for dataset = {i} and for epsilon = {eps}".format(query=query_name, library=library_name, i=i, eps=eps))
            pydp_all(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i, minimum=int(minimum), maximum=int(maximum))

                
#openmind_pydp_real_dataset(dataset_folder_path= '~/publication/files/real_datasets/', attribute='absences', query_name='var', number_of_experiments=50)
                
