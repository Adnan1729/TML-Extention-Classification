#Creating the TML input datasets
def load_single_base_model(model):
    base_model = pickle.load(open(f'C:\\Users\\AMahmud\\Regression_Analysis\\output\\models\\base\\{model}.sav', 'rb'))
    tml_train = []
    tml_test = []
    
    for dataset in datasets_2:
        
        if dataset == model:
                continue
        
        def load_files(dataset):
            
            
            df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{dataset}_train.csv')
            df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{dataset}_test.csv')
            
            x_train = df_train.drop(columns = ['molecule_id','pXC50'])
            x_test = df_test.drop(columns = ['molecule_id','pXC50'])
            
            pred_train = base_model.predict (x_train)
            pred_test = base_model.predict (x_test)
            
            #columns=f'pXC50_by_{model}'
            pred_train = pd.DataFrame(pred_train)
            pred_test = pd.DataFrame(pred_test)
            
            pred_train.columns = [f'pXC50_{dataset}_by_{model}']
            pred_test.columns = [f'pXC50_{dataset}_{model}']
            
            tml_train.append(pred_train)
            tml_test.append(pred_test)
            
#             tml_train_df = pd.DataFrame(tml_train)
#             tml_test_df = pd.DataFrame(tml_test)
            
#             tml_train_df.drop(columns = [f'pXC50_{dataset}_by_{dataset}'])
#             tml_test_df.drop(columns = [f'pXC50_{dataset}_by_{dataset}'])
            
            tml_train_df_all = pd.concat(tml_train, axis=1)
            #tml_train_df_all.drop(columns = [f'pXC50_{model}_by_{model}'])
            
            tml_test_df_all = pd.concat(tml_test, axis=1)
            #tml_test_df_all.drop(columns = [f'pXC50_{model}_by_{model}'])
            
            tml_train_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_train_by_model_{model}.csv', index=False)
            tml_test_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_test_by_model_{model}.csv', index=False)
                                       
        load_files(dataset)
        
#         tml_train_df_all = pd.concat(tml_train_df, axis=1) 
#         tml_test_df_all = pd.concat(tml_test_df, axis=1)
            
#         tml_train_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_train_{dataset}.csv', index=False)
#         tml_test_df_all.to_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_test_{dataset}.csv', index=False)
        
def main_2():
    for model in modelsets_2:
        load_single_base_model(model)

main_2()
