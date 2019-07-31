#PCA with SVM in 3D

#-----Required Packages-----#
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt 
import time
from mlxtend.plotting import plot_decision_regions
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
data = mat_contents['data_all']

#-----Standardizing the features-----#
data = StandardScaler().fit_transform(data)

#-----PCA-----#
pca = PCA(n_components=3).fit_transform(data)

#-----Plot for PCA-----#
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter3D(pca[:, 0], pca[:, 1],pca[:,2], marker='o')
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('PCA 3D Plot')  
plt.show()

X = pca

#-----Creating Labels Array-----#
y = np.zeros(len(X))
y[:int(len(X)/2)]=1
y[int(len(X)/2):]=2

#-----SVC with linear kernel C-Regularization parameter-----#
svc = svm.SVC(kernel='linear', C=1).fit(X, y)

Y = np.zeros([10000,3])
Y[:int(len(Y)/2),0]=1
Y[int(len(Y)/2):,0]=2

z = lambda X,Y: (-svc.intercept_[0]-svc.coef_[0][0]*X-svc.coef_[0][1]*Y) / svc.coef_[0][2]
	                    
#-----Plotting SVM with Linear Kernel and its Decision Region Boundary-----#
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, z(X,Y))
ax.scatter3D(X[:int(len(X)/2),0],X[:int(len(X)/2),1],X[:int(len(X)/2),2],c='r',alpha=0.3,marker='o',label="Target Present")
ax.scatter3D(X[int(len(X)/2):,0],X[int(len(X)/2):,1],X[int(len(X)/2):,2],c='b',alpha=0.3,marker='o',label="Target Absent")
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('PCA Decision Region Boundary')
ax.legend()
plt.show()

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))