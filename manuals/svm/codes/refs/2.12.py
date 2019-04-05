import numpy as np
import matplotlib.pyplot as plt


#Theoretical solution using Lagrange multipliers
A = np.matrix('8 0 3 2; 0 4 1 4; 3 1 0 0; 2 4 0 0')
b = np.matrix('0 ; 0 ; 8; 15')
sol = np.array(np.linalg.inv(A)*b)
r = np.sqrt(4*sol[0]**2+2*sol[1]**2)

print (sol)
print (r)

#Plotting the ellipse f
phi = np.linspace(0.0,2*np.pi,100)

alpha = r/2
beta  = r/np.sqrt(2)
x_line = alpha*np.cos(phi)
y_line = beta*np.sin(phi)

plt.plot(x_line,y_line,'b',label='$f(\mathbf{x})=4x_1^2 + 2x_2^2 = r^2$')

#Plotting g1
x1 = np.linspace(-5,5,100)
x2 = 8*np.ones(100)  - 3*x1 
plt.plot(x1,x2,'g',label='$g_1(\mathbf{x})=3x_1 + x_2 = 8$')

#Plotting g2
y1 = np.linspace(-5,5,100)
y2 = (15*np.ones(100) - 2*y1)/4
plt.plot(y1,y2,'r',label='$g_2(\mathbf{x})=4x_1 + 2x_2 = 15$')

plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc=3,prop={'size':12})

plt.xlim(-5, 5)
plt.ylim(-5, 5)

#Display solution 
A = sol[0]
B = sol[1]

plt.plot(A,B,'o')
for i,j in zip(A,B):
    plt.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
    plt.annotate('(%s,' %i, xy=(i,j))

#plt.savefig('../figs/2.12.eps')
plt.show()
