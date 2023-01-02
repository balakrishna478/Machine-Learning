
print('\n')
import numpy as np
# Parse data from training and testing data
training_attributes = np.loadtxt('iris-training-data.csv', delimiter=',', usecols=(0,1,2,3))
training_labels = np.loadtxt('iris-training-data.csv',dtype='S', delimiter=',', usecols=(4))
testing_attributes = np.loadtxt('iris-testing-data.csv', delimiter=',', usecols=(0,1,2,3))
testing_labels = np.loadtxt('iris-testing-data.csv',dtype='S', delimiter=',', usecols=(4))
# Finding distance from test data to training data
distances = np.sqrt((np.square(testing_attributes[:,np.newaxis]-training_attributes)).sum(axis=2))
print("# ","   True","    Predicted",sep=",")
k=0
for i in range(len(training_labels)):
    x = np.argmin(distances[i,:])
    print(i+1  , training_labels[i].decode()  , testing_labels[x].decode(),sep=",")
    if training_labels[i]==testing_labels[x]:
        k+=1
    res=round((k/75)*100,2)
print("Accuraracy:",res,"%")




