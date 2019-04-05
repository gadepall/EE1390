import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull




#Vertices of the convex polygon formed by intersection of the constraints
points = np.array([[0, 0], [0, 5],[2, 3], [4,0]])
#Filling up the polygon
plt.fill(points[:,0], points[:,1], 'k', alpha=0.3)


#Plotting the set of possible cost functions

p = 9*np.arange(1,5)
print (p)
x = np.linspace(0,4,100);
na=np.newaxis

x_line = x[:,na]
y_line = p[na,:]/5.0 - 6.0/5.0*x[:,na]
bx=plt.plot(x_line,y_line,'-')





#Plotting the first constraint
x1 = np.linspace(0,4,100)
x2 = 5*np.ones(100) - x1

ax=plt.plot(x1,x2)


#plotting the second constraint
x2 = 6*np.ones(100) - 3.0/2.0*x1

cx=plt.plot(x1,x2)

#Displaying solution on graph
sol = np.zeros((2,1))
sol[0] = 2
sol[1] = 3

#Display solution 
A = sol[0]
B = sol[1]


plt.plot(A,B,'o')
for xy in zip(A,B):
	plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend([bx[2], ax[0], cx[0]],['$6x_1+5x_2=27$', '$x_1+x_2=5$','$3x_1+2x_2=12$'], loc='best',prop={'size':11})
plt.xlim(0,4)
plt.ylim(0,5)
plt.savefig('../figs/4.1.eps')
plt.savefig('../figs/4.1.pdf')
plt.show()










