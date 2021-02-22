import opendp.whitenoise.core as wn
#import opendp.smartnoise.core as wn
import sys
import math
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
epsilon = pd.read_pickle('~/publication/files/epsilon.pkl')

dataset_num = 1

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


##############   Analysis Functions   ###################
def smartnoise_analysis_count(dataset_folder_path, i, eps):
    with wn.Analysis(neighboring='substitute', dynamic=True) as analysis:
        var_name = ['normal_distribution']
        data_path = 'dataset_{}.csv'.format(i)
        data = wn.Dataset(path = data_path, column_names = var_name)
        data_in_float = wn.to_float(data['normal_distribution'])
        dp = wn.dp_count(data=data_in_float, privacy_usage={'epsilon':eps})
    analysis.release()
    return dp.value


std_dp_result = []
std_error = []
std_scaled_error = []
for eps in epsilon:
    dp_results_list = []
    error = []
    scaled_error = []
    for repeat in range(100):
        r = smartnoise_analysis_count(dataset_folder_path = "~/publication/single_query_analysis", i=dataset_num, eps=eps)
        dp_results_list.append(r)
        true_count = 1000
        error.append(true_count - r)
        scaled_error.append((true_count - r)/true_count)

    std_dp_result.append(stdev(dp_results_list))
    std_error.append(stdev(error))
    std_scaled_error.append(stdev(scaled_error))

print(std_scaled_error)
df1 = pd.DataFrame(std_dp_result)
df2 = pd.DataFrame(std_error)
df3 = pd.DataFrame(std_scaled_error)

df1.to_csv('~/publication/single_query_analysis/whitenoise_results/dataset_{dataset}/std_dp_result.csv'.format(dataset=dataset_num), index=False)
df2.to_csv('~/publication/single_query_analysis/whitenoise_results/dataset_{dataset}/std_error.csv'.format(dataset=dataset_num), index=False)
df3.to_csv('~/publication/single_query_analysis/whitenoise_results/dataset_{dataset}/std_scaled_error.csv'.format(dataset=dataset_num), index=False)
#plt.plot(epsilon, std_dp_result)
#plt.show()


