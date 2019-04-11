#Solving a Quadtratic Program in cvxpy

import cvxpy as cp
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
one = np.ones(n) #matrix of n ones

""" 
	LD = -0.5*alpha.T*m1*m2*alpha + alpha.T*one
	A=m1*m2
"""

m1=(x@y).T
#print("m1=\n",m1)

m2=m1.T
#print("m2=\n",m2)

A = m1@m2
#print("A=\n",A)

alpha=cp.Variable(2)

#objective
obj=cp.Maximize( -0.5*cp.quad_form(alpha,A) +one.T@alpha)

#constraints
constraints=[alpha>=np.zeros(2),one.T@y@alpha==0]
prob=cp.Problem(obj, constraints)
prob.solve()

print("\nMaximum value is = \n", obj.value)
print("\nMaxima is at alpha = \n",alpha.value)

alpha = np.reshape(alpha.value,(n,1))
w = m2@alpha
LD = -0.5*(alpha.T)@m1@m2@alpha
print("Max value of LD is = \n", LD)
print("Max value obtained at alpha = \n", alpha	)
print("Learnt w = \n",w)