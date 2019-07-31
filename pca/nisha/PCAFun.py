#EE18MTECH11002
#Principal Component Analysis using Inbuilt Function

#-----Required Packages-----#
import time
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
X_data = mat_contents['data_all']

#-----Standardizing the features-----#
scaler = StandardScaler(copy=True, with_mean= True, with_std=True)
X_data = scaler.fit_transform(X_data)

#-----PCA-----#
#For 95% accuracy how many prin. comp need to be considered
#pca = PCA(.95)
#X_pca = pca.fit(X_data)
#X_pca1 = PCA().fit_transform(X_data1)
#Plotting the Cumulative Summation of the Explained Variance
#plt.figure()
#plt.plot(np.cumsum(X_comp.explained_variance_ratio_))
#plt.xlabel('Number of Components')
#plt.ylabel('Variance (%)') #for each component
#plt.title('Pulsar Dataset Explained Variance')
#plt.show()

#For 2 Principal Components
pca = PCA(n_components=2)
X_comp = PCA().fit_transform(X_data)

##-----2D Plot-----#
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(X_comp[:, 0], X_comp[:, 1],marker='o')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2') 
plt.title('PCA 2D Plot')

#For 3 Principal Components
pca = PCA(n_components=3)
X_comp = pca.fit_transform(X_data) 
#      
##-----3D Plot-----# c is for color
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter3D(X_comp[:, 0], X_comp[:, 1],X_comp[:,2], marker='o')
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('PCA 3D Plot')

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))