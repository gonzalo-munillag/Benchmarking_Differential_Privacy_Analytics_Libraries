from diffprivlib . mechanisms import Laplace
import diffprivlib.tools as dpt
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from utils import *
epsilon = pd.read_pickle('~/publication/files/epsilon.pkl')
#epsilon = [50.0, 60.0]
library_name = 'diffprivlib'

def diffprivlib_real_dataset(dataset_folder_path, attribute, query_name, number_of_experiments):
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
            print("count results for adult dataset = {att} and for epsilon = {eps}".format(att=attribute, eps=eps))
            diffprivlib_count(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i)
        else:
            print("{library} results for adult dataset = {att} and for epsilon = {eps}".format(library=library_name, att=attribute, eps=eps))
            diffprivlib_all(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, dataset=df, query_name=query_name, i=i, bounds=(minimum, maximum))

#diffprivlib_real_dataset(dataset_folder_path= '~/publication/files/real_datasets/', attribute='absences', query_name='sum', number_of_experiments=50)
