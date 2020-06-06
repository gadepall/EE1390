import os
import numpy as np
import soundfile as sf
from sklearn.model_selection import train_test_split

data_dir = '../Data/Pradeep_16/'
os.chdir(data_dir)
data_x = []
data_y = []
for a,i in enumerate(['forward','back','left','right','stop']):
    lis = os.listdir(data_dir+i)
    for j in lis:
        l,sr = sf.read(data_dir+i+'/'+j)
        if(len(l)==16000):
            data_x.append(l)
            data_y.append(a)
        else:
            print(i)
    print(i," Done")

data_x = np.array(data_x)
data_y = np.array(data_y)

tr_x,te_x, tr_y,te_y = train_test_split(data_x,data_y,stratify=data_y,random_state=123,test_size=0.2)

x_train = []
y_train = []
for i,j in enumerate(tr_x):
    x= len(j)
    p = 25000-x
    for y in range(1 ,p, 500):
        nx = np.zeros(25000)
        nx[y:y+x] =j
        x_train.append(nx)
        y_train.append(tr_y[i])
x_train = np.array(x_train)
y_train = np.array(y_train)

np.save('x_train.npy',x_train)
np.save('y_train.npy',y_train)

x_test = []
y_test = []
for i,j in enumerate(te_x):
    x= len(j)
    p = 25000-x
    for y in range(1 ,p, 500):
        nx = np.zeros(25000)
        nx[y:y+x] =j
        x_test.append(nx)
        y_test.append(te_y[i])
x_test = np.array(x_test)
y_test = np.array(y_test)

np.save('x_test.npy',x_test)
np.save('y_test.npy',y_test)