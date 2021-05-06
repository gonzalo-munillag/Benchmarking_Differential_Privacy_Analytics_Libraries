import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np
import pandas as pd
import csv
from matplotlib.lines import Line2D
epsilon = pd.read_pickle('epsilon.pkl')


def plots_with_sizes(result_folder, query, sets, first_dataset, second_dataset, third_dataset):
    ################# Std of scaled error  ######################

    IBM_std_scaled_error_0 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    IBM_std_scaled_error_1 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    IBM_std_scaled_error_2 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    IBM_mean_relative_error_0 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    IBM_mean_relative_error_1 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    IBM_mean_relative_error_2 = pd.read_csv(result_folder + "\\diffprivlib\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=third_dataset), header=None)

    ####
    SmartNoise_std_scaled_error_0 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    SmartNoise_std_scaled_error_1 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    SmartNoise_std_scaled_error_2 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    SmartNoise_mean_relative_error_0 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    SmartNoise_mean_relative_error_1 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    SmartNoise_mean_relative_error_2 = pd.read_csv(result_folder + "\\smartnoise\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=third_dataset), header=None)

    ####
    PyDP_std_scaled_error_0 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    PyDP_std_scaled_error_1 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    PyDP_std_scaled_error_2 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    PyDP_mean_relative_error_0 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    PyDP_mean_relative_error_1 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    PyDP_mean_relative_error_2 = pd.read_csv(result_folder + "\\pydp\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=third_dataset), header=None)

    ####
    diffpriv_simple_std_scaled_error_0 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    diffpriv_simple_std_scaled_error_1 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    diffpriv_simple_std_scaled_error_2 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    diffpriv_simple_mean_relative_error_0 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    diffpriv_simple_mean_relative_error_1 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    diffpriv_simple_mean_relative_error_2 = pd.read_csv(result_folder + "\\diffpriv_simple\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=third_dataset), header=None)
    
    ####
    diffpriv_std_scaled_error_0 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    diffpriv_std_scaled_error_1 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    diffpriv_std_scaled_error_2 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\std_scaled_error\\std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    diffpriv_mean_relative_error_0 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    diffpriv_mean_relative_error_1 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    diffpriv_mean_relative_error_2 = pd.read_csv(result_folder + "\\diffpriv\\{q}\\results_dataset_{d}\\mean_relative_error\\mean_relative_error.csv".format(q=query,d=third_dataset), header=None)
    
    ####
    chorus_std_scaled_error_0 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=first_dataset), header=None)
    chorus_std_scaled_error_1 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=second_dataset), header=None)
    chorus_std_scaled_error_2 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\std_scaled_error\\DP_std_scaled_error.csv".format(q=query,d=third_dataset), header=None)

    chorus_mean_relative_error_0 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=first_dataset), header=None)
    chorus_mean_relative_error_1 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=second_dataset), header=None)
    chorus_mean_relative_error_2 = pd.read_csv(result_folder + "\\chorus\\{q}\\results_dataset_{d}\\mean_relative_error\\DP_mean_relative_error.csv".format(q=query,d=third_dataset), header=None)

    ################   labels    ######################
    x1 = [0.01,0,0,0,0,0,0,0,0,  0.1  ,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0, 0,0, 1, 0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,100]
    x2 = [0.01,0,0,0,0,0,0,0,0,  0.1  ,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0, 0,0, 1, 0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,100]
    ################   Plotting    ######################
    gs1 = gs.GridSpec(nrows=1, ncols=2)
    gs1.update(wspace=0.26, hspace=0.05) # set the spacing between axes.
    
    figure = plt.gcf()  # get current figure
    figure.clf()    
    ###### Size plot  #######
    ax1 = plt.subplot(gs1[0,0])

    ax1.plot(x1, IBM_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, IBM_std_scaled_error_0, color = 'xkcd:orangish red')
    ax1.plot(x1, SmartNoise_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, SmartNoise_std_scaled_error_0, color = 'xkcd:moss green')
    ax1.plot(x1, PyDP_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, PyDP_std_scaled_error_0, color = 'xkcd:soft blue')
    ax1.plot(x1, diffpriv_simple_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, diffpriv_simple_std_scaled_error_0, color = 'xkcd:aquamarine')
    #ax1.plot(x1, diffpriv_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    #ax1.plot(epsilon, diffpriv_std_scaled_error_0, color = 'xkcd:grey')
    ax1.plot(x1, chorus_std_scaled_error_0, "o", markeredgecolor='k', mfc='none')
    ax1.plot(epsilon, chorus_std_scaled_error_0, color = 'xkcd:purple')
    #ax1.plot(x1, [float(additive_noise_std_scaled_error_0[0])]*73 , "o", markeredgecolor='k', mfc='none')
    #ax1.plot(epsilon, [float(additive_noise_std_scaled_error_0[0])]*73, color = 'k')

    ax1.plot(x1, IBM_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, IBM_std_scaled_error_1, color = 'xkcd:orangish red')
    ax1.plot(x1, SmartNoise_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, SmartNoise_std_scaled_error_1, color = 'xkcd:moss green')
    ax1.plot(x1, PyDP_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, PyDP_std_scaled_error_1, color = 'xkcd:soft blue')
    ax1.plot(x1, diffpriv_simple_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, diffpriv_simple_std_scaled_error_1, color = 'xkcd:aquamarine')
    #ax1.plot(x1, diffpriv_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    #ax1.plot(epsilon, diffpriv_std_scaled_error_1, color = 'xkcd:grey')
    ax1.plot(x1, chorus_std_scaled_error_1, "s", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, chorus_std_scaled_error_1, color = 'xkcd:purple')
    #ax1.plot(x1, [float(additive_noise_std_scaled_error_1[0])]*73 , "s", markeredgecolor='k', mfc='none')
    #ax1.plot(epsilon, [float(additive_noise_std_scaled_error_1[0])]*73, color = 'k')

    ax1.plot(x1, IBM_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, IBM_std_scaled_error_2, color = 'xkcd:orangish red', label="diffprivlib, IBM (Python)")
    ax1.plot(x1, SmartNoise_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, SmartNoise_std_scaled_error_2, color = 'xkcd:moss green', label="SmartNoise, Microsoft (Python wrapper over Rust)")
    ax1.plot(x1, PyDP_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, PyDP_std_scaled_error_2, color = 'xkcd:soft blue', label="PyDP (Python wrapper over Google DP C++)")
    ax1.plot(x1, diffpriv_simple_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, diffpriv_simple_std_scaled_error_2, color = 'xkcd:aquamarine', label="diffpriv, B. Rubinstein, et al. (R)")
    #ax1.plot(x1, diffpriv_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    #ax1.plot(epsilon, diffpriv_std_scaled_error_2, color = 'xkcd:grey', label="diffpriv (Sensitivity Sampler)")
    ax1.plot(x1, chorus_std_scaled_error_2, "v", markeredgecolor='k',mfc='none')
    ax1.plot(epsilon, chorus_std_scaled_error_2, color = 'xkcd:purple', label="Chorus, J. Near et al (Scala)")
    #ax1.plot(x1, [float(additive_noise_std_scaled_error_2[0])]*73 , "v", markeredgecolor='k', mfc='none')
    #ax1.plot(epsilon, [float(additive_noise_std_scaled_error_2[0])]*73, color = 'k')


    ax1.set_xlabel('ε', fontsize = 18)
    ax1.set_ylabel('Sample Std of the \n Absolute Scaled Error', fontsize = 28)


    #################   MEAN RELATIVE ERROR  ############################
    ax2 = plt.subplot(gs1[0,1])

    ax2.plot(x2, abs(IBM_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none', label="scale = 1000")
    ax2.plot(epsilon, abs(IBM_mean_relative_error_0)*100, color = 'xkcd:orangish red')
    ax2.plot(x2, abs(SmartNoise_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(SmartNoise_mean_relative_error_0)*100, color = 'xkcd:moss green')
    ax2.plot(x2, abs(PyDP_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(PyDP_mean_relative_error_0)*100, color = 'xkcd:soft blue')
    ax2.plot(x2, abs(diffpriv_simple_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(diffpriv_simple_mean_relative_error_0)*100, color = 'xkcd:aquamarine')
    #ax2.plot(x2, abs(diffpriv_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none')
    #ax2.plot(epsilon, abs(diffpriv_mean_relative_error_0)*100, color = 'xkcd:grey')
    ax2.plot(x2, abs(chorus_mean_relative_error_0)*100, "o", markeredgecolor='k', mfc='none')
    ax2.plot(epsilon, abs(chorus_mean_relative_error_0)*100, color = 'xkcd:purple')
    #ax2.plot(x2, [float(additive_noise_mean_relative_error_0[0])*100]*73 , "o", markeredgecolor='k', mfc='none')
    #ax2.plot(epsilon, [float(additive_noise_mean_relative_error_0[0])*100]*73, color = 'k')

    ax2.plot(x2, abs(IBM_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none', label="scale = 10000")
    ax2.plot(epsilon, abs(IBM_mean_relative_error_1)*100, color = 'xkcd:orangish red')
    ax2.plot(x2, abs(SmartNoise_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(SmartNoise_mean_relative_error_1)*100, color = 'xkcd:moss green')
    ax2.plot(x2, abs(PyDP_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(PyDP_mean_relative_error_1)*100, color = 'xkcd:soft blue')
    ax2.plot(x2, abs(diffpriv_simple_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(diffpriv_simple_mean_relative_error_1)*100, color = 'xkcd:aquamarine')
    #ax2.plot(x2, abs(diffpriv_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none')
    #ax2.plot(epsilon, abs(diffpriv_mean_relative_error_1)*100, color = 'xkcd:grey')
    ax2.plot(x2, abs(chorus_mean_relative_error_1)*100, "s", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(chorus_mean_relative_error_1)*100, color = 'xkcd:purple')
    #ax2.plot(x2, [float(additive_noise_mean_relative_error_1[0])*100]*73 , "s", markeredgecolor='k', mfc='none')
    #ax2.plot(epsilon, [float(additive_noise_mean_relative_error_1[0])*100]*73, color = 'k')


    ax2.plot(x2, abs(IBM_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none', label="scale = 100000")
    ax2.plot(epsilon, abs(IBM_mean_relative_error_2)*100, color = 'xkcd:orangish red')
    ax2.plot(x2, abs(SmartNoise_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(SmartNoise_mean_relative_error_2)*100, color = 'xkcd:moss green')
    ax2.plot(x2, abs(PyDP_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(PyDP_mean_relative_error_2)*100, color = 'xkcd:soft blue')
    ax2.plot(x2, abs(diffpriv_simple_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(diffpriv_simple_mean_relative_error_2)*100, color = 'xkcd:aquamarine')
    #ax2.plot(x2, abs(diffpriv_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none')
    #ax2.plot(epsilon, abs(diffpriv_mean_relative_error_2)*100, color = 'xkcd:grey')
    ax2.plot(x2, abs(chorus_mean_relative_error_2)*100, "v", markeredgecolor='k',mfc='none')
    ax2.plot(epsilon, abs(chorus_mean_relative_error_2)*100, color = 'xkcd:purple')
    #ax2.plot(x2, [float(additive_noise_mean_relative_error_2[0])*100]*73 , "v", markeredgecolor='k', mfc='none')
    #ax2.plot(epsilon, [float(additive_noise_mean_relative_error_2[0])*100]*73, color = 'k')


    ax2.set_xlabel('ε', fontsize = 18)
    ax2.set_ylabel('Sample Mean of the \n Absolute Relative Error [%]', fontsize = 28)

    
    #ax1.legend(prop={'size': 19}, loc="lower center", bbox_to_anchor=(1.05, -0.59), frameon=False, ncol=2, handletextpad=0.2, handlelength=1, columnspacing=0.5)
    #ax2.legend(prop={'size': 24}, loc="lower center", bbox_to_anchor=(-0.17, -0.23), frameon=False, ncol=3, handletextpad=0.2)

    #legend_elements1 = [Line2D([0], [0],marker ='o', color='w', label = 'scale = 1000', markerfacecolor='k', markersize=15), Line2D([0], [0],marker = 's', color='w', label = 'scale = 10000', markerfacecolor='k', markersize=15),Line2D([0], [0],marker ='v', color='w', label = 'scale = 100000', markerfacecolor='k', markersize=15)]
    #figure.legend(prop={'size': 24},handles=legend_elements1, loc="lower center", bbox_to_anchor=(0.5, 0.04), frameon=False, ncol=3, handletextpad=0.2, handlelength=1)


    #figure.subplots_adjust(bottom=0.22)
    

    if query == 'count':
        ax1.set_ylim(10**-8, 10**3)
        if sets == 1:
            figure.suptitle('Count Query (Std = 50, Skew = 0)', fontsize=28)
        if sets == 2:
            figure.suptitle('Count Query (Std = 250, Skew = 0)', fontsize=28)
        if sets == 3:
            figure.suptitle('Count Query (Std = 500, Skew = 0)', fontsize=28)
        if sets == 4:
            figure.suptitle('Count Query (Std = 50, Skew = 5)', fontsize=28)
        if sets == 5:
            figure.suptitle('Count Query (Std = 250, Skew = 5)', fontsize=28)
        if sets == 6:
            figure.suptitle('Count Query (Std = 500, Skew = 5)', fontsize=28)
        if sets == 7:
            figure.suptitle('Count Query (Std = 50, Skew = 50)', fontsize=28)
        if sets == 8:
            figure.suptitle('Count Query (Std = 250, Skew = 50)', fontsize=28)
        if sets == 9:
            figure.suptitle('Count Query (Std = 500, Skew = 50)', fontsize=28)

    ax1.tick_params(axis='both', which='major', labelsize=25)
    ax2.tick_params(axis='both', which='major', labelsize=25)
    ax1.loglog()
    ax2.set_xscale('log')
    figure.set_size_inches(24, 9)

    plt.savefig('E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\plots_code\\plots\\querywise_plots\\{q}\\set_{set}.pdf'.format(q=query, set=sets))
    #plt.show()

Query = 'count'
result_folder_location = "E:\\MS_Thesis\\publication_stuff\\results_Jan_2021\\micro_13April_2021"
for sets in range(0,10):
    if sets == 1:
        first_dataset = 0
        second_dataset = 1
        third_dataset = 2
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 2:
        first_dataset = 3
        second_dataset = 4
        third_dataset = 5
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 3:
        first_dataset = 6
        second_dataset = 7
        third_dataset = 8
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 4:
        first_dataset = 9
        second_dataset = 10
        third_dataset = 11
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 5:
        first_dataset = 12
        second_dataset = 13
        third_dataset = 14
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 6:
        first_dataset = 15
        second_dataset = 16
        third_dataset = 17
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 7:
        first_dataset = 18
        second_dataset = 19
        third_dataset = 20
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 8:
        first_dataset = 21
        second_dataset = 22
        third_dataset = 23
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)
    if sets == 9:
        first_dataset = 24
        second_dataset = 25
        third_dataset = 26
        plots_with_sizes(result_folder=result_folder_location, query=Query, sets=sets, first_dataset=first_dataset, second_dataset=second_dataset, third_dataset=third_dataset)

