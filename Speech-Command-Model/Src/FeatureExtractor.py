import numpy as np
from tensorflow.keras.models import Sequential,Model
from kapre.time_frequency import Melspectrogram
from kapre.utils import Normalization2D
from tensorflow.keras import layers as L

data_dir = '../Data/Pradeep_16/'
x_train = np.load(data_dir+'x_train.npy')
y_train = np.load(data_dir+'y_train.npy')
x_test = np.load(data_dir+'x_test.npy')
y_test = np.load(data_dir+'y_test.npy')

mfcc = Sequential()
mfcc.add(L.Reshape((1, -1)))
mfcc.add(Melspectrogram(padding='same', sr=16000, n_mels=39, n_dft = 1024,
                        power_melgram=2.0, return_decibel_melgram=True,
                        trainable_fb=False, trainable_kernel=False,
                        name='mel_stft'))
mfcc.add(Normalization2D(str_axis='freq'))
mfcc.add(L.Permute((2, 1, 3)))

x_train = mfcc.predict(x_train)
x_train.shape

x_test = mfcc.predict(x_test)
x_test.shape

np.save('mfcc_test.npy',x_test)
np.save('mfcc_train.npy',x_train)