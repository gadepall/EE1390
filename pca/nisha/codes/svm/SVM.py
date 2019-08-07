#EE18MTECH11002
#After applying PCA, SVM with Linear Kernel

#-----Required Packages-----#
from sklearn import svm    			# To fit the svm classifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt 
import time
from mpl_toolkits.mplot3d import proj3d

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
data = mat_contents['data_all']

#-----Standardizing the features-----#
data = StandardScaler().fit_transform(data)

#-----PCA-----#
#pca1 = PCA(n_components=2)
pca_2D = PCA(n_components=3).fit_transform(data)

X = pca_2D

#-----Creating Labels Array-----#
y = np.zeros(len(X))
y[:int(len(X)/2)]=1
y[int(len(X)/2):]=2

#-----SVC with linear kernel C-Regularization parameter-----#
svc_lin = svm.SVC(kernel='linear', C=1).fit(X, y)
	                    
#-----Plotting SVM Decision Region Boundary-----#
#plot_decision_regions(X[:,0:2], y.astype(np.integer),svc_lin, legend=2)
#plt.title('SVM Hyperplane for Linear Kernel')
#plt.xlabel('Principal Component 1')
#plt.ylabel('Principal Component 2')
plt.savefig('../figs/HyperPlane_Linear.png')
plt.savefig('../figs/HyperPlane_Linear.eps')

#-----Plotting SVM with Linear Kernel-----#
plot = plt.figure()
ax = plot.add_subplot(111)
plt.scatter(X[:int(len(X)/2),0],X[:int(len(X)/2),1],c='r',alpha=0.5,label="Target Present")
plt.scatter(X[int(len(X)/2):,0],X[int(len(X)/2):,1],c='b',alpha=0.5,label="Target Absent")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('SVM with Linear Kernel in 2D') 
plt.legend()
#plt.show()
plt.savefig('../figs/LinSVM_2D.png')
plt.savefig('../figs/LinSVM_2D.eps')
plt.close()

Y = np.zeros([10000,3])
Y[:int(len(Y)/2),0]=1
Y[int(len(Y)/2):,0]=2

z = lambda X,Y: (-svc_lin.intercept_[0]-svc_lin.coef_[0][0]*X-svc_lin.coef_[0][1]*Y) / svc_lin.coef_[0][2]

#-----Plotting SVM with Linear Kernel and its Decision Region Boundary-----#
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, z(X,Y))
ax.scatter3D(X[:int(len(X)/2),0],X[:int(len(X)/2),1],X[:int(len(X)/2),2],c='r',alpha=0.3,marker='o',label="Target Present")
ax.scatter3D(X[int(len(X)/2):,0],X[int(len(X)/2):,1],X[int(len(X)/2):,2],c='b',alpha=0.3,marker='o',label="Target Absent")
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('SVM with Linear Kernel in 3D')
ax.legend()
plt.savefig('../figs/LinSVM_3D.png')
plt.savefig('../figs/LinSVM_3D.eps')
#plt.show()
plt.close()

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))