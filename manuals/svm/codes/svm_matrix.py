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

a11 = np.eye(n)
#print("a11.shape",a11.shape)

a12=-1.0*x@y
#print("a12.shape",a12.shape)

a13 = np.zeros((n,1))
#print("a13.shape",a13.shape)

a21 = -1*a12.T
#print("a21.shape",a21.shape)

a22 = np.zeros((n,n))
#print("a22.shape",a22.shape)

a23 = sum(y).reshape((n,1))
#print("a23.shape",a23.shape)
#Compare Equation (4.13) with Ax=b and solve

a31=np.zeros((1,n))
#print("a31.shape",a31.shape)

a32=a23.T
#print("a32.shape",a32.shape)


a33=np.zeros((1,1))
#print("a33.shape",a33.shape)

A = np.block([
	[ a11, a12, a13	],
	[ a21, a22, a23	],
	[ a31, a32,	a33 ]
	])

print("\nA=\n",A)
b = np.array([[0],[0],[1],[1],[0]])
x = np.matmul( np.linalg.inv(A), b )


w, alpha, d = x[:2,:], x[2:4,:], x[4,:]
print("\nw=\n",w,"\nalpha=\n",alpha,"\nd=\n",d)