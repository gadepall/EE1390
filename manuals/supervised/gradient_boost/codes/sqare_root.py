#Newton Ralphson
import numpy as np

n = 10
c = 2
x = 1

for k in range(n):
	x = 0.5*(x + c/x)
	x = x

print(x)
	



