
# Do I Get the Privacy I Need? Benchmarking Utility in Differential Privacy Libraries


## Overview
This repository contains the implementation of the paper. We are evaluating five differential privacy libraries' analytics queries (Count, sum, mean, var) on synthetic and real datasets.

### Differential Privacy Libraries:

1: (Python) IBM-diffprivlib. https://github.com/IBM/differential-privacy-library

2: (Python) OpenMined-PyDp. https://github.com/OpenMined/PyDP

3: (Python) OpenDP-SmartNoise. https://github.com/opendp/smartnoise-core

4: (R) diffpriv. https://github.com/brubinstein/diffpriv

5: (Scala) Chorus. https://github.com/uvm-plaid/chorus

## Folders in Repository

### Datasets

1) Normally distributed datasets
2) Real Datasets

### Bugs

1) Whitenoise (v 1.0.3)
2) diffpriv_count_query (sensitivity sampler)

### Libraries_Benchmark

1) Normally_distributed_dataset_experiments
2) Real_dataset_experiments

### Time_and_Memory_calculation

Contain code to calculate `Execution Time` and `Memory Consumed.`


- To run the code, kindly read the `README.md` file of each sub-folders.

### Results

These are some of the outputs of our benchmark:

#### Utility on synthetic datasets

Count

Sum

Mean

Var

#### Utility on real datasets

Count

Sum

Mean

Var

#### Execution time

#### Memery consumption


