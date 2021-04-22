library(rio)
library(diffpriv)
library(tidyverse)
library(fs)
library(profmem)
library(pryr)
library(profvis)

dataset_folder_path = '~/publication/bigO'
number_of_csv_file = 6
query <- 'var'
data <- list()

for(f in 0:number_of_csv_file){
  print(paste0('results for dataset = ',f))
  data <- read_csv(file = paste0(dataset_folder_path,"/dataset_",f,".csv"), col_names = "X1")
  normal_distribution <- data$X1
  
  maximum = max(normal_distribution)
  minimum = min(normal_distribution)
  epsilons_l <- c(0.1, 1.0, 10.0)
  
  for (eps in epsilons_l){
    print(paste0('calculating results for epsilon = ',eps))
    
    for (itr in 0:100){
      #print(paste0('iteration = ',itr))
      gc()
      # Start profiler
      Rprof(tf <- paste0("Rprof_",f,".out"), line.profiling = TRUE,
            gc.profiling = TRUE, memory.profiling = TRUE)
      for (i in 0:100){
        target <- function(X) var(X)
        mech <- DPMechLaplace(target = target)
        #target <- function(X) NROW(X)
        #sens = (maximum - minimum)/NROW(data)
        sens = (((maximum - minimum)/NROW(data))^2)*(NROW(data)-1)
        #sens = maximum -minimum
        mechanism <- DPMechLaplace(target = target, sensitivity = sens, dims = 1)
        pparams <- DPParamsEps(epsilon = eps) 
        r <- releaseResponse(mechanism, privacyParams = pparams, X=normal_distribution)
        rr <- c(r$response)
        #print(rr)
      }
      Rprof(NULL)
      mem <- (max(summaryRprof(tf, memory="both")$by.total$mem.total)/100)*1000000000
      write.table(mem, paste0("~/publication/bigO/memory_Diffpriv/",query,"_",eps,"_memory_dataset_",f,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
      #print((max(summaryRprof(tf, memory="both")$by.total$mem.total)/100)*1000000000)
    }
    memory_csv <- read.csv(paste0("~/publication/bigO/memory_Diffpriv/",query,"_",eps,"_memory_dataset_",f,".csv"))
    memory_mean <- mean(memory_csv$X)
    print(memory_mean)
    write.table(memory_mean, paste0("~/publication/bigO/AVG_memory_Diffpriv/",query,"/eps_",eps,"_memory_dataset_",f,".csv"), append = T, row.names = F, col.names=F, eol = "\n")
    
  }

}


