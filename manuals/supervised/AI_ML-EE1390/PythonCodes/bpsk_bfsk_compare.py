import numpy as np
from scipy import special
import matplotlib.pyplot as plt

simlen = 1e4
N = np.random.normal(0, 1, int(simlen))
n1 = np.random.normal(0, 1, int(simlen))
n2 = np.random.normal(0, 1, int(simlen))
x_axis = np.linspace(0.0, 10.0, 100)	# x_axis = SNR in dB
A = np.sqrt(np.power(10, x_axis/10))    # note that A takes values from 1 to sqrt(10)
	
def bPsk_sim_prob(A):                   
	Y = A + N       		    # (Y|X=1) = A + N
	x_cap = np.size(np.nonzero(Y < 0))  # P(x_cap = -1 | X=1), which in general equal to BER=0.5*(P(x_cap=-1 | X=1)+P(x_cap=1 | X=-1))
	return x_cap / simlen               # simlen itself is size of Y here
	
def bFsk_sim_prob(A):
	s0 = [1, 0]
	y1 = A * s0[0] + n1		    # (Y|s=s0) = [A+n1  0+n2] 
	y2 = s0[1] + n2						
	pr = np.size(np.nonzero(y1 < y2))/simlen # P(x_tilda = s1 | s=s0), which in general equal to BER=0.5*(P(x_tilda=s1 | s=s0)+P(x_tilda=s0 | s=s1))
	return pr
	
bPsk_sim = []
bPsk_thry = []
bFsk_sim = []
bFsk_thry = []

# calculating error for SNR ranging from 1 to 10 dB

for i in  range (0, 100):
	bPsk_sim.append(bPsk_sim_prob(A[i]))
	bPsk_thry.append(0.5 *special.erfc(A[i] / np.sqrt(2)))
	bFsk_sim.append(bFsk_sim_prob(A[i]))
	bFsk_thry.append(0.5*special.erfc(A[i]/2))
	
#plot y in log scale

plt.semilogy(x_axis, bPsk_sim, 'o')	
plt.semilogy(x_axis.T, bPsk_thry)
plt.semilogy(x_axis, bFsk_sim, 'o')
plt.semilogy(x_axis, bFsk_thry)
plt.xlabel('$SNR_dB')
plt.xlabel('P(error)')
plt.legend(["bPsk simulated","bPsk theoretical","bFsk simulated","bFsk theoretical"])
plt.grid()
plt.show()
