import numpy as np
import pandas as pd

data = pd.read_excel('tinput.xlsx')
# print("data.shape=",data.shape)

df1 = data.loc[:,"Total" or "Marks"]

# print("df1.shape=",df1.shape)

x = np.array(df1)

N = x.size                #Size of Data
# print("N=",N)

x = x.reshape(N,1)
y = np.zeros((N,1))
# print("x.shape=",x.shape)
# print("y.shape=",y.shape)
 
X = np.hstack((x,y))    #Attach label column with data
# print("X.shape=",X.shape)

k = 8           #No.of Clusters(Grades)

k_points = np.linspace(0,1,8)*np.max(x)     #Initialize clusters with some values
                                            #Initializing Clusters with Values spaces equally at 102.0/7.0
# print("k_points.shape=",k_points.shape) 
# print("k_points=",k_points) 

k_points = np.sort(k_points)
iterations = 100                   #No. of iterations


for iter in range(iterations):
    label_changes = False
    mean_changes = False 
    
    for i in range(N):              #Compute nearest cluster to a datapoint and 
                                    #attach its label to the datapoint.        
        old_label=X[i][1]
        new_label=X[i][1]
        dist = 999999.0
        
        for j in range(k):
            dist1 = (X[i][0]-k_points[j])**2
            if dist1<dist:
                new_label = j + 1
                dist = dist1

        X[i][1]=new_label
        if (new_label!=old_label):
            label_changes=True
    

    for i in range(k):       #Update cluster values by taking mean of corresponding labelled data
        
        s = 0
        c = 0
        for j in range(N):
            
            if X[j][1] == i+1:
                c += 1
                s += X[j][0]
        if c!=0:
            if (s/c!=k_points[i]):
                k_points[i] = s/c
                mean_changes=True

    #print("Iter=",iter,"label_changes=",label_changes,"mean_changes=",mean_changes)
    if (label_changes==False and mean_changes==False):
        print("Converged on Iteration", iter)
        break           

grades = []

for i in range(N):              #Attach grades to the data points
    
    if X[i][1] == 1:
        grades.append('F')
    if X[i][1] == 2:
        grades.append('D')
    if X[i][1] == 3:
        grades.append('C-')
    if X[i][1] == 4:
        grades.append('C')
    if X[i][1] == 5:
        grades.append('B-')
    if X[i][1] == 6:
        grades.append('B')
    if X[i][1] == 7:
        grades.append('A-')
    if X[i][1] == 8:
        grades.append('A')

data['Grades'] = grades

data.to_excel('grades_new.xlsx',index = False)

#print(grades)