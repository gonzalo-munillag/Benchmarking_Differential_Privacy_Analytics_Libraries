import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm

# 1) n = 1000 ; domain => std = 50  ; Skew = 0
data1= skewnorm.rvs(a = 0, loc=0, scale= 50, size=1000)

# 2) n = 1000 ; domain => std = 250  ; Skew = 5
data5= skewnorm.rvs(a = 5, loc=0, scale= 250, size=1000)

# 3) n = 1000 ; domain => std = 500  ; Skew = 50
data9= skewnorm.rvs(a = 50, loc=0, scale= 500, size=1000)
#########################################################

# 4) n = 10000 ; domain => std = 50  ; Skew = 0
data10= skewnorm.rvs(a = 0, loc=0, scale= 50, size=10000)

# 5) n = 10000 ; domain => std = 250  ; Skew = 5
data14= skewnorm.rvs(a = 5, loc=0, scale= 250, size=10000)

# 6) n = 10000 ; domain => std = 500  ; Skew = 50
data18= skewnorm.rvs(a = 50, loc=0, scale= 500, size=10000)
#########################################################

# 7) n = 100000 ; domain => std = 50  ; Skew = 0
data19= skewnorm.rvs(a = 0, loc=0, scale= 50, size=100000)

# 8) n = 100000 ; domain => std = 250  ; Skew = 5
data23= skewnorm.rvs(a = 5, loc=0, scale= 250, size=100000)

# 9) n = 100000 ; domain => std = 500  ; Skew = 50
data27= skewnorm.rvs(a = 50, loc=0, scale= 500, size=100000)
#########################################################


fig, axs = plt.subplots(3, 3, sharex=True)
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

textstr1 = 'Std = 50\nSkew = 0'
textstr2 = 'Std = 250\nSkew = 5'
textstr3 = 'Std = 500\nSkew = 50'

axs[0, 0].hist(data1, bins=100, color='k')
axs[0, 0].text(0.70, 0.76, textstr1, transform=axs[0,0].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
#axs[0, 0].set_title('Size = 1000', fontsize=8)
#axs[0, 0].get_yaxis().set_visible(False)
axs[0, 0].set_ylim(0,35)
axs[0, 1].hist(data5, bins=100, color='k')
axs[0, 1].text(0.68, 0.76, textstr2, transform=axs[0,1].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
#axs[0, 1].set_title('Size = 10000', fontsize=8)
axs[0, 1].set_ylim(0,35)
axs[0, 2].hist(data9, bins=100, color='k')
axs[0, 2].text(0.66, 0.76, textstr3, transform=axs[0,2].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
#axs[0, 2].set_title('Size = 100000', fontsize=8)
axs[0, 2].set_ylim(0,35)

axs[1, 0].hist(data10, bins=100, color='k')
axs[1, 0].text(0.70, 0.76, textstr1, transform=axs[1,0].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
#axs[1, 0].get_yaxis().set_visible(False)
axs[1, 0].set_ylim(0, 350)
axs[1, 1].hist(data14, bins=100, color='k')
axs[1, 1].text(0.68, 0.76, textstr2, transform=axs[1,1].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
axs[1, 1].set_ylim(0, 350)
axs[1, 2].hist(data18, bins=100, color='k')
axs[1, 2].text(0.66, 0.76, textstr3, transform=axs[1,2].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
axs[1, 2].set_ylim(0, 350)

axs[2, 0].hist(data19, bins=100, color='k')
axs[2, 0].text(0.70, 0.76, textstr1, transform=axs[2,0].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
#axs[2, 0].get_yaxis().set_visible(False)
axs[2, 0].set_ylim(0, 3500)
axs[2, 1].hist(data23, bins=100, color='k')
axs[2, 1].text(0.68, 0.76, textstr2, transform=axs[2,1].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)
axs[2, 1].set_ylim(0, 3500)
axs[2, 2].hist(data27, bins=100, color='k')
axs[2, 2].set_ylim(0, 3500)
axs[2, 2].text(0.66, 0.76, textstr3, transform=axs[2,2].transAxes, fontsize=6, verticalalignment='bottom', bbox=props)

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
    #ax.set_ylim([0.00, 0.01])

#fig.text(0.5, 0.92, 'Normally Distributed Datasets', ha='center')
fig.text(0.5, 0.03, 'Domain', ha='center')
fig.text(0.04, 0.5, 'Frequency', va='center', rotation='vertical')
fig.text(0.01, 0.7, 'size = 1000', rotation='vertical')
fig.text(0.01, 0.5, 'size = 10000', va='center', rotation='vertical')
fig.text(0.01, 0.13, 'size = 100000', rotation='vertical')
plt.show()
