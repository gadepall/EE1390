#Code by GVV Sharma, Novermber 12, 2018
#Released under GNU GPL
from cvxpy import *
from numpy import matrix

A = matrix([ [1.0, 3.0], [1.0, 2.0 ]])
b = matrix([ 5.0, 12.0 ])
c = matrix([ 6.0, 5.0 ])

x = Variable((2,1),nonneg=True)
#Cost function
f = c*x
obj = Maximize(f)
#Constraints
constraints = [A.transpose()*x <= b.transpose()]

#solution
Problem(obj, constraints).solve()

print(f.value,x.value)

