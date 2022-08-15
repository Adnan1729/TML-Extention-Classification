from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle

#Defining the RF base model with default settings 
base_model = RandomForestRegressor()

base_r2_results = []
base_MSE_results = []

def read_and_fit_dataset(dataset):
    
    df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{dataset}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{dataset}_test.csv')
    
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = df_train.pXC50
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = df_test.pXC50
    
    base_model.fit(x_train,y_train)
    pickle.dump(base_model, open(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\models\\base\\{dataset}.sav', "wb"))
    y_pred = base_model.predict(x_test)
    
    #R2 Score Sumary via generating a txt file    
    R2_score = r2_score (y_test, y_pred)
    
    def crt_txt(dataset, R2_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\results\\base_case_r2_scores.txt', "a")
        txt_file.write(f'{dataset} R2 is {R2_score}\n')
        txt_file.close()
    crt_txt(dataset,R2_score)
    
    #MSE Score Sumary via generating a txt file
    MSE_score = mean_squared_error(y_test, y_pred)
    
    def crt_txt(dataset, MSE_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\results\\base_case_MSE-scores.txt', "a")
        txt_file.write(f'{dataset} mean squared score is {MSE_score}\n')
        txt_file.close()
    crt_txt(dataset,MSE_score)
    #
    
    base_r2_results.append(r2_score)
    base_MSE_results.append(MSE_score)
    
    
def main_01():
    datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset in datasets:
        read_and_fit_dataset(dataset)

main_01()

%store base_r2_results
%store base_MSE_results
