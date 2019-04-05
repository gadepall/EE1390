import numpy as np

A = np.matrix('2 0 -1; 0 2 -1; 1 1 0')
b = np.matrix('16 ; 12 ; 9')
print (np.linalg.inv(A)*b)
