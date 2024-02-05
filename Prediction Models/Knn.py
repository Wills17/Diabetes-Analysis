#import necessary libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


n = "\n"               #Jump to next line
print("\033c")         #Clear screen

#import dataset
diabetes = pd.read_csv('Dataset/diabetes.csv')

X = diabetes.drop(['Outcome'], axis=1)  #Remove the outcome column from the dataset
y = diabetes['Outcome']                 #Assign outcome column to variable y
print(X, y, n)

#Split datasets for training and testing
X0, X_test, y0, y_test = train_test_split(X, y, random_state=0, test_size=0.30)
#Split and X0 nd y0 fot cross validation
X_train, X_cv, y_train, y_cv = train_test_split(X0, y0, test_size=0.20, random_state=0)

print("The shape of X_train:", X_train.shape)
print("The shape of X_cv:", X_cv.shape)
print("The shape of X_test:", X_test.shape, n)
print("The shape of y_train:", y_train.shape)
print("The shape of y_cv:", y_cv.shape)
print("The shape of y_test:", X_test.shape, n)



#Test for multiple Ks
i = 0
for i in range(1, 30, 2):
    #Model Classifer
    clf = KNeighborsClassifier(n_neighbors=i, n_jobs=-1)
    
    #fit model on data
    clf = clf.fit(X_train, y_train)
    
    #prediction of cross validation
    y_cv_pred = clf.predict(X_cv)
    #print(y_cv_pred)
    
    #Check accuracy on cross validation
    accuracy1 = accuracy_score(y_cv, y_cv_pred, normalize=True) * 100
    #print("When K = {}, Accuracy on Cross Validation data is {}%" .format(i, accuracy1))
    
    #Pick accuracies >= 76.5%
    if accuracy1 >= 76.5:
        print("When K = {}, Accuracy on Cross Validation data is {}%" .format(i, accuracy1))
print(n)



#Use K = 5 or K = 7 for test

#fit model on classifier
clf = KNeighborsClassifier()
clf = clf.fit(X_train, y_train)

#Prediction on unseen (test) data
y_pred = clf.predict(X_test)
print(y_pred)

#Check accuracy on test data
accuracy2 = accuracy_score(y_test, y_pred, normalize=True) * 100
print("Accuracy on Test data is {}%" .format(accuracy2), n)

#Confusion Matrix
print("Confusion Matrix:", confusion_matrix(y_test,y_pred), n)

#Classification Report
print("Classification report:", classification_report(y_test,y_pred))
