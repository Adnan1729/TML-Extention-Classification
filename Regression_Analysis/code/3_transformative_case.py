from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import matplotlib.pyplot as plt

#predicting and getting the performance matrices of tml model
tml_r2_results=[]
tml_MSE_results=[]
def tml_model_results(model):
    
    #loading the model to train with
    base_model = pickle.load(open(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\models\\base\\{model}.sav', 'rb'))
    
    #loading the files for y variable-- ignore the name of the variable
    base_processed_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{model}_train.csv')
    base_processed_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\processed\\{model}_test.csv')
    
    #loading the files for x variable-- ignore the name of the variable
    tml_df_train = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_train_{model}.csv')
    tml_df_test = pd.read_csv(f'C:\\Users\\adnan\\Regression_Analysis_RP050822\\input\\tml_processed\\tml_dataset_test_{model}.csv')
    
    x_train = tml_df_train
    y_train = base_processed_train.pXC50
    x_test = tml_df_test
    y_test = base_processed_test.pXC50
    
    base_model.fit(x_train,y_train)
    y_pred = base_model.predict(x_test)
    
    #R2 Score Sumary via generating a txt file-- ignore the name of the variable    
    R2_score = r2_score (y_test, y_pred)
    def crt_txt(model, R2_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\results\\tml_case_r2_scores.txt', "a")
        txt_file.write(f'{model} R2 is {R2_score}\n')
        txt_file.close()
    crt_txt(model,R2_score)
    
    #MSE Score Sumary via generating a txt file-- ignore the name of the variable
    MSE_score = mean_squared_error(y_test, y_pred)
    def crt_txt(model, MSE_score):
        txt_file = open('C:\\Users\\adnan\\Regression_Analysis_RP050822\\output\\results\\tml_case_MSE-scores.txt', "a")
        txt_file.write(f'{model} mean squared score is {MSE_score}\n')
        txt_file.close()
    crt_txt(model,MSE_score)
    
    
    tml_r2_results.append(r2_score)
    tml_MSE_results.append(MSE_score)
    
def main_30():
    modelsets_30 =  ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']
    for model in modelsets_30:
        tml_model_results(model)

main_30()

%store -r base_r2_results
%store -r base_MSE_results

# Plotting the r2 values
ds_name = ["203", "204", "205", "228", "233", 
     "251", "253", "260", "267", "339"]

plt.plot(ds_name, base_r2_results, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5, label='Base')

plt.plot(ds_name, tml_r2_results, color='black', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5, label='TML')


plt.axhline(y = max(base_r2_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_r2_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = max(tml_r2_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_r2_results), color = 'b', linestyle = '-', linewidth = 0.3)


plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('R2 Performance')
plt.title('Base Vs TML Model Performance')
plt.legend()
plt.show() 

#plotting the MSE values
ds_name = ["203", "204", "205", "228", "233", 
     "251", "253", "260", "267", "339"]
##

plt.plot(ds_name, base_MSE_results, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5, label='Base')

plt.plot(ds_name, tml_MSE_results, color='black', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5, label='TML')

##
plt.axhline(y = max(base_MSE_results), color = 'r', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_MSE_results), color = 'r', linestyle = '-', linewidth = 0.3)

plt.axhline(y = max(tml_MSE_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_MSE_results), color = 'b', linestyle = '-', linewidth = 0.3)
##
plt.ylim(0,2)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('MSE Performance')
plt.title('Base Vs TML Model Performance')
plt.legend()
plt.show()
