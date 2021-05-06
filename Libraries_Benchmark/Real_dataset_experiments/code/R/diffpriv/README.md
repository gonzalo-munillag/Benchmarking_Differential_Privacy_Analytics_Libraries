
# (R) Differential privacy libraries benchmark on real datasets

## Folder `diffpriv`

Step 1 = open `utils.R`
- Line 7: specify `path_to_python`
- Line 13: specify location of `epsilon.pkl` (you can find it in python folder)
- Line 15: specify path to `micro` folder in `result_folder_location` (the `micro.zip` which you extracted to store results of python libraries)
- Line 218: specify path to age_adult.csv.
- Line 229: specify path to hrs_adult.csv.
- Line 241: specify path to absences_education.csv.
- Line 250: specify path to grade_education.csv.

`main.R`
- Line 8: give path to the `utils.R` file.
- Line 10: specify 'dataset_folder_path' and 'query'

### Code running

run `Rscript main.R`

(run it for all the queries for each atrribute. Results will get save in `micro/diffpriv_simple/`)

