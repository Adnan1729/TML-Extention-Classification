from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import numpy as np

def create_tml_dataset(dataset_01):
    
    df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset_01}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset_01}_test.csv')
    
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = df_train.pXC50
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = df_test.pXC50
    
    datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    
    for dataset_02 in datasets:
        #loading previously trained base models
        base_model = pickle.load(open(f'C:\\Users\\adnan\\Regression_Analysis\\output\\models\\base\\{dataset_02}.sav', 'rb'))

        #predicting new sets of data using the models        
        df_pred_train = base_model.predict (x_train)
        df_pred_test = base_model.predict (x_test)

        #converting the prediction to datafram so that it can be added to csv files
        pred_train = pd.DataFrame(df_pred_train, columns=['pXC50'])
        pred_test = pd.DataFrame(df_pred_test, columns=['pXC50'])

        #creating tml training datasets
        x_train.insert(0,"molecule_id", df_train.molecule_id)
        x_train.insert(1,"pXC50", pred_train)
        x_train.to_csv((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset_01}_predicted_by_model_{dataset_02}_tml_train.csv'))

        #creating tml testing datasets
        x_test.insert(0,"molecule_id", df_test.molecule_id)
        x_test.insert(1,"pXC50", pred_test)
        x_test.to_csv((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset_01}_predicted_by_model_{dataset_02}_tml_test.csv'))

    

def main_02():
    datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset_01 in datasets:
        create_tml_dataset(dataset_01)

main_02()
