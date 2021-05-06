
# (R) Differential Privacy Libraries Analysis for Sythetic Datasets

## Folder `diffpriv`

## Execution Time

Step 1 = open `utils.R`
- Line 7: specify `path_to_python`
- Line 13: specify location of `epsilon.pkl` (you can find it in python folder)
- Line 15: specify path to `micro` folder in `result_folder_location` (the `micro.zip` which you extracted to store results of python libraries)
- Line 216: specify path to synthetic dataset folder.

`main.R`
- Line 8: give path to the `utils.R` file.
- Line 10: specify 'dataset_folder_path' and 'query'

### Code running

run `Rscript main.R`

(run it for all the queries. Results will get save in `micro/diffpriv_simple/`)

## Memory Consumed

Step 1 = open `memory_diffpriv.R`
- Line 9: specify `dataset_folder_path`
- Line 11: specify `query`
- Line 33 - 38: Modify according to desired query. 
- Line 47, 50, 53: create two empty folder `memory_Diffpriv` and `AVG_memory_Diffpriv` to save the results. Also make sure you specify the correct path to these folders.
