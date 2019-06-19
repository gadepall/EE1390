# -*- coding: utf-8 -*-
import numpy as np
import pickle
import random
from convnet import *
from PIL import Image
from preprocessing import *

#CNN
#ARCHITECTURE : [INPUT - CONV1 - RELU - CONV2 - RELU- MAXPOOL - FC1 - OUT]


## Hyperparameters
NUM_OUTPUT = 10
LEARNING_RATE = 0.01	#learning rate
IMG_WIDTH = 28
IMG_DEPTH = 1
FILTER_SIZE=5
NUM_FILT1 = 8
NUM_FILT2 = 8
BATCH_SIZE = 20
NUM_EPOCHS = 2	 # number of iterations
MU = 0.95

#PICKLE_FILE = 'output.pickle'
PICKLE_FILE = 'trained.pickle'

## Opening the saved model parameter
pickle_in = open(PICKLE_FILE, 'rb')
out = pickle.load(pickle_in)

[filt1, filt2, bias1, bias2, theta3, bias3, cost, acc] = out

#Testing
for n in range(0,10):
	x=('28pix/img('+str(n)+').png')#file path here
	col = Image.open(x)
	gray = col.convert('L')
	#bw = gray.point(lambda x: 0 if x<128 else 255, '1')
	#bw.save("result_bw.png")
	#x=preprocess(x)
	img=np.array(gray)
	#print(img)
	#print(len(img),len(img[0]))
	img = preprocess(img)



	digit, prob = predict(img, filt1, filt2, bias1, bias2, theta3, bias3)
	print('Correct Digit: '+str(n)+' Predicted Digit: '+str(digit)+' Probability: '+str(prob))


