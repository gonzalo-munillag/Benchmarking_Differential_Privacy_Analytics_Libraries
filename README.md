
# Do I Get the Privacy I Need? Benchmarking Utility in Differential Privacy Libraries

## Contributors

Development: [Aitsam Muhammad](https://github.com/aitsam12)   
Code supervision, experiment design, and scientific work: [Gonzalo Munilla Garrido](https://github.com/gonzalo-munillag)

## Overview
This repository contains the implementation of the paper "Do I Get the Privacy I Need? Benchmarking Utility in Differential Privacy Libraries". We are evaluating five differential privacy libraries' analytics queries (Count, sum, mean, var) on synthetic and real datasets across five open-source libraries.

### Differential Privacy Libraries:

1: (Python) IBM-diffprivlib. https://github.com/IBM/differential-privacy-library

2: (Python) OpenMined-PyDp. https://github.com/OpenMined/PyDP

3: (Python) OpenDP-SmartNoise. https://github.com/opendp/smartnoise-core

4: (R) diffpriv. https://github.com/brubinstein/diffpriv

5: (Scala) Chorus. https://github.com/uvm-plaid/chorus

## Folders in Repository

### Datasets

We have employed synthetic datasets to cover the breadth of possible features a dataset may have and real datasets to validate the libraries in a real setting. 

1) Skew-normal distributed datasets
2) Real Datasets

### Bugs

We include two of the bugs we encountered in some of the libraries while performing this benchmark.

1) Whitenoise (v 1.0.3)
2) diffpriv_count_query (sensitivity sampler)

### Libraries_Benchmark

In these folders, you may find the code to replicate our benchmark.

1) Normally_distributed_dataset_experiments
2) Real_dataset_experiments

### Time_and_Memory_calculation

Contains code to calculate `Execution Time` and `Memory Consumed` of the five libraries.

- To run the code, kindly read the `README.md` file of each sub-folders.

### Results

These are some of the outputs of our benchmark:

#### Utility on synthetic datasets

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/count/count-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/sum/sum-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/var/var-1.png" alt="drawing" width="300"/>

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/mean_merged/mean_merged-1.png" alt="drawing" width="300"/>


#### Utility on real datasets


Education Dataset: Absences (Count Query) 

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/absences_count/absences_count-1.png" alt="drawing" width="300"/>

Adult Dataset: Age (Variance Query) 

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/age_var/age_var-1.png" alt="drawing" width="325"/>


#### Execution time

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/count_time/count_time-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/sum_time/sum_time-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/mean_time/mean_time-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/var_time/var_time-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/legends-1.png" alt="drawing" width="300"/>

#### Memory consumption

<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/count_memory/count_memory-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/sum_memory/sum_memory-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/mean_memory/mean_memory-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/var_memory/var_memory-1.png" alt="drawing" width="300"/>
<img src="/Libraries_Benchmark/Normally_distributed_dataset_experiments/Results/images/legends-1.png" alt="drawing" width="300"/>
