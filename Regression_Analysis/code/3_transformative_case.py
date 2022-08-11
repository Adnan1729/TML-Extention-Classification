from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import matplotlib.pyplot as plt


tml_r2_results = []

def read_and_fit_dataset(dataset):
    
    tml_df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset}_train.csv')
    tml_df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis\\input\\processed\\{dataset}_test.csv')
    
    x_train = tml_df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = tml_df_train.pXC50
    x_test = tml_df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = tml_df_test.pXC50
    
    base_model = pickle.load(open(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\models\\base\\{dataset}.sav', 'rb')

    base_model.fit(x_train,y_train)
    
    r2_score = base_model.score (x_test,y_test)
    
    def crt_txt(dataset,r2_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis\\output\\results\\tml_case.txt', "a")
        txt_file.write(f'tml {dataset} r2 score is {r2_score}\n')
        txt_file.close()
    crt_txt(dataset,r2_score)
    
    tml_r2_results.append(r2_score)
    
    
def main_3():
    datasets_3 = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for dataset in datasets_3:
        read_and_fit_dataset(dataset)

main_3()
                             
