from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle

base_path = f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed'
base_model = RandomForestRegressor()

base_r2_results = []

def read_and_fit_dataset(dataset):
    
    df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset}_test.csv')
    
    #Defining the dependent and independent varibales 
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = df_train.pXC50
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = df_test.pXC50
   
    #Fitting the model and storing it as .sav file 
    base_model.fit(x_train,y_train)
    pickle.dump(base_model, open(f'C:\\Users\\adnan\\Regression_Analysis\\output\\models\\base\\{dataset}.sav', "wb"))
    
    r2_score = base_model.score (x_test,y_test)
    
    #Creating a single text file to store R2 score. Example: CHEMBL203 r2 score is 0.752974. 
    def crt_txt(dataset,r2_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis\\output\\results\\base_case.txt', "a")
        txt_file.write(f'{dataset} r2 is {r2_score}\n')
        txt_file.close()
    crt_txt(dataset,r2_score)
    
    base_r2_results.append(r2_score)
    
    
def main_01():
    datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset in datasets:
        read_and_fit_dataset(dataset)

main_01()

#Visualisation

import matplotlib.pyplot as plt

ds_name = ["203", "204", "205", "228", "233", 
     "251", "253", "260", "267", "339"]

plt.plot(ds_name, base_r2_results, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5)

plt.axhline(y = max(base_r2_results), color = 'r', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_r2_results), color = 'r', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('R2 Performance')
plt.title('Base Model Performance')
plt.show()
