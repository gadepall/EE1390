#Mean-normalization
#Imports
import numpy as np
import time
import scipy.io as sio
#from sklearn.decomposition import TruncatedSVD
#from sklearn.utils.extmath import randomized_svd
import scipy.sparse.linalg
from matplotlib import pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
#from matplotlib.patches import FancyArrowPatch # FancyArrowPatch draws new arrow using ArrowStyle 
#from numpy import linalg

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
X_data = mat_contents['data_all']

#X_std = np.zeros((10000,25200))
X = np.matrix(X_data)
mu = X.mean(0)
std = X.std(0)
    
#-----Standardizing the features-----#
X_std = (X_data - mu)/std

#Covariance Matrix
cov = np.cov(X_std)

eig_vals, eig_vecs = scipy.sparse.linalg.eigs(cov,k=6)
eig_vals = np.real(eig_vals)
eig_vecs = np.real(eig_vecs)
#del(cov_mat2)

#Arranging eigen values in decreasing order
idx = eig_vals.argsort()[::-1]   
eig_vals = eig_vals[idx]
eig_vecs = eig_vecs[:,idx]

#eig_val_cv, eig_vec_cv = np.linalg.eig(np.cov(X_data))
#svd = TruncatedSVD(n_components =3)
#X_truncated = svd.fit_transform(cov)

##-----2D Plot-----#
fig = plt.figure()
ax = fig.add_subplot(111)
#plt.scatter(X_truncated[:, 0], X_truncated[:, 1],marker='o')
plt.scatter(eig_vecs[:, 0],eig_vecs[:, 1],marker='o')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2') 
plt.title('PCA 2D Plot')
plt.savefig('../figs/PCA_2D_woFun.png')
plt.savefig('../figs/PCA_2D_woFun.eps')

#------3D Plot------#
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax.scatter3D(X_truncated[:, 0], X_truncated[:, 1],X_truncated[:,2], marker='o')
ax.scatter3D(eig_vecs[:, 0], eig_vecs[:, 1],eig_vecs[:,2], marker='o')
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('PCA 3D Plot')
plt.title('Eigenvectors')
plt.savefig('../figs/PCA_3D_woFun.png')
plt.savefig('../figs/PCA_3D_woFun.eps')
plt.show()

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))