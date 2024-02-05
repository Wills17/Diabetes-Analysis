#import necessary libraires

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset file
diabetes = pd.read_csv('Dataset/diabetes.csv')
print(diabetes)


#Pair plot
sns.set_style("whitegrid")
sns.pairplot(diabetes, hue="Outcome", height=2.5, diag_kind="kde")\
    .add_legend()
plt.show()
