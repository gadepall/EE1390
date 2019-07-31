import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import mixture 

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')

def plot_line(eqn,labelstr):
	if eqn[1]!=0:
		#plotting line (eqn[0])x + (eqn[1])y = eqn[2]
		slope = -1*eqn[0]/eqn[1]
		intercept = eqn[2]/eqn[1]
		x_vals = np.array([-750,-250])
		y_vals = intercept + slope * x_vals
		plt.plot(x_vals, y_vals, label=labelstr)
	else:
		#plotting vertical line (eqn[0])x = eqn[2]
		plt.axvline(eqn[2]/eqn[0],label=labelstr)

pca_data=np.load('pca_data_2D.npy')
print("pca_data.shape=",pca_data.shape)
print("Plotting\n")
ax.scatter(pca_data[:int(len(pca_data)/2),0],pca_data[:int(len(pca_data)/2),1],color='r',alpha=0.3,label="Target Present")
ax.scatter(pca_data[int(len(pca_data)/2):,0],pca_data[int(len(pca_data)/2):,1],color='b',alpha=0.3,label="Target Absent")

ax.set_ylim([25,250])
ax.set_xlim([-800,-350])
plt.legend()
plt.grid()

#Creating Labels Array
y = np.zeros(len(pca_data))
y[:int(len(pca_data)/2)]=1
y[int(len(pca_data)/2):]=-1
print("y.shape=",y.shape)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')

print("Fitting SVC")
clf = svm.SVC(kernel='linear', C=1000)
clf.fit(pca_data, y)
w = 1000*clf.coef_
b = 1000*clf.intercept_
#Equation of Learnt Hyperplane : w[0].T@x+b=0
#Plotting SVC Hyperplane
plot_line(np.array([w[0,0],w[0,1],-1.0*b]),"SVC Hyperplane")
print("Done\n")

print("Fitting Gaussian Mixture Model")
gmm1 = mixture.GaussianMixture(n_components=4,covariance_type='spherical',max_iter=100000)
gmm1.fit(pca_data[:int(len(pca_data)/2)])
means1 = gmm1.means_
gmm2 = mixture.GaussianMixture(n_components=4,covariance_type='spherical',max_iter=100000)
gmm2.fit(pca_data[int(len(pca_data)/2):])
means2 = gmm2.means_
print("Done\n")

print("Plotting Clusters")
labels1 = gmm1.predict(pca_data[:int(len(pca_data)/2)])
plt.scatter(pca_data[:int(len(pca_data)/2), 0], pca_data[:int(len(pca_data)/2), 1], c=labels1);
plt.scatter(means1[:,0],means1[:,1], color='red', label="Type 1 Cluster Mean")
labels2 = gmm2.predict(pca_data[int(len(pca_data)/2):])
plt.scatter(pca_data[int(len(pca_data)/2):, 0], pca_data[int(len(pca_data)/2):, 1], c=labels2);
plt.scatter(means2[:,0],means2[:,1], color='red', label="Type 2 Cluster Mean")
print("Done\n")

ax.set_ylim([25,250])
ax.set_xlim([-800,-350])
plt.legend()
plt.grid()

plt.show()