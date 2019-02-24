import numpy as np
import matplotlib.pyplot as plt
import scipy


N=int(1000)  # Number of input samples
M = 7  # No. of taps
mu = 0.075 # Step size

F = 3.0  
h = np.zeros(4)  # Channel Impulse response
for n in range(1,len(h)):
	h[n] = 0.5*(1+np.cos(2*np.pi*(n-2)/F))
print h
 
#b=np.zeros(N)
#b_hat=np.zeros(N)
ip=np.random.randint(2,size=N)
b=2*ip-1
#print b
bh = np.convolve(h,b) 
#print bh

e = np.zeros(N) # Error signal
y = np.zeros(N) #Output signal
J = np.zeros(N) #Mean Square Error
w = np.zeros(M) # Filter Coefficients 

noise = np.sqrt(0.001)*np.random.randn(len(bh))
#print noise
d = bh+noise
#print d

#LMS algorithm for Equalization	
for j in range(M,N):
	x = np.flipud(d[j-M:j])
	
	y[j] = np.dot(w,x)
	
	e[j] = b[j-7] - y[j]
	
	w += mu*e[j] * x
	
	J[j] = (e[j])**2.0
	
				
#print w		
plt.plot(J)
plt.grid()
plt.ylabel('MSE')
plt.xlabel('Iterations')
plt.title('Mean Square Error Curve,F=3.0, $\mu$ =0.075 ,delay=7 ')
plt.savefig('Learning_curve.eps')
plt.show()


    
