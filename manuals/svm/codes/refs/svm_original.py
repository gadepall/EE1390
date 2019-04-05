from cvxpy import *
import numpy as np
x1 = np.matrix([[ 2.0], [1.0 ]])
x2 = np.matrix([[ 0.8], [-0.6 ]])
y1 = 1.0
y2 = -1.0
d= Variable()
w = Variable((2,1),nonneg=False)
f = 0.5*(w[0]**2 + w[1]**2)
obj = Minimize(f)
constraints = [ y1* (x1.transpose() * w + d) >=1 , y2* (x2.transpose() * w + d) >=1 ]
Problem(obj, constraints).solve()
print("Minimum value of Cost function= ", f.value)
print("Minima is at w = \n",w.value)
print("Minima is at d= ",d.value)