#import necessary libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

import time

print("\033c")         #Clear screen
n = "\n"               #Jump to next line

#import dataset and ensure dataset is in folder
try: 
    diabetes = pd.read_csv('Dataset/diabetes.csv')
except FileNotFoundError:
    print("Please ensure that the dataset is in the folder 'Dataset' and try again.") 
    quit()

X = diabetes.drop(['Outcome'], axis=1)  #Remove the outcome column from the dataset
y = diabetes['Outcome']                 #Assign outcome column to variable y
#print(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=30)


#Confirm request to take inputs from users
def Ask_to_input(): 
    """This function is meant to confirm is user really want to
    test with real data."""
    
    print("Do you want to check with your provided data?")
    ans1 = input("Input 'y' for Yes or any other key to quit\nUser: ")
    ans1 = ans1.lower()
    print()
    if ans1 == "yes" or ans1 == "y" or ans1 == "Y":
        time.sleep(1.5)
        inputs()
    else:
        time.sleep(1)
        print("Exit program?")
        ans2 = input("Input 'y' to confirm\nUser: ")
        ans2 = ans2.lower()
        print()
        if ans2 == "yes" or ans2 == "y":
            quit()
        else:
            print("Wrong input!!!")
            time.sleep(0.5)
            print("Try again.")
            print("Restarting in 3...")
            time.sleep(1)
            print("Restarting in 2...")
            time.sleep(1)
            print("Restarting in 1...")
            time.sleep(1)
            print("0\33c")
            Ask_to_input()


#Take each input and assign to dataset.
def inputs():
    """This function takes a patient's details for processing by model while handling errors in user's input"""
    print()
    print("Please ensure to input correct details for accurate prediction")
    try:
        Preg = int(input("Input for Pregnancies: "))
    except ValueError:
        print("You didn't input an integer, please try again")
        Preg = int(input("Input for Pregnancies: "))
        
    try:
        Glucose = int(input("Input for Glucose: "))
    except ValueError: 
        print("You didn't input an integer, please try again")
        Glucose = int(input("Input for Glucose: "))
        
    try:
        BP = int(input("Input for Blood Pressure: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        BP = int(input("Input for Blood Pressure: "))
        
    try:
        SkinThick = int(input("Input for Skin Thickness: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        SkinThick = int(input("Input for Skin Thickness: "))
        
    try:
        Insulin = int(input("Input for Insulin: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        Insulin = int(input("Input for Insulin: "))
    
    try:
        BMI = float(input("Input for BMI: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        BMI = float(input("Input for BMI: "))
        
    try:
        DPF = float(input("Input for Diabetes Pedigree Function: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        DPF = float(input("Input for Diabetes Pedigree Function: "))
        
    try:
        Age = int(input("Input for Age: "))
    except ValueError: 
        print("You didn't input an integer please try again")
        Age = int(input("Input for Age: "))
    
    Test_list = [[Preg, Glucose, BP, SkinThick, Insulin, BMI, DPF, Age]]
    print()
    print("Here are your inputs")
    time.sleep(2)
    print("Pregancies:", Preg)
    print("Glucose:", Glucose)
    print("Blood Pressure:", BP)
    print("Skin Thickness:", SkinThick)
    print("Insulin:", Insulin)
    print("BMI:", BMI)
    print("Diabetes Pedigree Function:", DPF)
    print("Age:", Age)
    time.sleep(2)
    
    # Correct details inputed?
    print()
    print("Please check your inputs again.\nAre they correct?")
    c_input = input("Input 'y' for Yes or any other key to redo\nUser: ")
    c_input = c_input.lower()
    if c_input == "y" or c_input == "yes":
        pass
    else:
        print()
        time.sleep(2)
        print("Input details again, please")
        time.sleep(2)
        inputs()

    time.sleep(3)
    # Function for different model prediction
    def pred_models():
        """Function to select between different available models of choice"""
        print()
        print("Which Model Prediction would you like to use?")
        print("1. Logistic Regression")
        print("2. K-Neighbors Classifier")
        
        time.sleep(1)
        model_choice = input("\nSelect choice by typing '1' or '2' or any other number as indicated\nUser: ")
        
        if model_choice == "1":
            clf = LogisticRegression(max_iter=800)
            clf = clf.fit(X_train,y_train)
            pred = clf.predict(Test_list)
            print(n)
            print("If warning message displays, please ignore")
            #print(pred[0])
            time.sleep(4)
            if pred[0] == 0:
                print("Great, patient is not diabetic")
            else:
                print("Unfortunately, patient is diabetic")
            
        elif model_choice == "2":
            clf = KNeighborsClassifier()
            clf = clf.fit(X_train, y_train)
            pred = clf.predict(Test_list)
            print(n)
            print("If warning message displays, please ignore")
            #print(pred[0])
            time.sleep(4)
            if pred[0] == 0:
                print("Great, patient is not diabetic")
            else:
                print("Unfortunately, patient is diabetic")
            
        else:
            time.sleep(4)
            print("Wrong input!!!\nTry again.")
            pred_models()
            
    pred_models() #call prediction function
    print(n)
    print("Do you want to quit program?")
    ans3 = input("Input 'y' for Yes or any other key to make another prediction\nUser: ")
    ans3 = ans3.lower()
    if ans3 =='y' or ans3 == "yes":
        time.sleep(1)
        print("Program exited")
        time.sleep(3)
        print("0\33c") #clear screen
        quit()
    else:
        print("Restarting in 3...")
        time.sleep(1)
        print("Restarting in 2...")
        time.sleep(1)
        print("Restarting in 1...")
        time.sleep(1)
        print("0\33c")
        inputs()



#Call entire program
Ask_to_input()
