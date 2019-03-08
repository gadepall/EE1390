import numpy as np
import matplotlib.pyplot as plt


#Plotting the circle
x = 8*np.ones(8)
y = 6*np.ones(8)
r = np.arange(8)/np.sqrt(2)
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis
# the first axis of these arrays varies the angle, 
# the second varies the circles
x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])

ax=plt.plot(x_line,y_line,'-')

#Plotting the line
x1 = np.linspace(-5,10,100)
x2 = 9*np.ones(100) - x1

x1_extend = np.linspace(0,20,100)
x2_extend = 22*np.ones(100) - x1_extend

bx=plt.plot(x1,x2,label="$x_1+x_2-9=0$")

plt.fill_between(x1_extend,x2_extend,color='grey')
plt.fill_between(x1,x2,color='white')
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend( loc='best')

plt.xlim(-5, 15)
plt.ylim(0, 22)


#plt.savefig('../figs/2.4.eps')
plt.show()









