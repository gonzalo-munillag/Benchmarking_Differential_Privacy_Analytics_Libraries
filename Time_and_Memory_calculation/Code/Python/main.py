from IBM_diffprivlib import diffprivlib_single_query
from smartnoise import smartnoise_single_query
from openmined_pydp import openmind_pydp_single_query

library_name = 'smartnoise'    # libraries: 'difforivlib', 'smartnoise', additive_noise', 'openmined_pydp'
dataset_folder_path = 'E:\\MS_Thesis\\publication_stuff\\car_datasets\\gaussian_datasets\\' # path to the dataset folder
number_of_csv_files = 7    # number of csv files in dataset folder
query = 'variance'           # query could be = count, sum, mean, var (for smartnoise: variance)
total_experiments = 500 

eval(library_name + '_single_query')(dataset_folder_path= dataset_folder_path, 
            number_of_csv_files=number_of_csv_files, query_name= query, number_of_experiments=total_experiments)
