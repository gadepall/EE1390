import numpy as np
import matplotlib.pyplot as plt

simlen = 1e4
Eb=5

s0 = np.array([1,0])
s1 = np.array([0,1])

y0 = [((Eb*s0[j])+np.random.normal(0, 1, int(simlen))) for j in range(2)] # y0 = 2 x simlen array = ( sqrt(A)+n1 , n2)
y1 = [((Eb*s1[j])+np.random.normal(0, 1, int(simlen))) for j in range(2)] # y0 = 2 x simlen array = ( n1 , sqrt(A)+n2)

plt.scatter(y0[0], y0[1],c='b')
plt.scatter(y1[0], y1[1],c='g')

plt.legend(["s0", "s1"])

plt.text(-0.5,-1,'$(0,0)$')
plt.text(5,0,'$(sqrt(A),0)$')
plt.text(0,5,'$(0,sqrt(A))$')
plt.plot(0, 0, 'o')
plt.plot(0, 5, 'o')
plt.plot(5,0, 'o')
plt.grid()
plt.show()
