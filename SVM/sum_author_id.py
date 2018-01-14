""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
from sklearn import svm
from sklearn.metrics import accuracy_score
features_train, features_test, labels_train, labels_test = preprocess()
clf = svm.SVC(C=10000,kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time() - t1, 3), "s"

accuracy = accuracy_score(labels_test, pred)
print(accuracy)

print(sum(pred)) #prints how many times "1" is in the prediction list

# before slicing dataset:
# training time: 195.075 s
# predicting time: 21.538 s
# accuracy: 0.984072810011

# after slicing dataset to 1% of original size (lines 25-26):
# training time: 0.113 s
# predicting time: 1.193 s
# accuracy: 0.884527872582

# after changing kernel from linear to rbf:
# training time: 0.127 s
# predicting time: 1.302 s
# accuracy: 0.616040955631

# when C=10
# accuracy: 0.616040955631

# when C=10000
# accuracy: 0.892491467577

# back to original dataset
# accuracy: 0.990329920364
