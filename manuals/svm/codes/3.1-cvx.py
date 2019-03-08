#Code by GVV Sharma, Novermber 15, 2018
#Released under GNU GPL
#Semi definite programming example
import cvxpy as cvx
from numpy import matrix, round, eye

#Create Variable
X = cvx.Variable((2,2),PSD = True)

#Create constant vectors/matrices
B = eye(2)
v = matrix([[1],[0]])
u = matrix([[1],[1]])
w = matrix([[1, 0, 0, 1]])

#Define the problem
f =  u.transpose()*X.T*v
obj = cvx.Minimize(f)
T = cvx.bmat([[X,B],[B,X]])
constraints = [w*T*w.transpose() == 1]

#solution
cvx.Problem(obj, constraints).solve()
print ("Minimum of f(x) is ",round(f.value,2),"at X=", X.value )

