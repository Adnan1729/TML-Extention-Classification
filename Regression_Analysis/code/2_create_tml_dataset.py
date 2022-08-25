from sklearn.ensemble import RandomForestRegressor 
import pandas as pd
import pickle

datasets_2 = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL206', 'CHEMBL208', 'CHEMBL210', 'CHEMBL211', 'CHEMBL214', 'CHEMBL219', 'CHEMBL220',
'CHEMBL221', 'CHEMBL222', 'CHEMBL224', 'CHEMBL225', 'CHEMBL226', 'CHEMBL228', 'CHEMBL230', 'CHEMBL233', 'CHEMBL234', 'CHEMBL247',
'CHEMBL248', 'CHEMBL249', 'CHEMBL251', 'CHEMBL253', 'CHEMBL255', 'CHEMBL256', 'CHEMBL258', 'CHEMBL259', 'CHEMBL260', 'CHEMBL261',
'CHEMBL262', 'CHEMBL264', 'CHEMBL267', 'CHEMBL268', 'CHEMBL269', 'CHEMBL270', 'CHEMBL283', 'CHEMBL284', 'CHEMBL286', 'CHEMBL287',
'CHEMBL289', 'CHEMBL298', 'CHEMBL301', 'CHEMBL302', 'CHEMBL308', 'CHEMBL313', 'CHEMBL318', 'CHEMBL321', 'CHEMBL322', 'CHEMBL325',
'CHEMBL332', 'CHEMBL333', 'CHEMBL335', 'CHEMBL338', 'CHEMBL339', 'CHEMBL340', 'CHEMBL344', 'CHEMBL1800', 'CHEMBL1824', 'CHEMBL1844',
'CHEMBL1862', 'CHEMBL1868', 'CHEMBL1871', 'CHEMBL1914', 'CHEMBL1957', 'CHEMBL1974', 'CHEMBL1981', 'CHEMBL2034', 'CHEMBL2208', 'CHEMBL2276',
'CHEMBL2334', 'CHEMBL2954', 'CHEMBL2971', 'CHEMBL3227', 'CHEMBL3371', 'CHEMBL3397', 'CHEMBL3571', 'CHEMBL3650', 'CHEMBL3706', 'CHEMBL3717']

modelsets_2 = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL206', 'CHEMBL208', 'CHEMBL210', 'CHEMBL211', 'CHEMBL214', 'CHEMBL219', 'CHEMBL220',
'CHEMBL221', 'CHEMBL222', 'CHEMBL224', 'CHEMBL225', 'CHEMBL226', 'CHEMBL228', 'CHEMBL230', 'CHEMBL233', 'CHEMBL234', 'CHEMBL247',
'CHEMBL248', 'CHEMBL249', 'CHEMBL251', 'CHEMBL253', 'CHEMBL255', 'CHEMBL256', 'CHEMBL258', 'CHEMBL259', 'CHEMBL260', 'CHEMBL261',
'CHEMBL262', 'CHEMBL264', 'CHEMBL267', 'CHEMBL268', 'CHEMBL269', 'CHEMBL270', 'CHEMBL283', 'CHEMBL284', 'CHEMBL286', 'CHEMBL287',
'CHEMBL289', 'CHEMBL298', 'CHEMBL301', 'CHEMBL302', 'CHEMBL308', 'CHEMBL313', 'CHEMBL318', 'CHEMBL321', 'CHEMBL322', 'CHEMBL325',
'CHEMBL332', 'CHEMBL333', 'CHEMBL335', 'CHEMBL338', 'CHEMBL339', 'CHEMBL340', 'CHEMBL344', 'CHEMBL1800', 'CHEMBL1824', 'CHEMBL1844',
'CHEMBL1862', 'CHEMBL1868', 'CHEMBL1871', 'CHEMBL1914', 'CHEMBL1957', 'CHEMBL1974', 'CHEMBL1981', 'CHEMBL2034', 'CHEMBL2208', 'CHEMBL2276',
'CHEMBL2334', 'CHEMBL2954', 'CHEMBL2971', 'CHEMBL3227', 'CHEMBL3371', 'CHEMBL3397', 'CHEMBL3571', 'CHEMBL3650', 'CHEMBL3706', 'CHEMBL3717']

#Creating the TML input datasets
def load_single_base_model(dataset):
    
    tml_train = []
    tml_test = []
    
    df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{dataset}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{dataset}_test.csv')
    
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    
    for model in modelsets_2:
        
        base_model = pickle.load(open(f'C:\\Users\\AMahmud\\Regression_Analysis\\output\\models\\base\\{model}.sav', 'rb'))
    
        if dataset == model:
                continue
        
        pred_train = base_model.predict (x_train)
        pred_test = base_model.predict (x_test)

        #columns=f'pXC50_by_{model}'
        pred_train = pd.DataFrame(pred_train)
        pred_test = pd.DataFrame(pred_test)

        pred_train.columns = [f'pXC50_by_{model}']
        pred_test.columns = [f'pXC50_by_{model}']

        tml_train.append(pred_train)
        tml_test.append(pred_test)

        tml_train_df_all = pd.concat(tml_train, axis=1)
        tml_test_df_all = pd.concat(tml_test, axis=1)

        tml_train_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_train_of_{dataset}.csv', index=False)
        tml_test_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_test_of_{dataset}.csv', index=False)
                                       
        
        
        
def main_02():
    
    for dataset in datasets_2:
        load_single_base_model(dataset)

main_02()
