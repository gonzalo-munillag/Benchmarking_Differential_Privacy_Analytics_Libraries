
import numpy as np
from scipy.stats import skewnorm
import itertools

# ## Goal: We would like to create different arrays that represent different characteristic combinations in terms of scale (number of elements, sample size), domain (the range of values the elements of the array take, std), and shape (how imbalanced the dataset is, skewness)

# ## Levels:
# ### Scale: 1000, 10000, 100000
# ### Domain: std= 50, std=250, std=500
# ### Shape: skew = 0, skew = 5, skew = 50
# ## We define three levels for each of these terms, yielding 27 possible combinations. We will later on apply differencial privacy mechanism to the arrays to test how the error is affected by these characteristics (scale, domain, shape).
# ## This notebook only shows how to tune each of the parameters of a normal distribution created with scipy 
# ### Funciton to be used:  skewnorm.rvs(a => for skewness, loc=> for mean, scale => for std, size => scale)
# ### Let us not confuse the term SCALE from the beginning with the input of the function called scale, which means std
# ### Here is how you change the SCALE, the number of samples (size input)

def dataset_generation(a, scale, size, f):
    data= skewnorm.rvs(a = a, loc=0, scale= scale, size=size)
    for i in data:
        guestFile = open("synthetic_datasets/dataset_{}.csv".format(f),"a")
        guestFile.write(str ("%.4f"% (i)))
        guestFile.write("\n")
        guestFile.close()

a = [[5],[250],[10, 100, 1000, 10000,100000,1000000,10000000]]
all_combinations = list(itertools.product(*a))
print(all_combinations)

for v in range(len(all_combinations)):
    c = all_combinations[v]
    s = c[0]
    t = c[1]
    u = c[2]
    print('Genrating dataset for {}'.format(all_combinations[v]))
    dataset_generation(s,t,u,v)


