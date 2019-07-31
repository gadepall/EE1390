#EE18MTECH11002
#Principal Component Analysis using Inbuilt Function

#-----Required Packages-----#
import time
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import scipy.io as sio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import csv
#import pandas as pd

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
X_data = mat_contents['data_all']

#X_data = pd.read_csv('data.csv')

#scaler = MinMaxScaler(feature_range=[0, 1])
#X_data1 = scaler.fit_transform(X_data)

#-----Standardizing the features-----#
scaler = StandardScaler(copy=True, with_mean= True, with_std=True)
X_data = scaler.fit_transform(X_data)

 #-----User giving Dimension-----#
#comp = int(input("Enter no of principle components: "))

#-----PCA-----#

pca = PCA(n_components=2)
X_comp = PCA().fit_transform(X_data)
#pca = PCA(.95)
#pca = PCA()
#X_pca = pca.fit(X_data)
#
#Plotting the Cumulative Summation of the Explained Variance
#plt.figure()
#plt.plot(np.cumsum(X_pca.explained_variance_ratio_))
#plt.xlabel('Number of Components')
#plt.ylabel('Variance (%)') #for each component
#plt.title('Pulsar Dataset Explained Variance')
#plt.show()


#-----2D Plot-----#
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(X_comp[:, 0], X_comp[:, 1],marker='o')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2') 
plt.title('PCA 2D Plot')

pca = PCA(n_components=3)
X_comp = pca.fit_transform(X_data) 
      
#-----3D Plot-----# c is for color
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter3D(X_comp[:, 0], X_comp[:, 1],X_comp[:,2], marker='o')
ax.set_xlabel('Prin. Comp 1')
ax.set_ylabel('Prin. Comp 2')
ax.set_zlabel('Prin. Comp 3')
ax.set_title('PCA 3D Plot')

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))