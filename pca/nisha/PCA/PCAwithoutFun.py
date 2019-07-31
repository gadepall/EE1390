#Mean-normalization
#Imports
import numpy as np
import time
import scipy.io as sio
from sklearn.decomposition import TruncatedSVD
from sklearn.utils.extmath import randomized_svd

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch # FancyArrowPatch draws new arrow using ArrowStyle 
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
#for i in range(0,25200,1):
#    X_std[:,i] = (X_data[:,i] - mu[:,i])/std[:,i]
X_std = (X_data - mu)/std

#Covariance Matrix
cov = np.cov(X_std)

#U, Sigma, VT = randomized_svd(cov, n_components=10, n_iter=5,random_state=None)
#U, Sigma, VT = randomized_svd(cov, n_components=2, n_iter=5,random_state=None)

#eig_val_cv, eig_vec_cv = np.linalg.eig(np.cov(X_data))
#svd = TruncatedSVD(n_components =5)
#svd.fit(cov)

#Scatter
scatter_matrix = np.zeros((10000,10000))
scatter_matrix = (X_std - mu).dot((X_std -mu).T)
#for i in range(X_data.shape[1]):
#    scatter_matrix += (X_data[:,i].reshape(10000,1) - mean_vector).dot((X_data[:,i].reshape(10000,1) - mean_vector).T)
#print('Scatter Matrix:\n', scatter_matrix)

eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)

#Eigen Value & Eigen Vector
#U,S,vh = np.linalg.svd(cov)

#Visualizing the Eigen Vectors
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M) 
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(X_data[:,0], X_data[:,1], X_data[:,2], 'o', markersize=8, color='green', alpha=0.2)
ax.plot([mu[:,0]], [mu[:,1]], [mu[:,2]], 'o', markersize=10, color='red', alpha=0.5)
for v in eig_vec_sc.T:
    a = Arrow3D([mu[:,0], v[0]], [mu[:,1], v[1]], [mu[:,2], v[2]], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
    ax.add_artist(a)
ax.set_xlabel('x_values')
ax.set_ylabel('y_values')
ax.set_zlabel('z_values')

plt.title('Eigenvectors')
plt.show()

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))