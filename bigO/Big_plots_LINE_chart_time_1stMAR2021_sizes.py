import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pandas as pd
import csv
epsilon = pd.read_pickle('epsilon.pkl')

result_folder = "E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\real_dataset_micro\\bigO"

query = 'count'


dataset1 = 0
dataset2 = 1
dataset3 = 2
dataset4 = 3


diffprivlib_1 = []
diffprivlib_2 = []
diffprivlib_3 = []
diffprivlib_4 = []

smartnosie_1 = []
smartnosie_2 = []
smartnosie_3 = []
smartnosie_4 = []

pydp_1 = []
pydp_2 = []
pydp_3 = []
pydp_4 = []

diffpriv_1 = []
diffpriv_2 = []
diffpriv_3 = []
diffpriv_4 = []

epsilon = [0.1, 1.0, 10.0]
epsilon_diffpriv = [0.1, 1, 10]

for eps_diffpriv in epsilon_diffpriv:
    diffpriv_time_1 = pd.read_csv(result_folder + "\\diffpriv\\{q}_time_eps_{eps}_dataset_{d1}.csv".format(q=query,d1=dataset1, eps=eps_diffpriv), header=None)
    diffpriv_time_2 = pd.read_csv(result_folder + "\\diffpriv\\{q}_time_eps_{eps}_dataset_{d2}.csv".format(q=query,d2=dataset2, eps=eps_diffpriv), header=None)
    diffpriv_time_3 = pd.read_csv(result_folder + "\\diffpriv\\{q}_time_eps_{eps}_dataset_{d3}.csv".format(q=query,d3=dataset3, eps=eps_diffpriv), header=None)
    diffpriv_1.append(1/diffpriv_time_1.iloc[:,0][0])
    diffpriv_2.append(1/diffpriv_time_2.iloc[:,0][0])
    diffpriv_3.append(1/diffpriv_time_3.iloc[:,0][0])

for eps in epsilon:
    diffprivlib_time_1 = pd.read_csv(result_folder + "\\diffprivlib\\{q}_time_eps_{eps}_dataset_{d1}.csv".format(q=query,d1=dataset1, eps=eps), header=None)
    smartnoise_time_1 = pd.read_csv(result_folder + "\\smartnoise\\{q}_time_eps_{eps}_dataset_{d1}.csv".format(q=query,d1=dataset1, eps=eps), header=None)
    pydp_time_1 = pd.read_csv(result_folder + "\\pydp\\{q}_time_eps_{eps}_dataset_{d1}.csv".format(q=query,d1=dataset1, eps=eps), header=None)

    diffprivlib_time_2 = pd.read_csv(result_folder + "\\diffprivlib\\{q}_time_eps_{eps}_dataset_{d2}.csv".format(q=query,d2=dataset2, eps=eps), header=None)
    smartnoise_time_2 = pd.read_csv(result_folder + "\\smartnoise\\{q}_time_eps_{eps}_dataset_{d2}.csv".format(q=query,d2=dataset2, eps=eps), header=None)
    pydp_time_2 = pd.read_csv(result_folder + "\\pydp\\{q}_time_eps_{eps}_dataset_{d2}.csv".format(q=query,d2=dataset2, eps=eps), header=None)

    diffprivlib_time_3 = pd.read_csv(result_folder + "\\diffprivlib\\{q}_time_eps_{eps}_dataset_{d3}.csv".format(q=query,d3=dataset3, eps=eps), header=None)
    smartnoise_time_3 = pd.read_csv(result_folder + "\\smartnoise\\{q}_time_eps_{eps}_dataset_{d3}.csv".format(q=query,d3=dataset3, eps=eps), header=None)
    pydp_time_3 = pd.read_csv(result_folder + "\\pydp\\{q}_time_eps_{eps}_dataset_{d3}.csv".format(q=query,d3=dataset3, eps=eps), header=None)

    diffprivlib_time_4 = pd.read_csv(result_folder + "\\diffprivlib\\{q}_time_eps_{eps}_dataset_{d4}.csv".format(q=query,d4=dataset4, eps=eps), header=None)
    #smartnoise_time_4 = pd.read_csv(result_folder + "\\smartnoise\\{q}_time_eps_{eps}_dataset_{d4}.csv".format(q=query,d4=dataset4, eps=eps), header=None)
    pydp_time_4 = pd.read_csv(result_folder + "\\pydp\\{q}_time_eps_{eps}_dataset_{d4}.csv".format(q=query,d4=dataset4, eps=eps), header=None)

    diffprivlib_1.append(1/diffprivlib_time_1.iloc[:,0][1])
    diffprivlib_2.append(1/diffprivlib_time_2.iloc[:,0][1])
    diffprivlib_3.append(1/diffprivlib_time_3.iloc[:,0][1])

    smartnosie_1.append(1/smartnoise_time_1.iloc[:,0][1])
    smartnosie_2.append(1/smartnoise_time_2.iloc[:,0][1])
    smartnosie_3.append(1/smartnoise_time_3.iloc[:,0][1])

    pydp_1.append(1/pydp_time_1.iloc[:,0][1])
    pydp_2.append(1/pydp_time_2.iloc[:,0][1])
    pydp_3.append(1/pydp_time_3.iloc[:,0][1])

'''
print('diffprivlib')
print(diffprivlib_1)
print(diffprivlib_2)
print(diffprivlib_3)
print('smartnoise')
print(smartnosie_1)
print(smartnosie_2)
print(smartnosie_3)
print('pydp')
print(pydp_1)
print(pydp_2)
print(pydp_3)
print('diffpriv')
print(diffpriv_1)
print(diffpriv_2)
print(diffpriv_3)
'''

####### initializing Gridspec #########
gs1 = gs.GridSpec(nrows=1, ncols=3)
figure = plt.gcf()  # get current figure
figure.clf()

ax1 = plt.subplot(gs1[0,0])
ax1.set_xlabel('ε', fontsize = 12)
ax1.set_ylabel('Throughput [queries/sec]', fontsize = 14)
#ax1.grid(color='b',b='animated', ls = '-.', lw = 0.25)

ax1.plot(epsilon, diffprivlib_1, color = 'xkcd:orangish red')
ax1.plot(epsilon, diffprivlib_1, "o", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')
ax1.plot(epsilon, smartnosie_1, color = 'xkcd:moss green')
ax1.plot(epsilon, smartnosie_1, "o", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')
ax1.plot(epsilon, pydp_1, color = 'xkcd:soft blue')
ax1.plot(epsilon, pydp_1, "o", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')
ax1.plot(epsilon, diffpriv_1, color = 'xkcd:pumpkin')
ax1.plot(epsilon, diffpriv_1, "o", markeredgecolor='xkcd:pumpkin', mfc='xkcd:pumpkin')

ax2 = plt.subplot(gs1[0,1], sharey=ax1)
plt.setp(ax2.get_yticklabels(), visible=False)
ax2.set_xlabel('ε', fontsize = 12)
#ax2.grid(color='b', ls = '-.', lw = 0.25)

ax2.plot(epsilon, diffprivlib_2, color = 'xkcd:orangish red')
ax2.plot(epsilon, diffprivlib_2, "o", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')
ax2.plot(epsilon, smartnosie_2, color = 'xkcd:moss green')
ax2.plot(epsilon, smartnosie_2, "o", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')
ax2.plot(epsilon, pydp_2, color = 'xkcd:soft blue')
ax2.plot(epsilon, pydp_2, "o", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')
ax2.plot(epsilon, diffpriv_2, color = 'xkcd:pumpkin')
ax2.plot(epsilon, diffpriv_2, "o", markeredgecolor='xkcd:pumpkin', mfc='xkcd:pumpkin')


ax3 = plt.subplot(gs1[0,2], sharey=ax1)
plt.setp(ax3.get_yticklabels(), visible=False)
ax3.set_xlabel('ε', fontsize = 12)
#ax3.grid(color='b', ls = '-.', lw = 0.25)


ax3.plot(epsilon, diffprivlib_3, color = 'xkcd:orangish red', label="diffprivlib, IBM (Python)")
ax3.plot(epsilon, diffprivlib_3, "o", markeredgecolor='xkcd:orangish red', mfc='xkcd:orangish red')
ax3.plot(epsilon, smartnosie_3, color = 'xkcd:moss green', label="SmartNoise, Microsoft (Python wrapper over Rust)")
ax3.plot(epsilon, smartnosie_3, "o", markeredgecolor='xkcd:moss green', mfc='xkcd:moss green')
ax3.plot(epsilon, pydp_3, color = 'xkcd:soft blue', label="PyDP (Python wrapper over Google DP C++)")
ax3.plot(epsilon, pydp_3, "o", markeredgecolor='xkcd:soft blue', mfc='xkcd:soft blue')
ax3.plot(epsilon, diffpriv_3, color = 'xkcd:pumpkin', label="diffpriv, B. Rubinstein, et al. (R)")
ax3.plot(epsilon, diffpriv_3, "o", markeredgecolor='xkcd:pumpkin', mfc='xkcd:pumpkin')
ax3_plot = ax3.plot(epsilon, diffpriv_3, "o", markeredgecolor='xkcd:pumpkin', mfc='xkcd:pumpkin')

leg1 = ax3.legend(prop={'size': 13}, loc="lower center", bbox_to_anchor=(-0.53, -0.31), frameon=False, ncol=2)
figure.subplots_adjust(bottom=0.25)

ax1.loglog()
ax2.loglog()
ax3.loglog()

legend1 = ax1.legend(loc='lower right', title='Size = 1000', frameon=False)
legend1.get_title().set_fontsize('13')
legend2 = ax2.legend(loc='lower right', title='Size = 10000', frameon=False)
legend2.get_title().set_fontsize('13')
handles, labels = ax3.get_legend_handles_labels()
legend3 = ax3.legend(loc='lower right', title='Size = 100000', frameon=False, labels=labels, handles=[ax3_plot])
leg2 = legend3.get_title().set_fontsize('13')
ax3.add_artist(leg1)

gs1.update(wspace=0.035, hspace=0.1)
if query == 'count':
    ax2.set_title('Count Query'.format(q=query), fontsize=13)
if query == 'sum':
    ax2.set_title('Sum Query'.format(q=query), fontsize=13)
if query == 'mean':
    ax2.set_title('Mean Query'.format(q=query), fontsize=13)
if query == 'var':
    ax2.set_title('Variance Query'.format(q=query), fontsize=13)

plt.show()
