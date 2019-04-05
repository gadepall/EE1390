import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

x = np.zeros(4)
y = np.zeros(4)
r = np.arange(4)
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis

x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])/2
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])/2
ax=plt.plot(x_line,y_line)
w1 = np.linspace(-2,2,100)

d = 0
w21 = (0.8*w1 + 1 + d)/0.6
w22 = (1-d-2*w1)
plt.plot(w1,w21,color = 'b')
plt.plot(w1,w22,color = 'b')

d = -0.5
w21 = (0.8*w1 + 1 + d)/0.6
w22 = (1-d-2*w1)
plt.plot(w1,w21,color = 'r')
plt.plot(w1,w22,color = 'r')

d = -1
w21 = (0.8*w1 + 1 + d)/0.6
w22 = (1-d-2*w1)
plt.plot(w1,w21,color = 'y',label = '$0.8x_1 - 0.6x_2 = 0$')
plt.plot(w1,w22,color = 'g',label = '$2x_1 + x_2 = 2$')

plt.axis([-2, 2, -2, 2])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.xlabel('$w_1$')
plt.ylabel('$w_2$')
plt.legend(loc='best')

A = [0.6]
B = [0.8]

plt.plot(A,B,'o')
for xy in zip(A, B):                                       
    plt.annotate('(%.4s, %.4s)' % xy, xy=xy, textcoords='data') 
#If using termux
plt.savefig('../figs/svm_graph.pdf')
plt.savefig('../figs/svm_graph.eps')
subprocess.run(shlex.split("termux-open ../figs/svm_graph.pdf"))
#else
#plt.show()










