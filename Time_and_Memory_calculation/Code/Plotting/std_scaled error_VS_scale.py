import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pandas as pd
import csv
import matplotlib.legend as mlegend
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


result_folder = "E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\real_dataset_micro\\bigO\\micro_bigO_20thMar_2021_v2\\27thApril"

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

chorus_1 = []
chorus_2 = []
chorus_3 = []
chorus_4 = []
chorus_5 = []
chorus_6 = []
chorus_7 = []


epsilon = [0.1, 1.0, 10.0]
epsilon_diffpriv = [0.1, 1, 10]


chorus_time_1 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_0\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_2 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_1\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_3 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_2\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_4 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_3\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_5 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_4\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_6 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_5\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
chorus_time_7 = pd.read_csv(result_folder + "\\chorus_stdvsscale\\{q}\\results_dataset_6\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)


diffpriv_time_1 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_0\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_2 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_1\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_3 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_2\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_4 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_3\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_5 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_4\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_6 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_5\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)
diffpriv_time_7 = pd.read_csv(result_folder + "\\diffpriv_simple_time\\{q}\\results_dataset_6\\std_scaled_error\\std_scaled_error.csv".format(q=query), header=None)


diffprivlib_time_1 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_0\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_2 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_1\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_3 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_2\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_4 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_3\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_5 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_4\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_6 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_5\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
diffprivlib_time_7 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_6\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)


smartnoise_time_1 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_0\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_2 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_1\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_3 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_2\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_4 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_3\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_5 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_4\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_6 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_5\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
smartnoise_time_7 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_6\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)


pydp_time_1 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_0\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_2 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_1\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_3 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_2\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_4 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_3\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_5 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_4\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_6 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_5\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)
pydp_time_7 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_6\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query), header=None)



for i in range(3):
    diffprivlib_1.append(diffprivlib_time_1.iloc[:,0][i])
    diffprivlib_2.append(diffprivlib_time_2.iloc[:,0][i])
    diffprivlib_3.append(diffprivlib_time_3.iloc[:,0][i])
    diffprivlib_4.append(diffprivlib_time_4.iloc[:,0][i])
    diffprivlib_5.append(diffprivlib_time_5.iloc[:,0][i])
    diffprivlib_6.append(diffprivlib_time_6.iloc[:,0][i])
    diffprivlib_7.append(diffprivlib_time_7.iloc[:,0][i])

    smartnosie_1.append(smartnoise_time_1.iloc[:,0][i])
    smartnosie_2.append(smartnoise_time_2.iloc[:,0][i])
    smartnosie_3.append(smartnoise_time_3.iloc[:,0][i])
    smartnosie_4.append(smartnoise_time_4.iloc[:,0][i])
    smartnosie_5.append(smartnoise_time_5.iloc[:,0][i])
    smartnosie_6.append(smartnoise_time_6.iloc[:,0][i])
    smartnosie_7.append(smartnoise_time_7.iloc[:,0][i])

    pydp_1.append(pydp_time_1.iloc[:,0][i])
    pydp_2.append(pydp_time_2.iloc[:,0][i])
    pydp_3.append(pydp_time_3.iloc[:,0][i])
    pydp_4.append(pydp_time_4.iloc[:,0][i])
    pydp_5.append(pydp_time_5.iloc[:,0][i])
    pydp_6.append(pydp_time_6.iloc[:,0][i])
    pydp_7.append(pydp_time_7.iloc[:,0][i])

    diffpriv_1.append(diffpriv_time_1.iloc[:,0][i])
    diffpriv_2.append(diffpriv_time_2.iloc[:,0][i])
    diffpriv_3.append(diffpriv_time_3.iloc[:,0][i])
    diffpriv_4.append(diffpriv_time_4.iloc[:,0][i])
    diffpriv_5.append(diffpriv_time_5.iloc[:,0][i])
    diffpriv_6.append(diffpriv_time_6.iloc[:,0][i])
    diffpriv_7.append(diffpriv_time_7.iloc[:,0][i])
    
    chorus_1.append(chorus_time_1.iloc[:,0][i])
    chorus_2.append(chorus_time_2.iloc[:,0][i])
    chorus_3.append(chorus_time_3.iloc[:,0][i])
    chorus_4.append(chorus_time_4.iloc[:,0][i])
    chorus_5.append(chorus_time_5.iloc[:,0][i])
    chorus_6.append(chorus_time_6.iloc[:,0][i])
    chorus_7.append(chorus_time_7.iloc[:,0][i])
    

print(diffprivlib_1)
print(smartnosie_1)
print(pydp_1)
print(diffpriv_1)


chorus_eps1_list = [chorus_1[0], chorus_2[0],chorus_3[0],chorus_4[0],chorus_5[0],chorus_6[0],chorus_7[0]]
chorus_eps2_list = [chorus_1[1], chorus_2[1],chorus_3[1],chorus_4[1],chorus_5[1],chorus_6[1],chorus_7[1]]
chorus_eps3_list = [chorus_1[2], chorus_2[2],chorus_3[2],chorus_4[2],chorus_5[2],chorus_6[2],chorus_7[2]]


diffprivlib_eps1_list = [diffprivlib_1[0], diffprivlib_2[0],diffprivlib_3[0],diffprivlib_4[0],diffprivlib_5[0],diffprivlib_6[0],diffprivlib_7[0]]
diffprivlib_eps2_list = [diffprivlib_1[1], diffprivlib_2[1],diffprivlib_3[1],diffprivlib_4[1],diffprivlib_5[1],diffprivlib_6[1],diffprivlib_7[1]]
diffprivlib_eps3_list = [diffprivlib_1[2], diffprivlib_2[2],diffprivlib_3[2],diffprivlib_4[2],diffprivlib_5[2],diffprivlib_6[2],diffprivlib_7[2]]

smartnoise_eps1_list = [smartnosie_1[0],smartnosie_2[0],smartnosie_3[0],smartnosie_4[0],smartnosie_5[0],smartnosie_6[0],smartnosie_7[0]]
smartnoise_eps2_list = [smartnosie_1[1],smartnosie_2[1],smartnosie_3[1],smartnosie_4[1],smartnosie_5[1],smartnosie_6[1],smartnosie_7[1]]
smartnoise_eps3_list = [smartnosie_1[2],smartnosie_2[2],smartnosie_3[2],smartnosie_4[2],smartnosie_5[2],smartnosie_6[2],smartnosie_7[2]]

pydp_eps1_list = [pydp_1[0],pydp_2[0],pydp_3[0],pydp_4[0],pydp_5[0],pydp_6[0],pydp_7[0]]
pydp_eps2_list = [pydp_1[1],pydp_2[1],pydp_3[1],pydp_4[1],pydp_5[1],pydp_6[1],pydp_7[1]]
pydp_eps3_list = [pydp_1[2],pydp_2[2],pydp_3[2],pydp_4[2],pydp_5[2],pydp_6[2],pydp_7[2]]

diffpriv_eps1_list = [diffpriv_1[0],diffpriv_2[0],diffpriv_3[0],diffpriv_4[0],diffpriv_5[0],diffpriv_6[0],diffpriv_7[0]]
diffpriv_eps2_list = [diffpriv_1[1],diffpriv_2[1],diffpriv_3[1],diffpriv_4[1],diffpriv_5[1],diffpriv_6[1],diffpriv_7[1]]
diffpriv_eps3_list = [diffpriv_1[2],diffpriv_2[2],diffpriv_3[2],diffpriv_4[2],diffpriv_5[2],diffpriv_6[2],diffpriv_7[2]]

datasets_list = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

gs1 = gs.GridSpec(nrows=1, ncols=1)
figure = plt.gcf()  # get current figure
figure.clf()

ax1 = plt.subplot(gs1[0,0])
#ax1.set_xlabel('Datasets', fontsize = 12)
ax1.set_ylabel('Sample Std of the \n Absolute Scaled Error', fontsize = 18.5)


# diffprivlib
ax1.plot(datasets_list, diffprivlib_eps1_list, color = 'xkcd:orangish red', label="diffprivlib, IBM (Python)")
ax1.plot(datasets_list, diffprivlib_eps1_list, "o", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

ax1.plot(datasets_list, diffprivlib_eps2_list, color = 'xkcd:orangish red')
ax1.plot(datasets_list, diffprivlib_eps2_list, "v", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

ax1.plot(datasets_list, diffprivlib_eps3_list, color = 'xkcd:orangish red')
ax1.plot(datasets_list, diffprivlib_eps3_list, "s", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')

# smartnoise
ax1.plot(datasets_list, smartnoise_eps1_list, color = 'xkcd:moss green', label="SmartNoise, Microsoft (Python wrapper over Rust)")
ax1.plot(datasets_list, smartnoise_eps1_list, "o", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

ax1.plot(datasets_list, smartnoise_eps2_list, color = 'xkcd:moss green')
ax1.plot(datasets_list, smartnoise_eps2_list, "v", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

ax1.plot(datasets_list, smartnoise_eps3_list, color = 'xkcd:moss green')
ax1.plot(datasets_list, smartnoise_eps3_list, "s", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')

# pydp
ax1.plot(datasets_list, pydp_eps1_list, color = 'xkcd:soft blue', label="PyDP (Python wrapper over Google DP C++)")
ax1.plot(datasets_list, pydp_eps1_list, "o", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

ax1.plot(datasets_list, pydp_eps2_list, color = 'xkcd:soft blue')
ax1.plot(datasets_list, pydp_eps2_list, "v", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

ax1.plot(datasets_list, pydp_eps3_list, color = 'xkcd:soft blue')
ax1.plot(datasets_list, pydp_eps3_list, "s", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')

# diffpriv
ax1.plot(datasets_list, diffpriv_eps1_list, color = 'xkcd:aquamarine', label="diffpriv, B. Rubinstein et al. (R)")
ax1.plot(datasets_list, diffpriv_eps1_list, "o", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

ax1.plot(datasets_list, diffpriv_eps2_list, color = 'xkcd:aquamarine')
ax1.plot(datasets_list, diffpriv_eps2_list, "v", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

ax1.plot(datasets_list, diffpriv_eps3_list, color = 'xkcd:aquamarine')
ax1.plot(datasets_list, diffpriv_eps3_list, "s", markeredgecolor='xkcd:aquamarine', mfc='xkcd:aquamarine')

# chorus
ax1.plot(datasets_list, chorus_eps1_list, color = 'xkcd:purple', label="Chorus, J. Near et al (Scala)")
ax1.plot(datasets_list, chorus_eps1_list, "o", markeredgecolor='xkcd:purple', mfc='xkcd:purple')

ax1.plot(datasets_list, chorus_eps2_list, color = 'xkcd:purple')
ax1.plot(datasets_list, chorus_eps2_list, "v", markeredgecolor='xkcd:purple', mfc='xkcd:purple')

ax1.plot(datasets_list, chorus_eps3_list, color = 'xkcd:purple')
ax1.plot(datasets_list, chorus_eps3_list, "s", markeredgecolor='xkcd:purple', mfc='xkcd:purple')


ax1.set_xlabel('Number of Data Points (Scale)', fontsize=16)

leg1 = ax1.legend(prop={'size': 19}, loc="lower center", bbox_to_anchor=(0.33, -0.9), frameon=False, ncol=1)

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

figure.legend(prop={'size': 18},handles=legend_elements, loc="lower center", bbox_to_anchor=(0.83, 0.03), frameon=False, ncol=1, handletextpad=0.2, handlelength=1)

#figure.text(0.89, 0.31,'Scale', size = 16)
plt.loglog()
plt.show()

