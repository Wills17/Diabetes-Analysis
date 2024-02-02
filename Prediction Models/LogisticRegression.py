#import necessary libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


n = "\n"               #Jump to next line
print("\033c")         #Clear screen

#import dataset
diabetes = pd.read_csv('diabetes.csv')

X = diabetes.drop(['Outcome'], axis=1)  #Remove the outcome column from the dataset
y = diabetes['Outcome']                 #Assign outcome column to variable y
print(X, y)

#Split datasets for training and testing 
X0, X_test, y0, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
print("The shape of X0:", X0.shape)
print("The shape of X_test:", X_test.shape)
print("The shape of y0:", y0.shape)
print("The shape of y_test:", y_test.shape)


print(n)

#Split train data for cross validation purpose
X_train, X_cv, y_train, y_cv = train_test_split(X0, y0, test_size=0.20, random_state=0)
print("The shape of X_train:", X_train.shape)
print("The shape of X_cv:", X_cv.shape)
print("The shape of y_train:", y_train.shape)
print("The shape of y_cv:", y_cv.shape)


#Define classifier
clf = LogisticRegression(max_iter=800)

#fit model on data
clf = clf.fit(X_train, y_train)

#prediction of cross validation
y_cv_pred = clf.predict(X_cv)
print(y_cv_pred)

#check accuracy on cross validation
accuracy1 = accuracy_score(y_cv, y_cv_pred, normalize=True) * 100
print("Accuracy on Cross Validation data is {}%" .format(accuracy1), n)



#fit model on classifier
clf = clf.fit(X_train, y_train)

#prediction of test data
y_pred = clf.predict(X_test)
print(y_pred)

#check accuracy on test data
accuracy2 = accuracy_score(y_test, y_pred, normalize=True) * 100
print("Accuracy on Test data is {}%" .format(accuracy2), n)

#Confusion Matrix
print("Confusion Matrix:", confusion_matrix(y_test,y_pred), n)

#Classification Report
print("Classification report:", classification_report(y_test,y_pred))