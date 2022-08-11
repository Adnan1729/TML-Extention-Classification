from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import numpy as np
import glob 

tml_df_train = []
tml_df_test = []

def load_single_base_model(model):
    base_model = pickle.load(open(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\models\\base\\{model}.sav', 'rb'))
    
    datasets_2 = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    
    for dataset in datasets_2:
        
        def load_files(dataset):
            
            df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{dataset}_train.csv')
            df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{dataset}_test.csv')

            x_train = df_train.drop(columns = ['molecule_id','pXC50'])
            x_test = df_test.drop(columns = ['molecule_id','pXC50'])

            pred_train = base_model.predict (x_train)
            pred_test = base_model.predict (x_test)


            #creating tml training datasets
            x_train.insert(0,"molecule_id", df_train.molecule_id)
            x_train.insert(1,"pXC50", pred_train)
            x_train.to_csv((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\train\\tml_train_{dataset}_predicted_by_model_{model}.csv'))

            #creating tml testing datasets
            x_test.insert(0,"molecule_id", df_test.molecule_id)
            x_test.insert(1,"pXC50", pred_test)
            x_test.to_csv((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\test\\tml_test_{dataset}_predicted_by_model_{model}.csv'))
            
            
        load_files(dataset)
        
def main_2():
    modelsets_2 =  ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for model in modelsets_2:
        load_single_base_model(model)

main_2()

def delete_files(dataset):
    
    os.remove((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\train\\tml_train_{dataset}_predicted_by_model_{dataset}.csv'))   
    os.remove((f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\test\\tml_test_{dataset}_predicted_by_model_{dataset}.csv'))    
def main_21():
    modelsets_21 =  ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset in modelsets_21:
        delete_files(dataset)

main_21()

#ignore the exact name of the variable for the time being. 

def combine_files(dataset):
    files_train = os.path.join(f"C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\train", "*.csv")
    files_test = os.path.join(f"C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml\\{dataset}\\test", "*.csv")
    
    files_train = glob.glob(files_train)
    files_test = glob.glob(files_test)
    
    df_train = pd.concat(map(pd.read_csv, files_train), ignore_index=True)
    df_train = df.drop(df.columns[[0, 1]], axis=1)
    
    df_test = pd.concat(map(pd.read_csv, files_test), ignore_index=True)
    df_test = df.drop(df.columns[[0, 1]], axis=1)



    df_train.to_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_train_{dataset}.csv')
    df_test.to_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_test_{dataset}.csv')
    #data_files_train
    #df_train_tml.to_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_{dataset}.csv')
        
def main_22():
    datasets_22 =  ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset in datasets_22:
        combine_files(dataset)

main_22()
