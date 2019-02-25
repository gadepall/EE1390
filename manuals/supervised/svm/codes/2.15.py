import numpy as np
import matplotlib.pyplot as plt


sol = np.zeros((2,1))
#Printing minimum
sol[0] = (np.sqrt(2)-1)/(2*np.sqrt(2))
sol[1] = -1/(2*np.sqrt(2))


#Plotting the circle

circle = plt.Circle((0.5, 0), 0.5, color='r', fill=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot

ax.add_artist(circle)

#Display solution 
A = np.around(sol[0],decimals=2)
B = np.around(sol[1],decimals=2)


plt.plot(A,B,'o')
for xy in zip(A,B):
	ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

print (sol)


#Plotting the line
p = (sol[0]+sol[1])*np.arange(-2,3)
x = np.linspace(0,1,100)
na=np.newaxis

x_line = x[:,na]
y_line = p[na,:] - x[:,na]
bx=plt.plot(x_line,y_line,'-')


plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.ylim(-0.5,0.5)

plt.legend([bx[3]],['$x_1+x_2=\\frac{\sqrt{2}-2}{2\sqrt{2}}$'], loc='best',prop={'size':11})
#plt.savefig('../figs/2.15.eps')
plt.show()










