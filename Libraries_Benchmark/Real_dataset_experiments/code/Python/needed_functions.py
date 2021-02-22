import pandas as pd 
import time
import os
import psutil
import numpy as np 
import diffprivlib.tools as dpt
from pydp.algorithms import laplacian as dp
import opendp.smartnoise.core as sn
import math

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

### function to save results of error and scaled_error at desired place
def save_file_1(DP, library, query, output_folder, i, eps):
    guestFile = open("micro/{library}/{query}/results_dataset_{i}/{output_folder}/DP_{query}_eps_{eps}.csv".format(library=library, output_folder=output_folder, query=query, i=i, eps=eps),"a")
    guestFile.write(str (DP))
    guestFile.write("\n")
    guestFile.close()

### function to save results of mean/std error and mean/std scaled_error at desired place
def save_file_2(DP, library, query, output_folder, i):
    guestFile = open("micro/{library}/{query}/results_dataset_{i}/{output_folder}/DP_{output_folder}.csv".format(library=library, output_folder=output_folder, query=query, i=i),"a")
    guestFile.write(str (DP))
    guestFile.write("\n")
    guestFile.close()

### function to save Avg time results at desired place
def save_file_3(DP, library, query, i, param):
    guestFile = open("micro/{library}/{query}/results_dataset_{i}/AVG_{param}.csv".format(library=library, param=param, query=query, i=i),"a")
    guestFile.write(str(DP))
    guestFile.write("\n")
    guestFile.close()

### function to save error and scaled error
def save_file_4(library_name, dataset, DP_result, true_result, query_name, eps, i):
    # DP_result
    save_file_1(DP=DP_result, output_folder='dp', query=query_name, i=i, eps=eps, library=library_name)
    # error
    save_file_1(DP=true_result - DP_result, output_folder='error', query=query_name, i=i, eps=eps, library=library_name)
    # relative_error
    save_file_1(DP=(true_result - DP_result)/true_result, output_folder='relative_error', query=query_name, i=i, eps=eps, library=library_name)
    # scaled error
    save_file_1(DP=(true_result - DP_result)/len(dataset), output_folder='scaled_error', query=query_name, i=i, eps=eps, library=library_name)
    
# function to save mean_error, mean_scaled_error, std_error, std_scaled_error, time, memory. 
def errors_calculation(library, err, relative_err, scaled_err, time_list, memory, query, i):
    # Mean error
    #print(np.sum(err)/100)
    save_file_2(DP=np.sum(err)/500, output_folder='mean_error', query=query, i=i, library=library)
    # Mean scaled_error
    #print('MEAN SCALED ERROR = {}'.format(np.sum(scaled_err)/500))
    save_file_2(DP=np.sum(scaled_err)/500, output_folder='mean_scaled_error', query=query, i=i, library=library)
    # Std error
    save_file_2(DP=stdev(err), output_folder='std_error', query=query, i=i, library=library)
    # Std scaled_error
    save_file_2(DP=stdev(scaled_err), output_folder='std_scaled_error', query=query, i=i, library=library)
    print('STD SCALED ERROR = {}'.format(stdev(scaled_err)))
    # Mean relative error
    print('MEAN RELATIVE ERROR = {}'.format(np.sum(relative_err)/500))
    save_file_2(DP=np.sum(relative_err)/500, output_folder='mean_relative_error', query=query, i=i, library=library)
    # Std relative error
    save_file_2(DP=np.sum(relative_err)/500, output_folder='std_relative_error', query=query, i=i, library=library)
    # time
    save_file_3(DP=np.mean(time_list)*1000, query=query, i=i, param='time', library=library)
    print('Time consumed in ms = {}'.format(np.mean(time_list)*1000))
    # memory
    save_file_3(DP=np.mean(memory), query=query, i=i, param='memory', library=library)
    print('Memory consumed in bytes = {}'.format(np.mean(memory)))

#######################################
#          IBM-diffprivlib            #
#######################################
class diffprivlib_attribute:
    name = 'diffprivlib'
    distribution = 'dataset'
    epsilon = 'eps'
    count_query = dpt.count_nonzero
    sum_query = dpt.sum
    true_sum = np.sum
    mean_query = dpt.mean
    true_mean = np.mean
    var_query = dpt.var
    true_var = np.var

def diffprivlib_count(library_name, number_of_experiments, eps, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # Count query
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = getattr(eval('{library}_attribute'.format(library=library_name)),'count_query')(dataset, eps)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = len(dataset)
        #print(DP_result)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        #print('error = {}'.format(true_result-DP_result))
        #print('relative error = {}'.format((true_result-DP_result)/true_result))
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
def diffprivlib_all(library_name, number_of_experiments, eps, bounds, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = getattr(eval('{library}_attribute'.format(library=library_name)),'{query}_query'.format(query=query_name))(dataset, eps, bounds=bounds)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = getattr(eval('{library}_attribute'.format(library=library_name)),'true_{query}'.format(query=query_name))(dataset)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        #print('error = {}'.format(true_result-DP_result))
        #print('relative error = {}'.format((true_result-DP_result)/true_result))
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
###########################################################################################################


#######################################
#               PyDP                  #
#######################################

class pydp_attribute:
    name = 'pydp'
    distribution = 'dataset'
    epsilon = 'eps'
    count_query = dp.Count
    sum_query = dp.BoundedSum
    true_sum = np.sum
    mean_query = dp.BoundedMean
    true_mean = np.mean
    var_query = dp.BoundedVariance
    true_var = np.var
    std_query = dp.BoundedStandardDeviation
    true_std = np.std

def pydp_count(library_name, number_of_experiments, eps, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # Count query
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        x = getattr(eval('{library}_attribute'.format(library=library_name)),'count_query')(epsilon=eps, dtype='float')
        DP_result = x.quick_result(list(dataset))
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = len(dataset)
        #print(DP_result)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
def pydp_all(library_name, number_of_experiments, eps, minimum, maximum, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        x = getattr(eval('{library}_attribute'.format(library=library_name)),'{query}_query'.format(query=query_name))(eps, minimum, maximum, dtype='float')
        DP_result = x.quick_result(list(dataset))
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = getattr(eval('{library}_attribute'.format(library=library_name)),'true_{query}'.format(query=query_name))(dataset)
        DP.append(DP_result)
        #print(DP_result)
        #print(true_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
###########################################################################################################


#######################################
#           Smartnoise                #
#######################################

##############   Analysis Functions   ###################
def smartnoise_analysis_count(dataset_folder_path, attribute, dataset, i, eps):
    if attribute == 'age':
        dataset_column = 'age_adult.csv'
    if attribute == 'hrs':
        dataset_column = 'hrs_adult.csv'

    if attribute == 'absences': 
        dataset_column = 'absences_education.csv'   
    if attribute == 'grade':
        dataset_column = 'grade_education.csv'
    
    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data_path = dataset_column
        data = sn.Dataset(path = data_path, column_names = var_name)
        data_in_float = sn.to_float(data[attribute])
        dp = sn.dp_count(data=data_in_float, privacy_usage={'epsilon':eps})
    analysis.release()
    return dp.value

def smartnoise_analysis_sum(dataset_folder_path, dataset_rows, attribute, i, eps, minimum, maximum, query_name):
    if attribute == 'age':
        dataset_column = 'age_adult.csv'
    if attribute == 'hrs':
        dataset_column = 'hrs_adult.csv'

    if attribute == 'absences':
        dataset_column = 'absences_education.csv'
    if attribute == 'grade':
        dataset_column = 'grade_education.csv'

    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data_path = dataset_column
        dataset = sn.Dataset(path = data_path, column_names = var_name)
        data_in_float = sn.to_float(dataset[attribute])
        data_in_float = sn.impute(data = data_in_float, lower = minimum, upper = maximum)
        data_in_float = sn.clamp(data_in_float, lower=minimum, upper=maximum)
        data_in_float = sn.resize(data_in_float, number_rows=dataset_rows, lower=minimum, upper=maximum)
        dp = sn.dp_sum(data=data_in_float, privacy_usage={'epsilon':eps})
    analysis.release()
    return dp.value

def smartnoise_analysis_mean(dataset_folder_path, dataset_rows, attribute, i, eps, minimum, maximum, query_name):

    if attribute == 'age':
        dataset_column = 'age_adult.csv'
    if attribute == 'hrs':
        dataset_column = 'hrs_adult.csv'

    if attribute == 'absences':
        dataset_column = 'absences_education.csv'
    if attribute == 'grade':
        dataset_column = 'grade_education.csv'

    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data_path = dataset_column
        dataset = sn.Dataset(path = data_path, column_names = var_name)
        data_in_float = sn.to_float(dataset[attribute])
        data_in_float = sn.impute(data = data_in_float, lower = minimum, upper = maximum)
        data_in_float = sn.clamp(data_in_float, lower=minimum, upper=maximum)
        data_in_float = sn.resize(data_in_float, number_rows=dataset_rows, lower=minimum, upper=maximum)
        dp = sn.dp_mean(data=data_in_float, privacy_usage={'epsilon':eps})
    analysis.release()
    return dp.value

def smartnoise_analysis_var(dataset_folder_path, dataset_rows, attribute, i, eps, minimum, maximum, query_name):

    if attribute == 'age':
        dataset_column = 'age_adult.csv'
    if attribute == 'hrs':
        dataset_column = 'hrs_adult.csv'

    if attribute == 'absences':
        dataset_column = 'absences_education.csv'
    if attribute == 'grade':
        dataset_column = 'grade_education.csv'


    with sn.Analysis(neighboring='substitute') as analysis:
        var_name = [attribute]
        data_path = dataset_column
        dataset = sn.Dataset(path = data_path, column_names = var_name)
        data_in_float = sn.to_float(dataset[attribute])
        data_in_float = sn.impute(data = data_in_float, lower = minimum, upper = maximum)
        data_in_float = sn.clamp(data_in_float, lower=minimum, upper=maximum)
        data_in_float = sn.resize(data_in_float, number_rows=dataset_rows, lower=minimum, upper=maximum)
        dp = sn.dp_variance(data=data_in_float, privacy_usage={'epsilon':eps})
    analysis.release()
    return dp.value
####################################

def smartnoise_count(library_name, dataset_folder_path, attribute, number_of_experiments, eps, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # Count query
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = smartnoise_analysis_count(dataset_folder_path=dataset_folder_path, attribute=attribute, dataset=dataset, i=i, eps=eps)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = len(dataset)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
def smartnoise_sum(library_name, dataset_folder_path, number_of_experiments, attribute, eps, minimum, maximum, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = smartnoise_analysis_sum(dataset_folder_path=dataset_folder_path, dataset_rows=len(dataset), attribute=attribute, query_name=query_name, i=i, eps=eps, minimum=minimum, maximum=maximum)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = np.sum(dataset)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)

 
def smartnoise_mean(library_name, dataset_folder_path, number_of_experiments, attribute, eps, minimum, maximum, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = smartnoise_analysis_mean(dataset_folder_path=dataset_folder_path, dataset_rows=len(dataset), attribute=attribute, query_name=query_name, i=i, eps=eps, minimum=minimum, maximum=maximum)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = np.mean(dataset)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
 
 
def smartnoise_var(library_name, dataset_folder_path, number_of_experiments, attribute, eps, minimum, maximum, dataset, query_name, i):
    DP = []
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        # query run time
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        DP_result = smartnoise_analysis_var(dataset_folder_path=dataset_folder_path, dataset_rows=len(dataset), attribute=attribute, query_name=query_name, i=i, eps=eps, minimum=minimum, maximum=maximum)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = np.var(dataset)
        DP.append(DP_result)
        err.append(true_result - DP_result)
        relative_err.append((true_result - DP_result)/true_result)
        scaled_err.append((true_result - DP_result)/len(dataset))
        
        save_file_4(library_name=library_name, dataset=dataset, DP_result=DP_result, true_result=true_result, query_name=query_name, eps=eps, i=i)
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=library_name)
  
###########################################################################################################

#######################################
#           additive_noise            #
#######################################

class additive_noise_attribute:
    name = 'additive_noise'
    distribution = 'dataset'
    epsilon = 'eps'
    true_count = len
    true_sum = np.sum
    true_mean = np.mean
    true_var = np.var

def additive_noise_all(experiment_name, number_of_experiments, dataset, query_name, i):
    err = []
    relative_err = []
    scaled_err = []
    time_list = []
    memory_list = []
    for iteration in range(number_of_experiments):
        process = psutil.Process(os.getpid())
        begin_time = time.time() 
        #error = np.random.uniform((eval('true_'+query_name)(dataset)) * (-0.1), (eval('true_'+query_name)(dataset)) * 0.1, 500)
        error = getattr(eval('{library}_attribute'.format(library=experiment_name)),'true_{query}'.format(query=query_name))(dataset) + (getattr(eval('{library}_attribute'.format(library=experiment_name)),'true_{query}'.format(query=query_name))(dataset) * np.random.uniform(-0.1, 0.1)) - getattr(eval('{library}_attribute'.format(library=experiment_name)),'true_{query}'.format(query=query_name))(dataset)
        time_list.append(time.time() - begin_time) # running time
        memory_list.append(process.memory_info().rss) # memory consumption
        true_result = getattr(eval('{library}_attribute'.format(library=experiment_name)),'true_{query}'.format(query=query_name))(dataset)
        err.append(error)
        relative_err.append(error/true_result)
        scaled_err.append(error/len(dataset))
    errors_calculation(err=err, relative_err=relative_err, scaled_err=scaled_err, time_list=time_list, memory=memory_list, query=query_name, i=i, library=experiment_name)
        
###########################################################################################################

