import pandas as pd
import time
import os
import psutil
import numpy as np
import diffprivlib.tools as dpt


number_of_csv_files = 4
number_of_experiments = 1
epsilon = [0.1, 1.0, 10.0]

for i in range(number_of_csv_files):
    print('Dataset = {}'.format(i))
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
            DP_result = dpt.count_nonzero(normal_distribution, eps)
            time_list.append(time.time() - begin_time) # running time in sec
            memory_list.append(process.memory_info().rss) # memory consumption in bytes
        print('(IBM_diffprivlib) Count query for Epsilon = {e} mean time is = {t} and mean memory is = {m}'.format(e = eps, t=time_list, m=memory_list))

        df_time = pd.DataFrame(time_list)
        df_memory = pd.DataFrame(memory_list)
        df_time.to_csv('~/publication/bigO/results/diffprivlib/count_time_eps_{eps}_dataset_{i}.csv'.format(eps=eps, i=i), index = False)
        df_memory.to_csv('~/publication/bigO/results/diffprivlib/count_mem_eps_{eps}_dataset_{i}.csv'.format(eps=eps, i=i), index = False) 

