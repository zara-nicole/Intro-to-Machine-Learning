""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)

#print(len(features_train[0])) # number of features in the data

pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test, pred)
print(accuracy)

# number of features in data when percentile=10 : 3785
# number of features in data when percentile=1 : 379
# Having fewer features means there are fewer chances for the decision tree to carve out very specific little spots when finding a decision surface.  These specific little spots (evidence of a high-variance result) indicate a more complex decision-making process



