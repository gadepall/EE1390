#PCA with SVM(Linear Kernel) 2D 

#-----Required Packages-----#
from sklearn import svm    			# To fit the svm classifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt 
import time
from mlxtend.plotting import plot_decision_regions

#-----Time Requirements-----#
start_time =time.time()

#-----Loading Data from .mat file-----#
mat_contents = sio.loadmat('data_all.mat')
data = mat_contents['data_all']

#-----Standardizing the features-----#
data = StandardScaler().fit_transform(data)

#-----PCA-----#
#pca1 = PCA(n_components=2)
pca = PCA(n_components=2).fit_transform(data)

#-----Plot for PCA-----#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(pca[:, 0], pca[:, 1],marker='o')
#ax.set_xlabel('Principal Component 1')
#ax.set_ylabel('Principal Component 2') 
#ax.set_title('PCA 2D Plot')  
#plt.show()

X = pca

#-----Creating Labels Array-----#
y = np.zeros(len(X))
y[:int(len(X)/2)]=1
y[int(len(X)/2):]=2

#-----SVC with linear kernel C-Regularization parameter-----#
#svc_lin = svm.SVC(kernel='linear', C=1).fit(X, y)

svc_rbf = svm.SVC(kernel='linear', C=10).fit(X, y)
	                    
#-----Plotting SVM Decision Region Boundary-----#
plot_decision_regions(X, y.astype(np.integer),svc_rbf, legend=2)
plt.title('SVM Hyperplane')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

#-----Plotting SVM with Linear Kernel-----#
plot = plt.figure()
ax = plot.add_subplot(111)
plt.scatter(X[:int(len(X)/2),0],X[:int(len(X)/2),1],c='r',alpha=0.5,label="Target Present")
plt.scatter(X[int(len(X)/2):,0],X[int(len(X)/2):,1],c='b',alpha=0.5,label="Target Absent")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('SVM with Linear Kernel') 
plt.legend()
plt.show()

#-----Print Time Required-----#
print("--- %s seconds ---" % (time.time() - start_time))