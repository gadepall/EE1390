import numpy as np 
from sklearn.cluster import KMeans  

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




def Predict(x,centers):
	grads = []
	centers = centers.reshape(-1)
	for elem in x:
		if(elem>=centers[-1]):
			grads.append("A")
		elif(elem>=centers[-2] and elem<centers[-1]):
			grads.append("A-")
		elif(elem>=centers[-3] and elem<centers[-2]):
			grads.append("B")
		elif(elem<centers[-3]):
			grads.append("B-")
	return grads

inp_data = []

X = grade
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)


centers = kmeans.cluster_centers_
print(kmeans.cluster_centers_)
print(kmeans.labels_)
centers = np.sort(centers.reshape(-1))
centers = centers.reshape(-1,1)
predictions = Predict(inp_data,centers)
print(predictions)
a=Predict(X,centers)
print(a)
