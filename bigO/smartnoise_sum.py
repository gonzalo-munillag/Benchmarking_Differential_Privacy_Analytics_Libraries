import pandas as pd
import time
import os
import psutil
import numpy as np
import opendp.smartnoise.core as sn
import math


number_of_csv_files = 4
number_of_experiments = 1
epsilon = [0.1, 1.0, 10.0]

for i in range(number_of_csv_files):
    print('Dataset = {i}'.format(i=i))
    df = pd.read_csv("dataset_{}.csv".format(i), header=None) # creating dataframs by using pandas for all datasets
    normal_distribution = [df] # making all values positive with "abs"
    maximum = np.max(df)
    minimum = np.min(df)

    for eps in epsilon:
        time_list = []
        memory_list = []
        for itr in range(number_of_experiments):
            process = psutil.Process(os.getpid())
            begin_time = time.time()
            with sn.Analysis(neighboring='substitute') as analysis:
                var_name = ['normal_distribution']
                data_path = "dataset_{}.csv".format(i)
                data = sn.Dataset(path = data_path, column_names = var_name)
                data_in_float = sn.to_float(data['normal_distribution'])
                data_in_float = sn.impute(data = data_in_float, lower = minimum, upper = maximum)
                data_in_float = sn.clamp(data_in_float, lower=minimum, upper=maximum)
                data_in_float = sn.resize(data_in_float, number_rows=len(df), lower=minimum, upper=maximum)
                dp = sn.dp_sum(data=data_in_float, privacy_usage={'epsilon':eps})
            analysis.release()
            time_list.append(time.time() - begin_time) # running time
            memory_list.append(process.memory_info().rss) # memory consumption
        print('(Smartnoise) Sum Query for Epsilon = {e} mean time is = {t} and mean memory is = {m}'.format(e = eps, t=time_list, m=memory_list))


        df_time = pd.DataFrame(time_list)
        df_memory = pd.DataFrame(memory_list)
        df_time.to_csv('~/publication/bigO/results/smartnoise/sum_time_eps_{eps}_dataset_{i}.csv'.format(eps=eps, i=i), index = False)
        df_memory.to_csv('~/publication/bigO/results/smartnoise/sum_mem_eps_{eps}_dataset_{i}.csv'.format(eps=eps, i=i), index = False)



