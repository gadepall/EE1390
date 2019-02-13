#Importing numpy
import numpy as np

#Function for generating coin toss
def coin(x):
	return 2*np.random.randint(2,size=x)-1
	


print (coin(1))


