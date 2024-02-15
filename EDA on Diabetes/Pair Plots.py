#import necessary libraires

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset and ensure dataset is in folder
try: 
    diabetes = pd.read_csv('Dataset/diabetes.csv')
except FileNotFoundError:
    print("Please ensure that the file is in the folder 'Dataset' and try again.") 
    quit()

print(diabetes)


#Pair plot
sns.set_style("whitegrid")
sns.pairplot(diabetes, hue="Outcome", height=2.5, diag_kind="kde")\
    .add_legend()
plt.show()
