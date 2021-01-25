import opendp.smartnoise.core as sn
import sys
import math
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from needed_functions import *
epsilon = pd.read_pickle('epsilon.pkl')

library_name = 'smartnoise'

def smartnoise_single_query(dataset_folder_path, number_of_csv_files, query_name, number_of_experiments):

    for i in range(number_of_csv_files):
        df = pd.read_csv(dataset_folder_path+"dataset_{}.csv".format(i)) # creating dataframs by using pandas for all datasets
        normal_distribution = [df] # making all values positive with "abs"
        maximum = np.max(normal_distribution) * 1.01
        minimum = np.min(normal_distribution) * 0.99

        for eps in epsilon:
            if query_name == 'count':
                print("Count results for dataset = {i} and for epsilon = {eps}".format(i=i, eps=eps))
                smartnoise_count(library_name=library_name, dataset_folder_path=dataset_folder_path, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i)
            if query_name == 'sum': 
                print("{library} results for dataset = {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
                smartnoise_sum(library_name=library_name, dataset_folder_path=dataset_folder_path, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i, minimum=minimum, maximum=maximum)
            if query_name == 'mean': 
                print("{library} results for dataset = {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
                smartnoise_mean(library_name=library_name, dataset_folder_path=dataset_folder_path, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i, maximum=maximum, minimum=minimum)
            if query_name == 'variance': 
                print("{library} results for dataset = {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
                smartnoise_var(library_name=library_name, dataset_folder_path=dataset_folder_path, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=df, query_name=query_name, i=i, maximum=maximum, minimum=minimum)
     
#smartnoise_single_query(dataset_folder_path= 'E:\\MS_Thesis\\publication_stuff\\car_datasets\\gaussian_datasets\\', 
 #           number_of_csv_files=27, query_name='count', number_of_experiments=50)
