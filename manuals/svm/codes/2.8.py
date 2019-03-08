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
x1 = np.linspace(5,15,100)
x2 = 18*np.ones(100) - x1
bx=plt.plot(x1,x2)
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend([ax[4], bx[0]],['$(x_1-8)^2+(x_2 -6)^2=8$','$x_1+x_2-18=0$'], loc='best')

#plt.savefig('../figs/2.8.eps')
plt.show()









