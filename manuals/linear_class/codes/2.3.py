#Importing numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


#Function for generating coin toss
def coin(x):
	return 2*np.random.randint(2,size=x)-1
	

simlen = int(1e5)
N = np.random.normal(0,1,simlen)
S = coin(simlen)
A = 4
X = A*S+N
plt.plot(X,'o')
plt.xlabel('$Sample}$')
plt.ylabel('$X$')
plt.grid()
#If using termux
plt.savefig('../figs/bpsk.pdf')
plt.savefig('../figs/bpsk.eps')
subprocess.run(shlex.split("termux-open ../figs/bpsk.pdf"))
#else
#plt.show()

