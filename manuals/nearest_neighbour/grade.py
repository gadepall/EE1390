import numpy as np
f=open("input.txt").read().splitlines()
s_no=[]
id_card=[]
grade=[]
for i in f:
	s_no1,id_card1,grade1=i.split(',')
	s_no.append(s_no1)
	id_card.append(id_card1)
	grade.append(grade1)
	#print("s.no "+str(s_no)+" id "+str(id_card)+" grade "+str(grade))
	#print i

s_no=np.reshape(s_no,[-1,1])
id_card=np.reshape(id_card,[-1,1])
grade=np.reshape(grade,[-1,1])


N =grade.size 

              #Size of Data
x = grade
y =np.zeros((N,1))
x = x.astype('float64')
X = np.hstack((x,y))    #Attach label column with data


k = 8           #No.of Clusters(Grades)

k_points = np.linspace(0,1,8)*100       #Initialize clusters with some values
 
k_points = np.sort(k_points)
iterations = 500                    #No. of iterations

for iter in range(iterations):
    
    
    for i in range(N):              #Compute nearest cluster to a datapoint and 
                                    #attach its label to the datapoint.        
        dist = 999999
        
        for j in range(k):
            dist1 = (X[i][0]-k_points[j])**2
            if dist1<dist:
                X[i][1] = j + 1
                dist = dist1
    

    for i in range(k):       #Update cluster values by taking mean of corresponding labelled data
        
        s = 0
        c = 0
        for j in range(N):
            
            if X[j][1] == i+1:
                c += 1
                s += X[j][0]
        if c!=0:
            
            k_points[i] = s/c

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

for i in range(N):              #Print grades
    
    print('%d\t%s\t%.3f\t%s ' %(i+1,id_card[i][0],grade[i],grades[i]))

