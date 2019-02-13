#This program generates a Gaussian random no with 0 mean and unit variance

#Importing numpy
import numpy as np


simlen = int(1e5) #No of samples

n = np.random.normal(0,1,simlen)#Random vector

mean = np.sum(n)/simlen #Mean value

print (mean)

var = np.sum(np.square(n - mean*np.ones((1,simlen))))/simlen

print (var)
