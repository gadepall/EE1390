# Speech-Command-Model

## Create Data
Record 80 one second utterences of each command at sampling rate of 16 KHz.

## Split Data
Split the dataset with 20% as test set.
Use Random Seed to reproduce results.
Stratify to have equal number of each different command.

## Augment the data
Augment the data by shifting the data in 25000 length vector

## Feature Extraction
Obtain MFCCs using Kapre(GPU) or Librosa

## Build Model
Model is built mainly based on LSTM and Attention mechanism

## Training
Train the model using Adam optimizer and Sparse Categorical Cross Entropy Loss.
Using Lower batch size is recomended

## Testing
Currently Testing performance is observed as validation set.
