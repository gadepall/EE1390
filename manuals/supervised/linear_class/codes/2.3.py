#Importing numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt


#Function for generating coin toss
def coin(x):
	return 2*np.random.randint(2,size=x)-1
	

simlen = int(1e5)
N = np.random.normal(0,1,simlen)
X = coin(simlen)
A = 4
Y = A*X+N

plt.plot(Y,'o')
plt.xlabel('$Sample}$')
plt.ylabel('$Y$')
plt.grid()
plt.show()

