#import necessary libraires

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset file
diabetes = pd.read_csv('Dataset/diabetes.csv')
#print(diabetes)
print(diabetes.head())


x = "Outcome" #assigning variable (column) for x axis

#Box plot for Pregnancies vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, x=x ,y="Pregnancies", hue=x)
plt.title("Box plot of Pregnancies vs Outcome")    
plt.ylabel("Pregnancies")
plt.xlabel("Outcome")
plt.legend(loc="center")
plt.show()


#Box plot for GLucose vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data= diabetes, x=x, y="Glucose", hue=x)
plt.title("Box plot of Glucose vs Outcome")
plt.xlabel(x)
plt.ylabel("Glucose")
plt.legend(loc="center")
plt.show()


#Box plot for Blood Pressure vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, x=x, y="BloodPressure", hue=x)
plt.title("Box plot of Blood Pressure vs Outcome")
plt.legend(loc="center")
plt.xlabel(x)
plt.ylabel("Blood Presuure")
plt.show()

#Box plot for Skin Thickness vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, x=x, y="SkinThickness", hue=x)
plt.title("Box plot of Skin Thickness vs Outcome")
plt.xlabel(x)
plt.ylabel("Skin Thickness")
plt.legend(loc="center")
plt.show()


#Box plot for Insulin vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, hue=x, x=x, y="Insulin")
plt.title("Box plot of Insulin vs Outcome")
plt.ylabel("Insulin")
plt.xlabel(x)
plt.legend(loc="center")
plt.show()


#Box plot for BMI vs Outcome
sns.set_style("darkgrid")
sns.violinplot(hue=x, data=diabetes, x=x, y="BMI")
plt.legend(loc="center")
plt.title("Box plot for BMI vs Outcome")
plt.xlabel(x)
plt.ylabel("BMI")
plt.show()


#Box plot for Diabetes Pedigree Function vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, hue=x, x=x, y="DiabetesPedigreeFunction")
plt.title("Box plot for Diabetes Pedigree Function vs Outcome")
plt.legend(loc="center")
plt.xlabel(x)
plt.ylabel("Diabetes Pedigree Function")
plt.show()


#Box plot for Age vs Outcome
sns.set_style("darkgrid")
sns.violinplot(data=diabetes, hue=x, x=x, y="Age")
plt.title("Box plot of Age vs Outcome")
plt.legend(loc="center")
plt.xlabel(x)
plt.ylabel("Age")
plt.show()