
### Bug diffpriv Count Query (Sensitivity Sampler)

Step 1 = open `utils_sensitivity_sampler.R`

- Line 7: specify `path_to_python`
- Line 13: specify location of `epsilon.pkl` (you can find it in python folder)
- Line 15: specify path to `micro` folder in `result_folder_location` (the `micro.zip` which you extracted to store results of python libraries)
- Line 212: specify path to synthetic dataset folder.

Step 2 = open `main.R`

- Line 8: give path to the `utils_sensitivity_sampler.R` file.
- Line 10: specify 'dataset_folder_path'

### Code running

run `Rscript main.R`



