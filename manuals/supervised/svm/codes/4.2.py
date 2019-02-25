from cvxopt import matrix
from cvxopt import solvers

A = matrix([ [1.0, 3.0, -1.0, 0], [1.0, 2.0, 0, -1.0] ])
b = matrix([ 5.0, 12.0, 0.0, 0.0 ])
c = matrix([ -6.0, -5.0 ])


sol = solvers.sdp(c, A, b)
print(sol['x'])                                     
