"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys='../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)


#split data into training and testing
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

#DT classifier and accuracy score
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
print(pred) #4 POI's are predicted
print(len(features_test)) #29 people in test set
print "Accuracy if all zeros: ", accuracy_score([0]*29, labels_test)
print(clf.score(features_test,labels_test))

#precision score and recall score
from sklearn.metrics import precision_score, recall_score
print(precision_score(labels_test, pred))
print(recall_score(labels_test, pred))


