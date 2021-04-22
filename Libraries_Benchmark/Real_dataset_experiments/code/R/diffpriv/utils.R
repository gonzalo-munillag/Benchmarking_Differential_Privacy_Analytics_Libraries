#import Libraries
library(rio)
library(diffpriv)
library(tidyverse)
library(fs)
library(reticulate)
path_to_python <- "/Users/Aitsam/AppData/Local/Programs/Python/Python38/python.exe"
use_python(path_to_python)

pd <- import("pandas")


epsilon <- pd$read_pickle("~/publication/files/epsilon.pkl")


log_errors <- function(dataset_folder_path, query, i, eps) {
  # mean error
  err <- read.csv(paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/error/DP_error_eps_",eps,".csv"))
  #mean_err <- sapply(err$X, mean)
  mean_err <- mean(err$X)
  print(mean_err)
  write.table(mean_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/mean_error/mean_error.csv"), append = T, row.names = F, col.names=F, eol = "\n")

  # mean scaled error
  scaled_err <- read.csv(paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/scaled_error/DP_scaled_error_eps_",eps,".csv"))
  mean_scaled_err <- mean(scaled_err$X)
  print(mean_scaled_err)
  write.table(mean_scaled_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/mean_scaled_error/mean_scaled_error.csv"), append = T, row.names = F, col.names=F, eol = "\n")

  # mean relative error
  relative_err <- read.csv(paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/relative_error/DP_relative_error_eps_",eps,".csv"))
  #print(relative_err)
  mean_relative_err <- mean(relative_err$X)
  print(mean_relative_err)
  write.table(mean_relative_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/mean_relative_error/mean_relative_error.csv"), append = T, row.names = F, col.names=F, eol = "\n")

  # std relative error
  std_relative_err <- sd(relative_err$X)
  print(std_relative_err)                                                                                                                                                
  write.table(std_relative_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/std_relative_error/std_relative_error.csv"), append = T, row.names = F, col.names=F, eol = "\n") 

  # std error
  std_err <- sd(err$X)
  print(std_err)
  write.table(std_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/std_error/std_error.csv"), append = T, row.names = F, col.names=F, eol = "\n")
  # std scaled error
  std_scaled_err <- sd(scaled_err$X)
  print(std_scaled_err)
  write.table(std_scaled_err, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/std_scaled_error/std_scaled_error.csv"), append = T, row.names = F, col.names=F, eol = "\n")
  # time consumption
  t <- read.csv(paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/time/time_eps_",eps,".csv"))
  time_taken <- mean(t$X)
  write.table(time_taken, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/",query,"/results_dataset_",i,"/execution_time.csv"), append = T, row.names = F, col.names=F, eol = "\n")
  
  }



calculate_dp_sum <- function(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum) {
  print(paste0("calculated results (SUM QUERY) for dataset = ",i," and epsilon = ",eps," completed"))
  
  time_taken <- c()
  replicate(
    number_of_experiments,
    {
      start.time <- Sys.time()
      
      target <- function(X) sum(X)
      sens = maximum - minimum
      mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims=1)
      pparams <- DPParamsEps(epsilon = eps) 
      r <- releaseResponse(mechanism, privacyParams = pparams, X=data)
      rr <- c(r$response)
      
      end.time <- Sys.time()
      time.taken <- round(end.time - start.time,5)
      #print(time.taken)
      write.table(round(end.time - start.time,5), paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/sum/results_dataset_",i,"/time/time_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      write.table(rr, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/sum/results_dataset_",i,"/dp/DP_count_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      true_sum <- sum(data)
      #print(rr)
      #print(paste0("true sum = ",true_sum))
      error <- true_sum - rr
      write.table(error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/sum/results_dataset_",i,"/error/DP_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      relative_error <- abs((true_sum - rr)/true_sum)
      #print(relative_error)
      write.table(relative_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/sum/results_dataset_",i,"/relative_error/DP_relative_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      scaled_error <- abs(error/NROW(data))
      write.table(scaled_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/sum/results_dataset_",i,"/scaled_error/DP_scaled_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
    }
  )
}

calculate_dp_var <- function(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum) {
  print(paste0("calculated results (VAR QUERY) for dataset = ",i," and epsilon = ",eps," completed"))
  
  time_taken <- c()
  replicate(
    number_of_experiments,
    {
      start.time <- Sys.time()
      
      target <- function(X) var(X)
      sens = (((maximum - minimum)/NROW(data))^2)*(NROW(data)-1)
      mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims=1)
      pparams <- DPParamsEps(epsilon = eps) 
      r <- releaseResponse(mechanism, privacyParams = pparams, X=data)
      rr <- c(r$response)
      
      end.time <- Sys.time()
      time.taken <- round(end.time - start.time,5)
      write.table(round(end.time - start.time,5), paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/var/results_dataset_",i,"/time/time_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      #print(time.taken)
      
      write.table(rr, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/var/results_dataset_",i,"/dp/DP_count_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      true_var <- var(data)
      
      error <- true_var - rr
      write.table(error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/var/results_dataset_",i,"/error/DP_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      relative_error <- abs((true_var - rr)/true_var)
      write.table(relative_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/var/results_dataset_",i,"/relative_error/DP_relative_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")

      scaled_error = abs((error)/NROW(data))
      write.table(scaled_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/var/results_dataset_",i,"/scaled_error/DP_scaled_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
    }
  )
}

calculate_dp_mean <- function(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum) {
  print(paste0("calculated results (MEAN QUERY) for dataset = ",i," and epsilon = ",eps," completed"))
  
  time_taken <- c()
  replicate(
    number_of_experiments,
    {
      start.time <- Sys.time()
      
      target <- function(X) mean(X)
      sens = (maximum - minimum)/NROW(data)
      mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims = 1)
      pparams <- DPParamsEps(epsilon = eps) 
      r <- releaseResponse(mechanism, privacyParams = pparams, X=data)
      rr <- c(r$response)
      
      end.time <- Sys.time()
      time.taken <- round(end.time - start.time,5)
      write.table(round(end.time - start.time,5), paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/mean/results_dataset_",i,"/time/time_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      #print(time.taken)
      
      
      write.table(rr, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/mean/results_dataset_",i,"/dp/DP_count_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      #true_mean <- sapply(data, mean)
      true_mean <- mean(data)
      #print(true_mean)
      error <- true_mean - rr
      #print(error)      
      write.table(error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/mean/results_dataset_",i,"/error/DP_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")

      relative_error <- abs((true_mean - rr)/true_mean)
      #print(paste0('Relative error ',relative_error))
      write.table(relative_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/mean/results_dataset_",i,"/relative_error/DP_relative_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")

      scaled_error <- abs(error/NROW(data))
      write.table(scaled_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/mean/results_dataset_",i,"/scaled_error/DP_scaled_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
    }
  )
  
}

calculate_dp_count <- function(data, number_of_experiments, dataset_folder_path, query_name, eps, i) {
  print(paste0("calculated results (COUNT QUERY) for dataset = ",i," and epsilon = ",eps," completed"))
  
  time_taken <- c()
  replicate(
    number_of_experiments,
    {
      start.time <- Sys.time()
      
      target <- function(X) NROW(X)
      mechanism <- DPMechLaplace(target = target, sensitivity = 1, dims = 1)
      pparams <- DPParamsEps(epsilon = eps) 
      r <- releaseResponse(mechanism, privacyParams = pparams, X = data)
      rr <- c(r$response)
      #print(rr)
      end.time <- Sys.time()
      time.taken <- round(end.time - start.time,5)
      #print(time.taken)
      write.table(round(end.time - start.time,5), paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/count/results_dataset_",i,"/time/time_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
      write.table(rr, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/count/results_dataset_",i,"/dp/DP_count_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      error <- NROW(data) - rr
      #print(NROW(data) - rr)
      write.table(error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/count/results_dataset_",i,"/error/DP_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")

      relative_error <- abs((NROW(data) - rr)/NROW(data))
      write.table(relative_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/count/results_dataset_",i,"/relative_error/DP_relative_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n") 

      scaled_error <- abs(error/NROW(data))
      write.table(scaled_error, paste0("~/publication/real_dataset_analysis/micro/diffpriv_simple/count/results_dataset_",i,"/scaled_error/DP_scaled_error_eps_",eps,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      
    }
  )
  
}

diffpriv_real_dataset <- function(attribute, number_of_experiments, dataset_folder_path, query_name) {

    if (attribute == "age") {

      data_age <- read_csv(file = paste0("~/publication/files/real_datasets/age_adult.csv"), col_names = "X1", skip = 1)
      #data <- data_age
      data <- as.numeric(data_age$X1)
      #print(as.numeric(data$X1))
      maximum = 100.0
      minimum = 0.0
      i = 1
      #print(data)
    }
    if (attribute == "hrs") {

      data_hrs <- read_csv(file = paste0("~/publication/files/real_datasets/hrs_adult.csv"), col_names = "X1", skip = 1, )
      data <- as.numeric(data_hrs$X1)
      data <- function(data, UB=80, LB=0) pmax( LB, pmin( vec, UB))    #ref: https://stackoverflow.com/questions/13868963/clip-values-between-a-minimum-and-maximum-allowed-value-in-r
      #print(data)
      maximum = 80.0
      minimum = 0.0
      i = 2
      #print(data)
    }

  if (attribute == "absences") {

    data_abs <- read_csv(file = paste0("~/publication/files/real_datasets/absences_education.csv"), col_names = "X1", skip = 1)
    data <- as.numeric(data_abs$X1)
    maximum = 93.0
    minimum = 0.0
    i = 3
    #print(data)
  }
  if (attribute == "grade") {

    data_grade <- read_csv(file = paste0("~/publication/files/real_datasets/grade_education.csv"), col_names = "X1", skip = 1)
    data <- as.numeric(data_grade$X1)
    maximum = 20.0
    minimum = 0.0
    i = 4
    #print(data)
  }


    
    for (eps in epsilon) {
 
      if (query_name == "count") {
        calculate_dp_count(data, number_of_experiments, dataset_folder_path, query_name, eps, i)
      } else if (query_name == "sum") {
        calculate_dp_sum(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum)
      } else if (query_name == "var") {
        calculate_dp_var(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum)
      } else if(query_name == "mean") {
        calculate_dp_mean(data, number_of_experiments, dataset_folder_path, query_name, eps, i, maximum, minimum)
      }
      
      log_errors(dataset_folder_path, query=query_name, i, eps)
    }
  
  
  
}



