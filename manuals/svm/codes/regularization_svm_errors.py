from cvxpy import *
import numpy as np

import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

fig,ax = plt.subplots()

# x is array of datapoints stacked column wise [x1, x2, ... , xn]
x = 100*np.array([
	[ 1.0, 1.0, 2.0, 2.0, 4.0, 4.0, 5.0, 5.0, 4.5] , 
	[ 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 2.0]
	])

# y is matrix with labels stacked diagonally
y = np.diag([1,1,1,1,-1,-1,-1,-1,1])

#plotting datapoints
ax.scatter(x[0,:4],x[1,:4],marker="X",color='red',label="y= 1")
ax.scatter(x[0,4:-1],x[1,4:-1],label="y= -1")
ax.scatter(x[0,-1],x[1,-1],marker="X",color='red')

n=9 #no of datapoints
p=2 #dimension of each datapoint

C=5

d= Variable()
d_v = np.ones((n,1))*d
#broadcasted d into a vector d_v

w = Variable((p,1),nonneg=False)
xi = Variable((n,1),nonneg=True)

#objective function 
obj = Minimize(0.5*square(norm(w)) + C*np.ones((n,1)).T@xi)

#constraints in matrix form
constraints = [((x@y).T)@w + y@d_v>= np.ones((n,1)) - xi]

Problem(obj, constraints).solve()
print("Minimum value of Cost function= ", obj.value)
print("Minima is at w = \n",w.value)
print("Minima is at d= ",d.value)

w1,w2 = w.value[0,0], w.value[1,0]
print(-w1/w2)


xx = np.linspace(0,500,100)
plt.plot(xx,(w1*xx+d.value)/(-w.value[1,0]),label="Hyperplane(C="+str(C)+")")
plt.ylim(0.0,300.0)
plt.legend(loc='upper left')
#If using termux
plt.savefig('../figs/svm_C_opt.pdf')
plt.savefig('../figs/svm_C_opt.eps')
subprocess.run(shlex.split("termux-open ../figs/svm_C_opt.pdf"))
#else
#plt.show()

