import numpy as np
import pandas as pd

data = pd.read_excel('marks.xlsx')      #reading input
df1 = data.loc[:,"Total" or "Marks"]    #storing marks column
x = np.array(df1)

N = x.size                              #Size of Data
x = x.reshape(N,1)                      #Converting to column
y = np.zeros((N,1))                     #column of Assigned clusters 
X = np.hstack((x,y))                    #stacking data and cluster
k = 7                                   #No.of Clusters(Grades)

k_points = np.linspace(0,1,k)*np.max(x) 
#Initializing Clusters means spaced equally in (0,x_max)
k_points = np.sort(k_points)

iterations = 150                        #Max iterations

for iter in range(iterations):
    label_changes = False               #tracks label changes
    mean_changes = False                #tracks cluster mean changes
    
    for i in range(N):              
    #Compute nearest cluster, attach its label to the datapoint.  
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
    
    for i in range(k):       
    #Update cluster mean by taking mean of corresponding marks  
        s = 0 #sum of elements of cluster i
        c = 0 #count of elements of cluster i
        for j in range(N):            
            if X[j][1] == i+1:
                c += 1
                s += X[j][0]
        if c!=0:
            if (s/c!=k_points[i]):
                k_points[i] = s/c
                mean_changes=True
    if (label_changes==False and mean_changes==False):
        print("Converged on Iteration", iter)
        break           

grades = []                #Attach grades to the data points 
for i in range(N):              
    if X[i][1] == 1:
        grades.append('D')
    if X[i][1] == 2:
        grades.append('C-')
    if X[i][1] == 3:
        grades.append('C')
    if X[i][1] == 4:
        grades.append('B-')
    if X[i][1] == 5:
        grades.append('B')
    if X[i][1] == 6:
        grades.append('A-')
    if X[i][1] == 7:
        grades.append('A')
data['Grades'] = grades
data.to_excel('grades.xlsx',index = False)  #writing to file