from cvxopt import matrix
from cvxopt import solvers

c = matrix([1.,1.,0.])
G = [ matrix([[-1., 0., 0., 0.],[ 0., -1., -1., 0.],[0.,  0.,  0., -1.]]) ]

Aval = matrix([1.,0.,1.],(1,3))
bval = matrix([1.])

h = [ matrix([[0., 0.], [0., 0.]]) ]
sol = solvers.sdp(c, Gs=G, hs=h,A=Aval, b=bval)
print(sol['x'])                                     
