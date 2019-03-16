
import cvxpy as cvx
from numpy import matrix, round, eye

#Create Variable
w = cvx.Variable(3)


#Define the problem
f=((w[0]**2)+(w[1]**2))/2
obj = cvx.Minimize(f)
constraints = [2*w[0]+w[1]+w[2]>=1,0.8*w[0]-0.6*w[1]+w[2]<=-1]

#solution
result=cvx.Problem(obj, constraints)
result.solve()
print "Minimum of f(x) is ",result.value 
print w.value
