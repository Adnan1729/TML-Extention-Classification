from sklearn.ensemble import RandomForestClassifier 
import pandas as pd
import os
import pickle
import numpy as np
import glob 
import os

# The Path where all the 500 or 1000 or 1500 or 2000 datasets are stored. "/500" shall be chnaged to "/1000" or "/1500" or "/2000" for scaling up. 
dir_path = r'/content/drive/MyDrive/Classification_Analysis/input/base_raw/500'
all_file_names = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        all_file_names.append(path)

datasets_2 = all_file_names
modelsets_2 = all_file_names

#Creating the TML input datasets
def load_single_base_model(dataset):
    
    tml_train = []
    tml_test = []
    
    df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_test.csv')
    
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    
    for model in modelsets_2:
        
        base_model = pickle.load(open(f'C:\\Users\\AMahmud\\Classification_Analysis\\output\\models\\base\\{model}.sav', 'rb'))
    
        if dataset == model:
                continue
            
        pred_train = base_model.predict (x_train)
        pred_test = base_model.predict (x_test)

        pred_train = pd.DataFrame(pred_train)
        pred_test = pd.DataFrame(pred_test)

        pred_train.columns = [f'pXC50_by_{model}']
        pred_test.columns = [f'pXC50_by_{model}']

        tml_train.append(pred_train)
        tml_test.append(pred_test)

        tml_train_df_all = pd.concat(tml_train, axis=1)
        tml_test_df_all = pd.concat(tml_test, axis=1)

        tml_train_df_all.to_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\tml_processed\\tml_dataset_train_of_{dataset}.csv', index=False)
        tml_test_df_all.to_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\tml_processed\\tml_dataset_test_of_{dataset}.csv', index=False)
                                             
def main_2():
    
    for dataset in datasets_2:
        load_single_base_model(dataset)

main_2()
