#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt



maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e5) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
n = np.random.normal(0,1,simlen)

for i in range(0,maxrange):
	err_ind = np.nonzero(n < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_gauss_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.show() #opening the plot window

