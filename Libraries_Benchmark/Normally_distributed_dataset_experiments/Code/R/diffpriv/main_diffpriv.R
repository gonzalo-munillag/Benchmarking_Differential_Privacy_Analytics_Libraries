#import Libraries
library(rio)
library(diffpriv)
library(tidyverse)
library(fs)
library(reticulate)

source("E:/MS_Thesis/publication_stuff/refactored_code/diffpriv_R/utils_diffpriv.R")

results <- diffpriv_single_query(number_of_csv_file=2, number_of_experiments= 1, dataset_folder_path = "E:/MS_Thesis/publication_stuff/refactored_code/diffpriv_R", query_name="var")

