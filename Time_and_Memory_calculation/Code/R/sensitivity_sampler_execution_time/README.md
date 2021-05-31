
##Comparing Execution Time of diffpriv (with Sampler) and diffpriv (without Sampler).


Open the `avg_time_diffpriv_sampler.py` and 
define the path to `micro` folder.


### Results in `sec`:

Scale = 1000

- diffpriv without sampler = 0.0007530508238699153
- diffpriv with sampler = 0.03992646543086172
- Difference = 0.039173414606991815

The sampler is circa 53 times slower.

Scale = 10000

- diffpriv without sampler = 0.0008588234802938819
- diffpriv with sampler = 0.2542956771944444
- Difference = 0.2534368537141506

The sampler is circa 296 times slower.

Scale = 100000

- diffpriv without sampler = 0.0010545282231128501
- diffpriv with sampler = 2.3278701230238252
- Difference = 2.3268155948007125

The sampler is circa 2208 times slower.
