import numpy as np
from matplotlib import pyplot as plt
import random
import soundfile as sf
from python_speech_features import mfcc

def sigmoid(x):                                #defining sigmoid function 
    x = np.array(x,dtype=np.float128)
    x = x.reshape(nOut,1)
    x = x
    for  i in range (0,5):
	if x[i] < -700:                            # to prevent overflow error, we have manually defined it to be 0, when input is very low
	    x[i]=0
	else:
	    x[i] = 1/(1+np.exp(-x[i]))	
    x=x.reshape(-1,nOut)
    return x
nOut = 5

 
def sigmoidprime(x):                          # derivative of sigmoid function
    return sigmoid(x)*(1-sigmoid(x))
#    return 1.*(x>0)




y0 = np.empty([6250,4043])                    # reading all the back.wav files, coverting to mfcc format, adding labels and storing in an array
for j in range(0,6250):
    b = "back"+str(j)+".wav"
    #print b
    data, samplerate = sf.read(b)
    data1 = mfcc(data,samplerate)
    data = data1.reshape(4043,)
    y0[j]=data
y = np.empty([6250,5])
for i in range (0,6250):                      # manually assigning labels
    y[i][0]=1.0
    y[i][1]=0.0
    y[i][2]=0.0
    y[i][3]=0.0
    y[i][4]=0.0	
y0l = np.append(y0,y,axis=1)
print("y0l shape {}".format(y0l.shape))

y1 = np.empty([6250,4043])

for j in range(0,6250):                       # reading all the forward.wav files, coverting to mfcc format, adding labels and storing in an array
    b = "forward"+str(j)+".wav"
    #print b
    data, samplerate = sf.read(b)
    data1 = mfcc(data,samplerate)
    data = data1.reshape(4043,)
    y1[j]=data
y = np.empty([6250,5])
for i in range (0,6250):                      # manually assigning labels
    y[i][0]=0.0
    y[i][1]=1.0
    y[i][2]=0.0
    y[i][3]=0.0
    y[i][4]=0.0
y1l = np.append(y1,y,axis=1)
print("y1l shape {}".format(y1l.shape))  

y2 = np.empty([6250,4043])

for j in range(0,6250):                        # reading all the left.wav files, coverting to mfcc format, adding labels and storing in an array  
    b = "left"+str(j)+".wav"
    #print b
    data, samplerate = sf.read(b)
    data1 = mfcc(data,samplerate)
    data = data1.reshape(4043,)
    y2[j]=data
y = np.empty([6250,5])
for i in range (0,6250):                        # manually assigning labels
    y[i][0]=0.0
    y[i][1]=0.0
    y[i][2]=1.0
    y[i][3]=0.0
    y[i][4]=0.0
y2l = np.append(y2,y,axis=1)
print("y2l shape {}".format(y2l.shape))

y3 = np.empty([6250,4043])                      # reading all the right.wav files, coverting to mfcc format, adding labels and storing in an array
for j in range(0,6250):
    b = "right"+str(j)+".wav"
    #print b
    data, samplerate = sf.read(b)
    data1 = mfcc(data,samplerate)
    data = data1.reshape(4043,)
    y3[j]=data
y = np.empty([6250,5])
for i in range (0,6250):                        # manually assigning labels
    y[i][0]=0.0
    y[i][1]=0.0
    y[i][2]=0.0
    y[i][3]=1.0
    y[i][4]=0.0
y3l = np.append(y3,y,axis=1)
print("y3l shape {}".format(y3l.shape))  

y4 = np.empty([6250,4043])                      # reading all the stop.wav files, coverting to mfcc format, adding labels and storing in an array   
for j in range(0,6250):
    b = "stop"+str(j)+".wav"
    #print b
    data, samplerate = sf.read(b)
    data1 = mfcc(data,samplerate)
    data = data1.reshape(4043,)
    y4[j]=data
y = np.empty([6250,5])
for i in range (0,6250):                         # manually assigning labels
    y[i][0]=0.0
    y[i][1]=0.0
    y[i][2]=0.0
    y[i][3]=0.0
    y[i][4]=1.0
y4l = np.append(y4,y,axis=1)
print("y4l shape {}".format(y4l.shape))







trains = np.empty([27500,4048])                   # using the first 5500 elements of each word in the train set 
k=0
for j in range(0,5500):
    trains[j]=y0l[k]
    k=k+1 
k=0
for j in range(5500,11000):
    trains[j]=y1l[k]
    k=k+1 
k=0
for j in range(11000,16500):
    trains[j]=y2l[k]
    k=k+1 
k=0
for j in range(16500,22000):
    trains[j]=y3l[k]
    k=k+1 
k=0
for j in range(22000,27500):
    trains[j]=y4l[k]
    k=k+1 
print("trains shape {}".format(trains.shape))
np.random.shuffle(trains)






tests = np.empty([3750,4048])                      # using the last 750 elements of each array in the test set
k = 5500
for j in range(0,750):
    tests[j]=y0l[k]
    k=k+1
k = 5500    
for j in range(750,1500):
    tests[j]=y1l[k]
    k=k+1
k = 5500 
for j in range(1500,2250):
    tests[j]=y2l[k]
    k=k+1
k = 5500 
for j in range(2250,3000):
    tests[j]=y3l[k]
    k=k+1 
k = 5500
for j in range(3000,3750):
    tests[j]=y4l[k]
    k=k+1 
print("tests shape {}".format(tests.shape))
np.random.shuffle(tests)







nIn = 4043                                             # nIn = no. of inputs, nOut = no. of outputs, lr = learning rate, nEpochs = no. of epochs, losses = a list to store losses in each epoch
nOut = 5
lr = 0.01
nEpochs = 10
losses = []






def nn_forward(X, Y, W1, b):                           # function which is called to predict output
    x = X.reshape(-1, nIn)
    Y = Y.reshape(-1, nOut)
    #print x.shape
    layer2 = np.dot(x,W1) + b
    out= sigmoid(layer2)
    loss = np.sum(0.5 * (Y - out)**2)
    #losses1.append(loss)
    return out

def train(X, Y, W1, b):                                # function used to train the dataset
    x = X.reshape(-1, nIn)
    Y = Y.reshape(-1, nOut)
    
    layer2 = np.dot(x,W1) + b 
    a_out = sigmoid(layer2)
    
    
    #out = np.dot(a_layer2, W2)
    #a_out = sigmoid(out)
    
    loss = np.sum(0.5 * (Y - a_out)**2)                 # cost function
    #losses.append(loss)
    delta_loss = (Y - a_out) * -sigmoidprime(a_out)     # finding delta loss
    delta_W1 = np.dot(x.T, delta_loss)                  # delta W1 = X(transpose) dot deltaloss
    delta_b  = delta_loss 
    
    #delta_loss = np.dot(delta_loss, W2.T) * sigmoidprime(layer2)
    #delta_W1 = np.dot(X.T.reshape(nIn, 1), delta_loss)

    #print ("a_out",a_out)
    #print Y
    
    W1 = W1 - lr * delta_W1                             # updating value of W1 using gradient descent
    b = b - lr*delta_b                                  # updating value of b using gradient descent

    #aw1.append(W1)
    #aw2.append(W2)
    
    return W1, loss, a_out, b








W1 = np.random.rand(nIn, nOut) * 0.5                    # W1 and b randomly initialised
b  = np.random.rand(1 , nOut)





      
trainX = np.empty([27500,4043])                         # spliting of train set into features and labels          
trainY = np.empty([27500,5])
for i in range(0,27500):
    trainX[i]=trains[i][:4043]
for i in range(0,27500):
    trainY[i]=trains[i][4043:]
print("trainX shape {}".format(trainX.shape))
print("trainY shape {}".format(trainY.shape))

testX = np.empty([3750,4043])                           # spliting of test set into features and labels  
testY = np.empty([3750,5])
for i in range(0,3750):
    testX[i]=tests[i][:4043]
for i in range(0,3750):
    testY[i]=tests[i][4043:]
print("testX shape {}".format(testX.shape))
print("testY shape {}".format(testY.shape))





for j in range(nEpochs):                                # traing the dataset
    for i in range(trainX.shape[0]):
        W1, loss, a_out, b = train(trainX[i], trainY[i], W1, b)
    print("Epoch {} Loss: {}".format(j, loss))
    #print a_out
    losses.append(loss)
              
            
     
correct = 0
total = len(testX)


#print pred 
for i in range(testX.shape[0]):                        # making predictions and calculating accuracy
    pred = np.argmax(nn_forward(testX[i],testY[i], W1, b))
    actual = np.argmax(testY[i])
    
    print("Prediction: Type {}".format(pred))
    print("Actual: Type {}\n".format(actual))
   
    if pred == actual:
        correct +=1
        
print("Accuracy: {}%".format((correct*1.0)/total * 100))

np.savetxt('W1.out',W1,delimiter = ',')                # values of W1 and b stored in different files to be used in the raspberry pi
np.savetxt('b.out',b,delimiter = ',')
#nE = np.linspace(1,500,500)
nE1 = np.linspace(1,nEpochs,nEpochs)                   # plotting loss with respect to no. of epochs
plt.plot(nE1,losses)
#plt.plot(nE,losses1)
#print W1
#print W1.shape
#plt.grid()
#plt.show()

#print aw2 
