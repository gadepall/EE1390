#SVM Using Non-Linear Kernel

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import time
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mlxtend.plotting import plot_decision_regions

#-----Time Requirements----#
start_time = time.time()

#-----Loading Data-----#
mat_contents = sio.loadmat('data_all.mat')
X_data = mat_contents['data_all']

#------Standardizing the features-----#
scaler = StandardScaler(copy =True, with_mean = True, with_std = True)
X_data = scaler.fit_transform(X_data)

#-------Applying Principal Component Analysis-----#
pca = PCA(n_components =2)
X = pca.fit_transform(X_data)

#------Creating a labeled array------#
y= np.zeros(len(X))
y[:int(len(X)/2)] = 1
y[int(len(X)/2):] = 2

#-----Fit SVM model-----#
#X_svm = svm.NuSVC(gamma = 'auto')
X_svm = svm.SVC(kernel= 'rbf', gamma =0.01)
X_svm.fit(X,y)

xx, yy = np.meshgrid(np.linspace(-3, 3, 500),np.linspace(-3, 3, 500))

# plot the decision function for each datapoint on the grid
Z = X_svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

##-----Plotting SVM Decision Region Boundary-----#
#plot_decision_regions(X, y.astype(np.integer), clf= X_svm, legend=2)
#plt.title('SVM Hyperplane for Non-Linear Kernel')
#plt.xlabel('Principal Component 1')
#plt.ylabel('Principal Component 2')
#plt.savefig('../figs/HyperPlane_NLin.png')
#plt.savefig('../figs/HyperPlane_NLin.eps')

plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired,edgecolors='k')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('SVM with Non-Linear Kernel in 2D') 
plt.savefig('../figs/NLinSVM_2D.png')
plt.savefig('../figs/NLinSVM_2D.eps')

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))