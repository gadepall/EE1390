from cvxpy import *
import numpy as np

# x is array of datapoints stacked column wise [x1, x2, ... , xn]
x = np.array([
	[ 2.0, 0.8 ] , 
	[ 1.0, -0.6 ]
	])

# y is matrix with labels stacked diagonally
y = np.diag([1,-1])

n=2 #no of datapoints
p=2 #no of parameters of each datapoint

d= Variable()
d_v = np.ones((p,1))*d
#broadcasted d into a vector d_v

w = Variable((p,1),nonneg=False)

#objective function 
obj = Minimize(0.5*square(norm(w)))

#constraints
constraints = [((x@y).T)@w + y@d_v>= np.ones((n,1))]

Problem(obj, constraints).solve()
print("Minimum value of Cost function= ", obj.value)
print("Minima is at w = \n",w.value)
print("Minima is at d= ",d.value)