from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import matplotlib.pyplot as plt


tml_r2_results=[]
def tml_model_results(model):
    base_model = pickle.load(open(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\models\\base\\{model}.sav', 'rb'))
    
    tml_df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_train_{model}.csv')
    tml_df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_test_{model}.csv')
    
    x_train = tml_df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = tml_df_train.pXC50
    x_test = tml_df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = tml_df_test.pXC50
    
    r2_score = base_model.score (x_test,y_test)
    
    def crt_txt(model,r2_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis\\output\\results\\base_case.txt', "a")
        txt_file.write(f'{model} r2 is {r2_score}\n')
        txt_file.close()
    crt_txt(model,r2_score)
    
    tml_r2_results.append(r2_score)
    
def main_2():
    modelsets_2 =  ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for model in modelsets_2:
        tml_model_results(model)

main_2()                   
