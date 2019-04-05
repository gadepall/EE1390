import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#If using termux
import subprocess
import shlex
#end if


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = np.linspace(-5,5,10)
x2 = np.linspace(-5,5,10)

X1,X2 = np.meshgrid(x1,x2)

f = X1**2 + X2**2

ax.plot_surface(X1,X2,f,rstride=1, cstride=1,
                cmap='viridis')
f1 = 1-2*X1-X2

ax.plot_wireframe(X1,X2,f1,color = 'grey')

f2 = -1 - 0.8*X1 + 0.6*X2

ax.plot_wireframe(X1,X2,f2,color = 'grey')

ax.scatter3D(0.6,0.8,-1,s=100,c='red')
ax.text(0.6,0.8,-1,  '%s' % (str('0.6,0.8,-1')), size=15, zorder=1,color='red')
#ax.plot_wireframe(X1,X2,f1,color = 'red')
ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_zlabel('d' )
for angle in range(360):
    
    ax.view_init(0,angle)
    plt.draw()
    plt.pause(.001)

#plt.title('Plane joining the points (5,0),(0,5),(-5,0),(0,-5) \nlies above as well as below the surface\n Hence the function is neither concave nor convex ')
#If using termux
plt.savefig('../figs/xnyn.pdf')
plt.savefig('../figs/xnyn.eps')
subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
#else
#plt.show()
