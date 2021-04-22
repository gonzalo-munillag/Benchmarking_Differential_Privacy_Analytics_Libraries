#import Libraries
library(rio)
library(diffpriv)
library(tidyverse)
library(fs)
library(reticulate)

source("~/publication/bigO/single_query_analysis/diffpriv_R/without_sampler_code/utils.R")

results <- diffpriv_single_query(number_of_csv_file=6, number_of_experiments= 3, dataset_folder_path = "~/publication/bigO", query_name="count")



