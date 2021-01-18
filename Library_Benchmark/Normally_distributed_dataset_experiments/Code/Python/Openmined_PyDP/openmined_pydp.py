from pydp.algorithms import laplacian as dp
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from needed_functions import *
epsilon = pd.read_pickle('epsilon.pkl')

library_name = 'pydp'

def openmind_pydp_single_query(dataset_folder_path, number_of_csv_files, query_name, number_of_experiments):

    for i in range(number_of_csv_files):
        
        df = pd.read_csv(dataset_folder_path+"dataset_{}.csv".format(i)) # creating dataframs by using pandas for all datasets
        normal_distribution = [df] # making the series a list for function compatibility
        maximum = np.mean(normal_distribution) + std_val[i] * np.std(normal_distribution)
        minimum = np.mean(normal_distribution) - std_val[i] * np.std(normal_distribution)
        
        for eps in epsilon:
            
            if query_name == 'count':
                
                print("Count results for dataset = {i} and for epsilon = {eps}".format(i=i, eps=eps))
                pydp_count(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=normal_distribution, query_name=query_name, i=i)
            
            else:
                
                print("{library} results for dataset = {i} and for epsilon = {eps}".format(library=library_name, i=i, eps=eps))
                pydp_all(library_name=library_name, number_of_experiments=number_of_experiments, eps=eps, normal_distribution=normal_distribution, query_name=query_name, i=i, minimum=int(minimum), maximum=int(maximum))
              
