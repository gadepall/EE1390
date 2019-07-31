#1. IMPORTS
print("Data File ready, reading...")
import scipy.io as sio
import numpy as np
import time
import scipy.sparse.linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt




#2. DATA LOADING AND PROCESSING

#Loading data
mat_contents = sio.loadmat('data_all.mat')
data = mat_contents['data_all']
print("Loaded Data")
print("data.shape=","(obs,feat) = ",data.shape)
print("Checking and filtering NaN Values...")
data=np.nan_to_num(data)
print("Done.\n")
  
#Data has 25200 features and 10000 datapoints
X = data
num_datapoints, num_features = X.shape

#Adjusting precision according to RAM

#Originally, X[i,j] is of type np.float64
#If this gives memory error, uncomment : 
#X = np.float32(X)
#If memory error persists, uncomment : 
#X = np.float16(X)

print("X.shape=","(obs,feat) = ",X.shape)
#freeing up RAM, deleting used variables
del(data)
del(mat_contents)







#3. FINDING COVARIANCE

print("Finding Covariance Matrix...")
t3=time.time()
cov_mat2 = np.cov(X.T)
print("Done\ncov_mat2.shape=",cov_mat2.shape)
t4 = time.time()
print("Time taken  = ", t4-t3, "\n")





#4. FINDING EIG VAL & EIG VEC

print("Finding Eigen Values...")
t5=time.time()
eig_vals, eig_vecs = scipy.sparse.linalg.eigs(cov_mat2,k=6)
#taking only real parts as imaginary part of eigen values of Hermitian matrix are zero
eig_vals=np.real(eig_vals)
eig_vecs=np.real(eig_vecs)
t6=time.time()
print("Done\nTime taken= ", t6-t5, "\n")
#print("eig vals = \n",eig_vals)
#Covariance matrix not required anymore
del(cov_mat2)



#5. SORTING EIG VECS ACCORDING TO MAGNITUDE OF EIG VAL

eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
print("See top 6 eigvalues : \n")
for i in range(len(eig_vals)):
  print(eig_pairs[i][0], end=' ')
print()




#6. PROJECTION AND PLOTTING PART
print("\n\n\nPlotting\n\n")

def project_plot(X,eig_pairs,num_features,num_vec_to_keep):
    print("Original Dimensions = ", num_features)
    print("Keeping",num_vec_to_keep,"dimensions")
    #initializing projection matrix with 1 dim to keep
    proj_mat = eig_pairs[0][1].reshape(num_features,1)
    for eig_vec_idx in range(1, num_vec_to_keep):
      proj_mat = np.hstack((proj_mat, eig_pairs[eig_vec_idx][1].reshape(num_features,1)))
    # Project the data 
    print("Projecting Data...")
    pca_data = X.dot(proj_mat)
    print("Done")
    #save new array
    np.save('pca_data_'+str(num_vec_to_keep)+'D.npy',pca_data)
    print('Saved Final '+str(num_vec_to_keep)+'D Array')
    print("pca_data.shape=",pca_data.shape)
    #PLOTTING
    pca_data=np.load('pca_data_'+str(num_vec_to_keep)+'D.npy')
    print("pca_data.shape=",pca_data.shape)
    print("Plotting\n")
    #setting up plot
    fig = plt.figure()    
    if (num_vec_to_keep==3):
        ax = fig.add_subplot(111,projection='3d',aspect='auto')
        ax.scatter(pca_data[:int(len(pca_data)/2),0],pca_data[:int(len(pca_data)/2),1],pca_data[:int(len(pca_data)/2),2],color='r',alpha=0.3,label="Target Present")
        ax.scatter(pca_data[int(len(pca_data)/2):,0],pca_data[int(len(pca_data)/2):,1],pca_data[int(len(pca_data)/2):,2],color='b',alpha=0.3,label="Target Absent")
    elif (num_vec_to_keep==2):
        ax = fig.add_subplot(111,aspect='equal')
        ax.scatter(pca_data[:int(len(pca_data)/2),0],pca_data[:int(len(pca_data)/2),1],color='r',alpha=0.3,label="Target Present")
        ax.scatter(pca_data[int(len(pca_data)/2):,0],pca_data[int(len(pca_data)/2):,1],color='b',alpha=0.3,label="Target Absent")
    plt.legend()
    plt.grid()
    print("Done\n")

ch_3d = input("Project to 3D? [Y/N]").lower()
if (ch_3d=='y'):
    project_plot(X,eig_pairs,num_features,3)

ch_2d = input("Project to 2D? [Y/N]").lower()
if (ch_2d=='y'):
    project_plot(X,eig_pairs,num_features,2)

plt.show()