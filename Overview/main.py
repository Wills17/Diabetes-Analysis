#import necessary libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


n = "\n"            #Jump to next line

#import dataset dataset
diabetes = pd.read_csv('Dataset/diabetes.csv')
print(diabetes)
print(diabetes.columns)
print("\033c")      #Clear screen

print("Overview of dataset:\n", diabetes.head(), n )

print("Description of dataset:\n", diabetes.describe(), n)

print("The shape of dataset is:", diabetes.shape, n)

