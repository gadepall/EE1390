#Code by Rohit Reddy
#July 4, 2019
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

x=np.linspace(-10,10,50)

y=1/(1+np.exp(-x))

plt.plot(x,y)
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
#if using termux
plt.savefig('../figs/sigmoid.pdf')
plt.savefig('../figs/sigmoid.eps')
subprocess.run(shlex.split("termux-open ../figs/sigmoid.pdf"))
#else
#plt.show()

