#import necessary libraires

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = "\n" #Jump to next line

#import dataset file
diabetes = pd.read_csv('diabetes.csv')
#print(diabetes)
#print(diabetes.columns)

print("Overview of file:\n", diabetes.head(), n )

print("Description of file:\n", diabetes.describe(), n)

print("The shape of file is:", diabetes.shape, n)

#value Counts for each column
for columns in diabetes.columns:
    print((diabetes[columns]).value_counts, n)


#Histogram for each column
#For pregnancies
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "Pregnancies")
plt.title("Histogram of Pregancies")
plt.legend()    
plt.xlabel("Pregancies")
plt.show()


#For Glucose
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "Glucose")
plt.title("Histogram of Glucose")
plt.legend()    
plt.xlabel("Glucose")
plt.show()


#For Blood Pressure
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "BloodPressure")
plt.title("Histogram of Blood Pressure")
plt.legend()    
plt.xlabel("BloodPressure")
plt.show()


#For Skin Thickness
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "SkinThickness")
plt.title("Histogram of Skin Thickness")
plt.legend()    
plt.xlabel("SkinThickness")
plt.show()


#For Insulin
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "Insulin")
plt.title("Histogram of Insulin")
plt.legend()    
plt.xlabel("Insulin")
plt.show()


#For BMI
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "BMI")
plt.title("Histogram of BMI")
plt.legend()    
plt.xlabel("BMI")
plt.show()


#For Diabetes Pedigree Function
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "DiabetesPedigreeFunction")
plt.title("Histogram of Diabetes Pedigree Function")
plt.legend()    
plt.xlabel("Diabetes Pedigree Function")
plt.show()


#For Age
sns.set_style("darkgrid")
sns.FacetGrid(diabetes, hue="Outcome", height=3)\
    .map(sns.histplot, "Age")
plt.title("Histogram of Age")
plt.legend()    
plt.xlabel("Age")
plt.show()