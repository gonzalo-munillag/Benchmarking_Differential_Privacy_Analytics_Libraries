import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pandas as pd
import csv
from matplotlib.lines import Line2D
epsilon = pd.read_pickle('epsilon.pkl')



def plots_with_sizes(result_folder, query, attribute):
        
    if attribute == 'age':
        d = 1
    if attribute == 'hrs':
        d = 2
    if attribute == 'absences':
        d = 3
    if attribute == 'grade':
        d = 4  


    ################# Std of scaled error  ######################
    diffprivlib_std = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=d), header=None)
    smartnoise_std = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=d), header=None)
    pydp_std = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=d), header=None)
    diffpriv_std = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=d), header=None)
    chorus_std = pd.read_csv(result_folder + "\\chorus_real_dataset_results\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=d), header=None)

    ################# Mean relative error  ######################
    diffprivlib_relative = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=d), header=None)
    smartnoise_relative = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=d), header=None)
    pydp_relative = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=d), header=None)
    diffpriv_relative = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=d), header=None)
    chorus_relative = pd.read_csv(result_folder + "\\chorus_real_dataset_results\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=d), header=None)


    ################   labels    ######################
    x1 = [0.01,0,0,0,0,0,0,0,0,  0.1  ,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0, 0,0, 1, 0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,100]
    x2 = [0.01,0,0,0,0,0,0,0,0,  0.1  ,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0, 0,0, 1, 0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,100]
    ################   Plotting    ######################
    gs1 = gs.GridSpec(nrows=1, ncols=2)
    gs1.update(wspace=0.3, hspace=0.05) # set the spacing between axes.
    figure = plt.gcf()  # get current figure
    figure.clf()    
    ###### Size plot  #######
    ax1 = plt.subplot(gs1[0,0])

    ax1.plot(x1, diffprivlib_std, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, diffprivlib_std, color = 'xkcd:orangish red')
    ax1.plot(x1, smartnoise_std[1:], "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, smartnoise_std[1:], color = 'xkcd:moss green')
    ax1.plot(x1, pydp_std, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, pydp_std, color = 'xkcd:soft blue')
    ax1.plot(x1, diffpriv_std, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, diffpriv_std, color = 'xkcd:aquamarine')
    ax1.plot(x1, chorus_std, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, chorus_std, color = 'xkcd:purple')

    ax1.set_xlabel('ε', fontsize = 12)
    ax1.set_ylabel('Sample Std of the \n Absolute Scaled Error', fontsize = 16)

    #################   MEAN RELATIVE ERROR  ############################
    ax2 = plt.subplot(gs1[0,1])

    ax2.plot(x2, abs(diffprivlib_relative)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(diffprivlib_relative)*100, color = 'xkcd:orangish red', label="diffprivlib, IBM (Python)")
    ax2.plot(x2, abs(smartnoise_relative[1:])*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(smartnoise_relative[1:])*100, color = 'xkcd:moss green', label="SmartNoise, Microsoft (Python wrapper over Rust)")
    ax2.plot(x2, abs(pydp_relative)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(pydp_relative)*100, color = 'xkcd:soft blue', label="PyDP (Python wrapper over Google DP C++)")
    ax2.plot(x2, abs(diffpriv_relative)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(diffpriv_relative)*100, color = 'xkcd:aquamarine', label="diffpriv, B. Rubinstein, et al. (R)")
    ax2.plot(x2, abs(chorus_relative)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(chorus_relative)*100, color = 'xkcd:purple', label="Chorus, J. Near et al (Scala)")

    ax2.set_xlabel('ε', fontsize = 12)
    ax2.set_ylabel('Sample Mean of the \n Absolute Relative Error [%]', fontsize = 16)
    
    #ax1.legend(prop={'size': 19}, loc="lower center", bbox_to_anchor=(1.00, -0.02), frameon=False, ncol=4, handletextpad=0.2, handlelength=1, columnspacing=0.5)
    #ax2.legend(prop={'size': 18}, loc="lower center", bbox_to_anchor=(-0.13, -0.30), frameon=False, ncol=2, handletextpad=0.2, handlelength=1, columnspacing=0.5)
    figure.subplots_adjust(bottom=0.30)
    
    #legend_elements_1 = [Line2D([1], [1], color='xkcd:orangish red', label='diffprivlib, IBM (Python)'), Line2D([1], [1], color='xkcd:soft blue', label='PyDP (Python wrapper over Google DP C++)'), Line2D([1], [1], color='xkcd:moss green', label='SmartNoise, Microsoft (Python wrapper over Rust)')]
    #figure.legend(prop={'size': 18.5},handles=legend_elements_1, loc="lower center", bbox_to_anchor=(0.33, -0.02), frameon=False, ncol=1, handletextpad=0.2, handlelength=1)
    #legend_elements_2 = [ Line2D([1], [1], color='xkcd:aquamarine', label='diffpriv, B. Rubinstein, et al. (R)'), Line2D([1], [1], color='xkcd:purple', label='Chorus, J. Near et al (Scala)')]
    #legend_elements_2 = [ Line2D([1], [1], color='xkcd:aquamarine', label='diffpriv, B. Rubinstein, et al. (R)')]
    #figure.legend(prop={'size': 18.5},handles=legend_elements_2, loc="lower center", bbox_to_anchor=(0.77, 0.04), frameon=False, ncol=1, handletextpad=0.2, handlelength=1)


    if query == 'count':
        ax1.set_ylim(10**-8, 10**3)
        figure.suptitle('Count Query', fontsize=19)

    if query == 'sum':
        ax1.set_ylim(10**-8, 10**8)
        figure.suptitle('Sum Query', fontsize=19)

    if query == 'mean':
        ax1.set_ylim(10**-12, 10**2)
        figure.suptitle('Mean Query', fontsize=19)

    if query == 'var':
        ax1.set_ylim(10**-8, 10**4)
        figure.suptitle('Variance Query', fontsize=19)

    ax1.tick_params(axis='both', which='major', labelsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax1.loglog()
    ax2.set_xscale('log')

    plt.show()


plots_with_sizes(result_folder="E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\real_dataset_micro\\22April2021", query="mean", attribute='grade')