import numpy as np
import scipy 
import matplotlib.pyplot as plt
import subprocess
import shlex


def sq(x):
	return x**2

#Plotting the parabola
x = np.linspace(-5,5,50)#points on the x axis
vec_sq = scipy.vectorize(sq)
f=vec_sq(x)#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\ln x$')

#Convexity/Concavity
a = -3
b = 4
lamda = 0.3
c = lamda *a + (1-lamda)*b
f_a = sq(a)
f_b = sq(b)

f_c = sq(c)
f_c_hat = lamda *f_a + (1-lamda)*f_b

#Plot commands
plt.plot([a,a],[0,f_a],color=(1,0,0),marker='o',label="$f(a)$")
plt.plot([b,b],[0,f_b],color=(0,1,0),marker='o',label="$f(b)$")
plt.plot([c,c],[0,f_c],color=(0,0,1),marker='o',label="$f(\lambda a + (1-\lambda)b)$")
plt.plot([c,c],[0,f_c_hat],color=(1/2,2/3,3/4),marker='o',label="$\lambda f(a) + (1-\lambda)f(b)$")
plt.plot([a,b],[f_a,f_b],color=(0,1,1))
plt.legend(loc=2)
plt.savefig('../figs/1.2.pdf')
subprocess.run(shlex.split("termux-open ../figs/1.2.pdf"))
#plt.show()#Reveals the plot








