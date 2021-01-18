from needed_functions import *
import numpy as np 
import pandas as pd 
import time
import os
import psutil
from guppy import hpy; h=hpy()
epsilon = pd.read_pickle('epsilon.pkl')

experiment_name = 'additive_noise'
def additive_noise_single_query(dataset_folder_path, number_of_csv_files, query_name, number_of_experiments):

    for i in range(number_of_csv_files):
        
        print("{query} results for dataset = {i} ".format(query=query_name, i=i))
        df = pd.read_csv(dataset_folder_path+"dataset_{}.csv".format(i)) # creating dataframs by using pandas for all datasets
        normal_distribution = [df] # making the series a list for function compatibility
        additive_noise_all(experiment_name=experiment_name, number_of_experiments=number_of_experiments, normal_distribution=normal_distribution, query_name=query_name, i=i)
