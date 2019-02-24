import numpy as np
import matplotlib.pyplot as plt


#Plotting log(x)
x = np.linspace(0.5,8,50)#points on the x axis
f=np.log(x)#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\ln x$')


#Plot commands
#Plotting line segments with x>0 and y=logx 
#color used to color each line with a different color
plt.plot([1,4],[np.log(1),np.log(4)],color=(1,0,0),marker='o',label="($1$,$\ln(1)$)-($4$,$\ln(4)$)")
plt.plot([2,6],[np.log(2),np.log(6)],color=(0,1,0),marker='o',label="($2$,$\ln(2)$)-($6$,$\ln(6)$)")
plt.plot([3,5],[np.log(3),np.log(5)],color=(0,0,1),marker='o',label="($3$,$\ln(3)$)-($5$,$\ln(5)$)")
plt.legend(loc=2)
#plt.savefig('../figs/1.3.eps')
plt.show()#Reveals the plot










