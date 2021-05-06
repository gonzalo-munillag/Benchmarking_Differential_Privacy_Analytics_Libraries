from diffprivlib . mechanisms import Laplace
import diffprivlib.tools as dpt
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from utils import *
epsilon = pd.read_pickle('~/publication/files/epsilon.pkl')

library_name = 'diffprivlib'

def diffprivlib_single_query(dataset_folder_path, number_of_csv_files, query_name, number_of_experiments):

    for i in range(number_of_csv_files):
        df = pd.read_csv(dataset_folder_path+"dataset_{}.csv".format(i), header=None) # creating dataframs by using pandas for all datasets
        normal_distribution = [df] 
        maximum = np.max(df)
        minimum = np.min(df)

        for eps in epsilon:
            if query_name == 'count':
                print("count results for dataset = {i} and for epsilon = {eps}".format(i=i, eps=eps))
                diffprivlib_count(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i)
            else:
                print("{library} results for dataset = {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
                diffprivlib_all(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i, bounds=(minimum, maximum))

#diffprivlib_single_query(dataset_folder_path= '~/publication/files/gaussian_datasets/', 
 #           number_of_csv_files=27, query_name='var', number_of_experiments=1)
