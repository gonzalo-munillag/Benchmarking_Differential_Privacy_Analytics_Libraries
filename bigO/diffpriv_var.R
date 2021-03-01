#import Libraries
library(rio)
library(diffpriv)
library(tidyverse)
library(fs)
library(reticulate)
path_to_python <- "/Users/Aitsam/AppData/Local/Programs/Python/Python38/python.exe"
use_python(path_to_python)

pd <- import("pandas")


epsilon <- c(0.1, 1.0, 10.0)
number_of_csv_file = 3

                                                                                                                                                                            
data <- list()
for (i in 0:number_of_csv_file) {

  data <- read_csv(file = paste0("dataset_",i,".csv"), col_names = "X1")
  print(paste0("DATASET = ",i))
  normal_distribution <- data$X1
  maximum = max(normal_distribution)
  minimum = min(normal_distribution)

  for (eps in epsilon){
        start.time <- Sys.time()
        target <- function(X) var(X)
        sens = (((maximum - minimum)/NROW(data))^2)*(NROW(data)-1)
        mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims=1)
        pparams <- DPParamsEps(epsilon = eps)
        r <- releaseResponse(mechanism, privacyParams = pparams, X=normal_distribution)
        rr <- c(r$response)

        end.time <- Sys.time()
        time.taken <- round(end.time - start.time,5)
        print(time.taken) 
        write.table(time.taken, paste0("~/publication/bigO/results/diffpriv/var_time_eps_",eps,"_dataset_",i,".csv"), append = T, row.names = F, col.names=F, eol = "\n") 
  }
} 
  
