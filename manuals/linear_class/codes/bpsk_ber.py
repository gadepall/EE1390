import numpy as np
from scipy import special
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

simlen = 1e6
N = np.random.normal(0, 1, int(simlen))
x_axis = np.linspace(0.0, 10.0, 100)	# x_axis = SNR in dB
A = np.sqrt(np.power(10, x_axis/10))    # note that A takes values from 1 to sqrt(10)
s = 0	
def bPsk_sim_prob(A):                   
	X = A*(2*s-1) + N       		    # (x|0) = -A + n
	x_cap = np.size(np.nonzero(X > 0))  
	return x_cap / simlen               # simlen itself is size of Y here
	
	
bPsk_sim = []
bPsk_thry = []

# calculating error for SNR ranging from 1 to 10 dB

for i in  range (0, 100):
	bPsk_sim.append(bPsk_sim_prob(A[i]))
	bPsk_thry.append(0.5 *special.erfc(A[i] / np.sqrt(2)))
	
#plot y in log scale

plt.semilogy(x_axis, bPsk_sim, 'o')	
plt.semilogy(x_axis.T, bPsk_thry)
plt.xlabel('SNR(dB)')
plt.ylabel('$P_e$')
plt.legend(["bPsk simulated","bPsk theoretical"])
plt.grid()
#If using termux
plt.savefig('../figs/bpsk_ber.pdf')
plt.savefig('../figs/bpsk_ber.eps')
subprocess.run(shlex.split("termux-open ../figs/bpsk_ber.pdf"))
#else
#plt.show()

