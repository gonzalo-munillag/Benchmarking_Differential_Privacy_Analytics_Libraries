from IBM_diffprivlib import diffprivlib_real_dataset

from openmined_pydp import openmind_pydp_real_dataset

#library_name = 'diffprivlib'    # libraries (string): 'diffprivlib', 'openmind_pydp'
dataset_folder_path = '/home/aitsam/publication/files/real_datasets/' # path to the dataset folder
#attribute = 'age'    # age, hrs, absences, grade
#query = 'var'           # query could be (string): count, sum, mean, var 
total_experiments = 500

attribute_list = ['age', 'hrs', 'absences', 'grade']
query_list = ['count', 'sum', 'mean', 'var']
library_list = ['diffprivlib', 'openmind_pydp']

for library_name in library_list:
    for attribute in attribute_list:
        for query in query_list:
            print('{l} library, attribute  {a}  calculating results for query  {q}'.format(l=library_name, a=attribute, q=query))
            eval(library_name + '_real_dataset')(dataset_folder_path= dataset_folder_path, attribute=attribute, query_name= query, number_of_experiments=total_experiments)
