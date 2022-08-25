from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle
import matplotlib.pyplot as plt

modelsets_3 = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL206', 'CHEMBL208', 'CHEMBL210', 'CHEMBL211', 'CHEMBL214', 'CHEMBL219', 'CHEMBL220',
'CHEMBL221', 'CHEMBL222', 'CHEMBL224', 'CHEMBL225', 'CHEMBL226', 'CHEMBL228', 'CHEMBL230', 'CHEMBL233', 'CHEMBL234', 'CHEMBL247',
'CHEMBL248', 'CHEMBL249', 'CHEMBL251', 'CHEMBL253', 'CHEMBL255', 'CHEMBL256', 'CHEMBL258', 'CHEMBL259', 'CHEMBL260', 'CHEMBL261',
'CHEMBL262', 'CHEMBL264', 'CHEMBL267', 'CHEMBL268', 'CHEMBL269', 'CHEMBL270', 'CHEMBL283', 'CHEMBL284', 'CHEMBL286', 'CHEMBL287',
'CHEMBL289', 'CHEMBL298', 'CHEMBL301', 'CHEMBL302', 'CHEMBL308', 'CHEMBL313', 'CHEMBL318', 'CHEMBL321', 'CHEMBL322', 'CHEMBL325',
'CHEMBL332', 'CHEMBL333', 'CHEMBL335', 'CHEMBL338', 'CHEMBL339', 'CHEMBL340', 'CHEMBL344', 'CHEMBL1800', 'CHEMBL1824', 'CHEMBL1844',
'CHEMBL1862', 'CHEMBL1868', 'CHEMBL1871', 'CHEMBL1914', 'CHEMBL1957', 'CHEMBL1974', 'CHEMBL1981', 'CHEMBL2034', 'CHEMBL2208', 'CHEMBL2276',
'CHEMBL2334', 'CHEMBL2954', 'CHEMBL2971', 'CHEMBL3227', 'CHEMBL3371', 'CHEMBL3397', 'CHEMBL3571', 'CHEMBL3650', 'CHEMBL3706', 'CHEMBL3717',
'CHEMBL3837', 'CHEMBL3952', 'CHEMBL4005', 'CHEMBL4124', 'CHEMBL4235', 'CHEMBL4282', 'CHEMBL4296', 'CHEMBL4354', 'CHEMBL4630', 'CHEMBL4722']

#creating empty set of variables for loop purpose
tml_r2_results=[]
tml_MSE_results=[]

def tml_model_results(model):
    
    #loading the model to train with
    base_model = pickle.load(open(f'C:\\Users\\AMahmud\\Regression_Analysis\\output\\models\\base\\{model}.sav', 'rb'))
    
    #loading the files for y variable-- ignore the name of the variable
    base_processed_train = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{model}_train.csv')
    base_processed_test = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\base_processed\\{model}_test.csv')
    
    #loading the files for x variable-- ignore the name of the
    tml_df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_train_of_{model}.csv')
    tml_df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Regression_Analysis\\input\\tml_processed\\tml_dataset_test_of_{model}.csv')
    
    x_train = tml_df_train
    y_train = base_processed_train.pXC50
    x_test = tml_df_test
    y_test = base_processed_test.pXC50
    
    base_model.fit(x_train,y_train)
    y_pred = base_model.predict(x_test)
    
    #R2 Score Sumary via generating a txt file-- ignore the name of the variable    
    R2_score = r2_score (y_test, y_pred)
    def crt_txt(model, R2_score):
        txt_file = open('C:\\Users\\AMahmud\\Regression_Analysis\\output\\results\\tml_case_r2_scores.txt', "a")
        txt_file.write(f'{model} R2 is {R2_score}\n')
        txt_file.close()
    crt_txt(model,R2_score)
    
    #MSE Score Sumary via generating a txt file-- ignore the name of the variable
    MSE_score = mean_squared_error(y_test, y_pred)
    def crt_txt(model, MSE_score):
        txt_file = open('C:\\Users\\AMahmud\\Regression_Analysis\\output\\results\\tml_case_MSE-scores.txt', "a")
        txt_file.write(f'{model} mean squared score is {MSE_score}\n')
        txt_file.close()
    crt_txt(model,MSE_score)
    
    
    tml_r2_results.append(R2_score)
    tml_MSE_results.append(MSE_score)
    
def main_03():
    
    for model in modelsets_3:
        tml_model_results(model)

main_03()

#Calling the base model results
%store -r base_r2_results
%store -r base_MSE_results

# Plotting the r2 values
ds_name = ['203', '204', '205', '206', '208', '210', '211', '214', '219', '220',
           '221', '222', '224', '225', '226', '228', '230', '233', '234', '247',
           '248', '249', '251', '253', '255', '256', '258', '259', '260', '261',
           '262', '264', '267', '268', '269', '270', '283', '284', '286', '287',
           '289' ,'298' ,'301', '302', '308',  '313', '318', '321', '322', '325', 
           '332', '333', '335', '338', '339', '340', '344', '1800', '1824', '1844', 
           '1862', '1868', '1871', '1914', '1957', '1974', '1981', '2034', '2208', '2276', 
           '2334', '2954', '2971', '3227', '3371', '3397', '3571','3650', '3706', '3717', 
          '3837', '3952', '4005', '4124', '4235', '4282', '4296', '4354', '4630', '4722']

plt.plot(ds_name, base_r2_results, color='green', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='green', markersize=.5, label='Base')

plt.plot(ds_name, tml_r2_results, color='blue', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='blue', markersize=.5, label='TML')

plt.axhline(y = max(base_r2_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_r2_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = max(tml_r2_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_r2_results), color = 'b', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('R2 Performance')
plt.title('Base Vs TML Model Performance_90 Trained Models_')
plt.legend()
plt.show() 

#plotting the MSE values
plt.plot(ds_name, base_MSE_results, color='green', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='green', markersize=.5, label='Base')

plt.plot(ds_name, tml_MSE_results, color='blue', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='blue', markersize=.5, label='TML')

##
plt.axhline(y = max(base_MSE_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_MSE_results), color = 'g', linestyle = '-', linewidth = 0.3)

plt.axhline(y = max(tml_MSE_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_MSE_results), color = 'b', linestyle = '-', linewidth = 0.3)
##
plt.ylim(0,2)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('MSE Performance')
plt.title('Base Vs TML Model Performance_90 Trained Models_')
plt.legend()
plt.show()

#Getting the mean of gap between base and tml performances
#R2
r2_b = pd.DataFrame(base_r2_results)
r2_t = pd.DataFrame(tml_r2_results)

R2_error_percent = ((r2_b - r2_t)/r2_b)*100
R2_error_percent.mean(axis=0)

#MSE
MSE_b = pd.DataFrame(base_MSE_results)
MSE_t = pd.DataFrame(tml_MSE_results)

MSE_error_percent = ((MSE_b - MSE_t)/MSE_b)*100
MSE_error_percent.mean(axis=0)
