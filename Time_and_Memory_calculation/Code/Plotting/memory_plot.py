import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pandas as pd
import csv
import matplotlib.legend as mlegend
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

result_folder = "E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\real_dataset_micro\\bigO\\micro_bigO_20thMAR_2021_v2\\27thApril"
diffpriv_folder = 'E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\real_dataset_micro\\bigO\\micro_bigO_20thMar_2021_v2\\27thApril\\AVG_memory_Diffpriv'
query = 'mean'

diffprivlib_1 = []
diffprivlib_2 = []
diffprivlib_3 = []
diffprivlib_4 = []
diffprivlib_5 = []
diffprivlib_6 = []
diffprivlib_7 = []

smartnosie_1 = []
smartnosie_2 = []
smartnosie_3 = []
smartnosie_4 = []
smartnosie_5 = []
smartnosie_6 = []
smartnosie_7 = []

pydp_1 = []
pydp_2 = []
pydp_3 = []
pydp_4 = []
pydp_5 = []
pydp_6 = []
pydp_7 = []

diffpriv_1 = []
diffpriv_2 = []
diffpriv_3 = []
diffpriv_4 = []
diffpriv_5 = []
diffpriv_6 = []
diffpriv_7 = []

my_chorus_1 = []
my_chorus_2 = []
my_chorus_3 = []
my_chorus_4 = []
my_chorus_5 = []
my_chorus_6 = []
my_chorus_7 = []

epsilon = [0.1, 1.0, 10.0]
epsilon_diffpriv = [0.1, 1, 10]


diffpriv_0_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_0.csv'.format(query=query), header=None)
diffpriv_0_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_0.csv'.format(query=query), header=None)
diffpriv_0_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_0.csv'.format(query=query), header=None)

diffpriv_1_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_1.csv'.format(query=query), header=None)
diffpriv_1_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_1.csv'.format(query=query), header=None)
diffpriv_1_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_1.csv'.format(query=query), header=None)

diffpriv_2_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_2.csv'.format(query=query), header=None)
diffpriv_2_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_2.csv'.format(query=query), header=None)
diffpriv_2_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_2.csv'.format(query=query), header=None)

diffpriv_3_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_3.csv'.format(query=query), header=None)
diffpriv_3_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_3.csv'.format(query=query), header=None)
diffpriv_3_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_3.csv'.format(query=query), header=None)

diffpriv_4_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_4.csv'.format(query=query), header=None)
diffpriv_4_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_4.csv'.format(query=query), header=None)
diffpriv_4_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_4.csv'.format(query=query), header=None)

diffpriv_5_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_5.csv'.format(query=query), header=None)
diffpriv_5_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_5.csv'.format(query=query), header=None)
diffpriv_5_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_5.csv'.format(query=query), header=None)

diffpriv_6_01 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_0.1_memory_dataset_6.csv'.format(query=query), header=None)
diffpriv_6_1 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_1_memory_dataset_6.csv'.format(query=query), header=None)
diffpriv_6_10 = pd.read_csv(diffpriv_folder +'\\{query}\\eps_10_memory_dataset_6.csv'.format(query=query), header=None)


#diffpriv_memory_1 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d0}\\execution_memory.csv".format(q=query,d0=dataset0), header=None)
#diffpriv_memory_2 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d1}\\execution_memory.csv".format(q=query,d1=dataset1), header=None)
#diffpriv_memory_3 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d2}\\execution_memory.csv".format(q=query,d2=dataset2), header=None)
#diffpriv_memory_4 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d3}\\execution_memory.csv".format(q=query,d3=dataset3), header=None)
#diffpriv_memory_5 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d4}\\execution_memory.csv".format(q=query,d4=dataset4), header=None)
#diffpriv_memory_6 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d5}\\execution_memory.csv".format(q=query,d5=dataset5), header=None)
#diffpriv_memory_7 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d6}\\execution_memory.csv".format(q=query,d6=dataset6), header=None)


diffprivlib_memory_1 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_0\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_2 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_1\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_3 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_2\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_4 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_3\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_5 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_4\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_6 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_5\\AVG_memory.csv".format(q=query), header=None)
diffprivlib_memory_7 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_6\\AVG_memory.csv".format(q=query), header=None)


smartnoise_memory_1 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_0\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_2 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_1\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_3 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_2\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_4 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_3\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_5 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_4\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_6 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_5\\AVG_memory.csv".format(q=query), header=None)
smartnoise_memory_7 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_6\\AVG_memory.csv".format(q=query), header=None)


pydp_memory_1 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_0\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_2 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_1\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_3 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_2\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_4 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_3\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_5 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_4\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_6 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_5\\AVG_memory.csv".format(q=query), header=None)
pydp_memory_7 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_6\\AVG_memory.csv".format(q=query), header=None)


my_chorus_memory_1 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_0\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_2 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_1\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_3 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_2\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_4 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_3\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_5 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_4\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_6 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_5\\AVG_memory.csv".format(q=query), header=None)
my_chorus_memory_7 = pd.read_csv(result_folder + "\\chorus_27April\\{q}\\results_dataset_6\\AVG_memory.csv".format(q=query), header=None)


chorus_memory_1 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_0.csv", header=None)
chorus_memory_2 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_1.csv", header=None)
chorus_memory_3 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_2.csv", header=None)
chorus_memory_4 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_3.csv", header=None)
chorus_memory_5 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_4.csv", header=None)
chorus_memory_6 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_5.csv", header=None)
chorus_memory_7 = pd.read_csv(result_folder + "\\chorus_23April_memory\\memory_dataset_6.csv", header=None)

for i in range(3):
    diffprivlib_1.append(diffprivlib_memory_1.iloc[:,0][i])
    diffprivlib_2.append(diffprivlib_memory_2.iloc[:,0][i])
    diffprivlib_3.append(diffprivlib_memory_3.iloc[:,0][i])
    diffprivlib_4.append(diffprivlib_memory_4.iloc[:,0][i])
    diffprivlib_5.append(diffprivlib_memory_5.iloc[:,0][i])
    diffprivlib_6.append(diffprivlib_memory_6.iloc[:,0][i])
    diffprivlib_7.append(diffprivlib_memory_7.iloc[:,0][i])

    smartnosie_1.append(smartnoise_memory_1.iloc[:,0][i])
    smartnosie_2.append(smartnoise_memory_2.iloc[:,0][i])
    smartnosie_3.append(smartnoise_memory_3.iloc[:,0][i])
    smartnosie_4.append(smartnoise_memory_4.iloc[:,0][i])
    smartnosie_5.append(smartnoise_memory_5.iloc[:,0][i])
    smartnosie_6.append(smartnoise_memory_6.iloc[:,0][i])
    smartnosie_7.append(smartnoise_memory_7.iloc[:,0][i])

    pydp_1.append(pydp_memory_1.iloc[:,0][i])
    pydp_2.append(pydp_memory_2.iloc[:,0][i])
    pydp_3.append(pydp_memory_3.iloc[:,0][i])
    pydp_4.append(pydp_memory_4.iloc[:,0][i])
    pydp_5.append(pydp_memory_5.iloc[:,0][i])
    pydp_6.append(pydp_memory_6.iloc[:,0][i])
    pydp_7.append(pydp_memory_7.iloc[:,0][i])
    
    
    #diffpriv_1.append(diffpriv_memory_1.iloc[:,0][i])
    #diffpriv_2.append(diffpriv_memory_2.iloc[:,0][i])
    #diffpriv_3.append(diffpriv_memory_3.iloc[:,0][i])
    #diffpriv_4.append(diffpriv_memory_4.iloc[:,0][i])
    #diffpriv_5.append(diffpriv_memory_5.iloc[:,0][i])
    #diffpriv_6.append(diffpriv_memory_6.iloc[:,0][i])
    #diffpriv_7.append(diffpriv_memory_7.iloc[:,0][i])


for i in range(15):
    my_chorus_1.append(abs(my_chorus_memory_1.iloc[:,0][i]))
    my_chorus_2.append(abs(my_chorus_memory_2.iloc[:,0][i]))
    my_chorus_3.append(abs(my_chorus_memory_3.iloc[:,0][i]))
    my_chorus_4.append(abs(my_chorus_memory_4.iloc[:,0][i]))
    my_chorus_5.append(abs(my_chorus_memory_5.iloc[:,0][i]))
    my_chorus_6.append(abs(my_chorus_memory_6.iloc[:,0][i]))
    my_chorus_7.append(abs(my_chorus_memory_7.iloc[:,0][i]))

print(diffprivlib_1)
print(smartnosie_1)
print(pydp_1)




diffprivlib_eps1_list = [diffprivlib_1[0], diffprivlib_2[0],diffprivlib_3[0],diffprivlib_4[0],diffprivlib_5[0],diffprivlib_6[0],diffprivlib_7[0]]
diffprivlib_eps2_list = [diffprivlib_1[1], diffprivlib_2[1],diffprivlib_3[1],diffprivlib_4[1],diffprivlib_5[1],diffprivlib_6[1],diffprivlib_7[1]]
diffprivlib_eps3_list = [diffprivlib_1[2], diffprivlib_2[2],diffprivlib_3[2],diffprivlib_4[2],diffprivlib_5[2],diffprivlib_6[2],diffprivlib_7[2]]

smartnoise_eps1_list = [smartnosie_1[0],smartnosie_2[0],smartnosie_3[0],smartnosie_4[0],smartnosie_5[0],smartnosie_6[0],smartnosie_7[0]]
smartnoise_eps2_list = [smartnosie_1[1],smartnosie_2[1],smartnosie_3[1],smartnosie_4[1],smartnosie_5[1],smartnosie_6[1],smartnosie_7[1]]
smartnoise_eps3_list = [smartnosie_1[2],smartnosie_2[2],smartnosie_3[2],smartnosie_4[2],smartnosie_5[2],smartnosie_6[2],smartnosie_7[2]]

pydp_eps1_list = [pydp_1[0],pydp_2[0],pydp_3[0],pydp_4[0],pydp_5[0],pydp_6[0],pydp_7[0]]
pydp_eps2_list = [pydp_1[1],pydp_2[1],pydp_3[1],pydp_4[1],pydp_5[1],pydp_6[1],pydp_7[1]]
pydp_eps3_list = [pydp_1[2],pydp_2[2],pydp_3[2],pydp_4[2],pydp_5[2],pydp_6[2],pydp_7[2]]

my_chorus_eps1_list = [np.mean(my_chorus_1[0:6]) + 119266, np.mean(my_chorus_2[0:6]) + 119266, np.mean(my_chorus_3[0:6]) + 119266, np.mean(my_chorus_4[0:6]) + 362688, np.mean(my_chorus_5[0:6]) + 2130536, np.mean(my_chorus_6[0:6])+ 2130536, np.mean(my_chorus_7[0:6])+ 2130540]
my_chorus_eps2_list = [np.mean(my_chorus_1[6:11]) + 119266, np.mean(my_chorus_2[6:11])  + 119266, np.mean(my_chorus_3[6:11]) + 119266, np.mean(my_chorus_4[6:11])+ 362688, np.mean(my_chorus_5[6:11])+ 2130536, np.mean(my_chorus_6[6:11])+ 2130536, np.mean(my_chorus_7[6:11])+ 2130540]
my_chorus_eps3_list = [np.mean(my_chorus_1[11:16])  + 119266, np.mean(my_chorus_2[11:16])  + 119266, np.mean(my_chorus_3[11:16]) + 119266, np.mean(my_chorus_4[11:16])+ 362688, np.mean(my_chorus_5[11:16])+ 2130536, np.mean(my_chorus_6[11:16])+ 2130536, np.mean(my_chorus_7[11:16])+ 2130540]

chorus_all_eps_list = [np.mean(chorus_memory_1), np.mean(chorus_memory_2), np.mean(chorus_memory_3), np.mean(chorus_memory_4), np.mean(chorus_memory_5), np.mean(chorus_memory_6), np.mean(chorus_memory_7)]

diffpriv_eps1_list = [diffpriv_0_01.iloc[:,0][0], diffpriv_1_01.iloc[:,0][0], diffpriv_2_01.iloc[:,0][0], diffpriv_3_01.iloc[:,0][0], diffpriv_4_01.iloc[:,0][0], diffpriv_5_01.iloc[:,0][0], diffpriv_6_01.iloc[:,0][0]]
diffpriv_eps2_list = [diffpriv_0_1.iloc[:,0][0], diffpriv_1_1.iloc[:,0][0], diffpriv_2_1.iloc[:,0][0], diffpriv_3_1.iloc[:,0][0], diffpriv_4_1.iloc[:,0][0], diffpriv_5_1.iloc[:,0][0], diffpriv_6_1.iloc[:,0][0]]
diffpriv_eps3_list = [diffpriv_0_10.iloc[:,0][0], diffpriv_1_10.iloc[:,0][0], diffpriv_2_10.iloc[:,0][0], diffpriv_3_10.iloc[:,0][0], diffpriv_4_10.iloc[:,0][0], diffpriv_5_10.iloc[:,0][0], diffpriv_6_10.iloc[:,0][0]]

datasets_list = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

gs1 = gs.GridSpec(nrows=1, ncols=1)
figure = plt.gcf()  # get current figure
figure.clf()

ax1 = plt.subplot(gs1[0,0])
#ax1.set_xlabel('Datasets', fontsize = 12)
ax1.set_ylabel('𝔼[Memory Consumed] \n [bytes]', fontsize = 16)

#### diffprivlib plotting
ax1.plot(datasets_list, diffprivlib_eps1_list, color = 'xkcd:orangish red', label="diffprivlib, IBM (Python)")
ax1.plot(datasets_list, diffprivlib_eps1_list, "o", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

ax1.plot(datasets_list, diffprivlib_eps2_list, color = 'xkcd:orangish red')
ax1.plot(datasets_list, diffprivlib_eps2_list, "v", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

ax1.plot(datasets_list, diffprivlib_eps3_list, color = 'xkcd:orangish red')
ax1.plot(datasets_list, diffprivlib_eps3_list, "s", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

#### smartnoise plotting
ax1.plot(datasets_list, smartnoise_eps1_list, color = 'xkcd:moss green', label="SmartNoise, Microsoft (Python wrapper over Rust)")
ax1.plot(datasets_list, smartnoise_eps1_list, "o", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

ax1.plot(datasets_list, smartnoise_eps2_list, color = 'xkcd:moss green')
ax1.plot(datasets_list, smartnoise_eps2_list, "v", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

ax1.plot(datasets_list, smartnoise_eps3_list, color = 'xkcd:moss green')
ax1.plot(datasets_list, smartnoise_eps3_list, "s", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

#### pydp plotting
ax1.plot(datasets_list, pydp_eps1_list, color = 'xkcd:soft blue', label="PyDP (Python wrapper over Google DP C++)")
ax1.plot(datasets_list, pydp_eps1_list, "o", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

ax1.plot(datasets_list, pydp_eps2_list, color = 'xkcd:soft blue')
ax1.plot(datasets_list, pydp_eps2_list, "v", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

ax1.plot(datasets_list, pydp_eps3_list, color = 'xkcd:soft blue')
ax1.plot(datasets_list, pydp_eps3_list, "s", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

#### diffpriv plotting
ax1.plot(datasets_list, diffpriv_eps1_list, color = 'xkcd:aquamarine', label="diffpriv, B. Rubinstein, et al. (R)")
ax1.plot(datasets_list, diffpriv_eps1_list, "o", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

ax1.plot(datasets_list, diffpriv_eps2_list, color = 'xkcd:aquamarine')
ax1.plot(datasets_list, diffpriv_eps2_list, "v", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

ax1.plot(datasets_list, diffpriv_eps3_list, color = 'xkcd:aquamarine')
ax1.plot(datasets_list, diffpriv_eps3_list, "s", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

#ax1.plot(datasets_list, smartnoise_eps3_list, "s", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

#### MY chorus plotting
ax1.plot(datasets_list, my_chorus_eps1_list, color = 'xkcd:purple', label="Chorus, J. Near et al (Scala)")
ax1.plot(datasets_list, my_chorus_eps1_list, "o", markeredgecolor='xkcd:purple', mfc='xkcd:purple')

ax1.plot(datasets_list, my_chorus_eps2_list, color = 'xkcd:purple')
ax1.plot(datasets_list, my_chorus_eps2_list, "v", markeredgecolor='xkcd:purple', mfc='xkcd:purple')

ax1.plot(datasets_list, my_chorus_eps3_list, color = 'xkcd:purple')
ax1.plot(datasets_list, my_chorus_eps3_list, "s", markeredgecolor='xkcd:purple', mfc='xkcd:purple')

# labels
ax1.set_xlabel('Number of Data Points (Scale)', fontsize=16)
leg1 = ax1.legend(prop={'size': 19}, loc="lower center", bbox_to_anchor=(0.33, -0.915), frameon=False, ncol=1)
figure.subplots_adjust(bottom=0.4)

if query == 'count':
    plt.title('Count Query (Std = 250, Skew = 5)'.format(q=query), fontsize=18)
if query == 'sum':
    plt.title('Sum Query (Std = 250, Skew = 5)'.format(q=query), fontsize=18)
if query == 'mean':
    plt.title('Mean Query (Std = 250, Skew = 5)'.format(q=query), fontsize=18)
if query == 'var':
    plt.title('Variance Query (Std = 250, Skew = 5)'.format(q=query), fontsize=18)


legend_elements = [Line2D([0], [0], marker='o', color='w', label='ε = 0.1', markerfacecolor='k', markersize=10), Line2D([0], [0], marker='v', color='w', label='ε = 1.0', markerfacecolor='k', markersize=10), Line2D([0], [0], marker='s', color='w', label='ε = 10.0', markerfacecolor='k', markersize=10)]

figure.legend(prop={'size': 18},handles=legend_elements, loc="lower center", bbox_to_anchor=(0.83, 0.02), frameon=False, ncol=1, handletextpad=0.2, handlelength=1)
ax1.tick_params(axis='both', which='major', labelsize=16)

plt.loglog()
plt.show()

