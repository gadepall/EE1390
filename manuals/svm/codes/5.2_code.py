#Solving a Quadtratic Program in cvxpy

import cvxpy as cp
import numpy as np

x1 = np.matrix('2;1')
x2 = np.matrix('0.8;-0.6')
y1 = 1
y2 = -1
one = np.matrix('1;1')

A = np.matmul( np.block([[y1*x1.T],[y2*x2.T]]), np.block([[y1*x1 , y2*x2]]) )
print("A=\n",A)

alpha=cp.Variable(2)
print(cp.quad_form(alpha,A).shape)
w = np.block([y1*x1, y2*x2]) @alpha
constraints=[alpha>=np.zeros(2), y1*alpha[0]+y2*alpha[1]==0]#cp.quad_form(alpha,A) - alpha == np.zeros((1,2)) ]
prob = cp.Problem(cp.Maximize( -0.5*cp.quad_form(alpha,A) +one.T@alpha), constraints)
prob.solve()

print("\nMaximum value is = \n", prob.value)
print("\nMaxima is at alpha = \n",alpha.value)

alpha = np.matrix(alpha.value).T
# #print(alpha.shape)
w = np.matmul(np.block([y1*x1, y2*x2]), alpha)
LD = np.matmul(one.T,alpha) -0.5*(np.matmul(alpha.T,np.matmul(A,alpha)))
print("Max value of LD is = \n", LD)
print("Max value obtained at alpha = \n", alpha	)
print("Learnt w = \n",w)