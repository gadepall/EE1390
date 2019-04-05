from cvxpy import *
x = Variable((2,2),PSD = True)
f = x[0][0] + x[0][1]
obj = Minimize(f)
constraints = [x[0][0] + x[1][1] == 1]

Problem(obj, constraints).solve()
print ("Minimum of f(x) is ",round(f.value,2), " at  \
(",round(x[0][0].value,2),",",round(x[0][1].value,2),")") 

