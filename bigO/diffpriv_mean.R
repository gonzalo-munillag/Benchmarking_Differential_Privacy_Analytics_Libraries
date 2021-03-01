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
        #gc()
        #Rprof("Rprof.out", memory.profiling=TRUE, interval = runif(1,.005,0.02))
        start.time <- Sys.time()
        target <- function(X) mean(X)
        sens = (maximum - minimum)/NROW(normal_distribution)
        mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims=1)
        pparams <- DPParamsEps(epsilon = eps)
        r <- releaseResponse(mechanism, privacyParams = pparams, X=normal_distribution)
        rr <- c(r$response)

        end.time <- Sys.time()
        time.taken <- round(end.time - start.time,5)
        #Rprof(NULL)
        #print(summaryRprof("Rprof.out", memory="both")$by.total$mem.total)
        print(time.taken) 
        write.table(time.taken, paste0("~/publication/bigO/results/diffpriv/mean_time_eps_",eps,"_dataset_",i,".csv"), append = T, row.names = F, col.names=F, eol = "\n") 
  }
} 
  
