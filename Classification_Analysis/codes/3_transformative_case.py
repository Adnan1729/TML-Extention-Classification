from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import matplotlib.pyplot as plt


tml_accuracy_results = []
tml_precision_results = []
tml_recall_results = []

def tml_model_results(model):
    
    #loading the model to train with
    base_model = pickle.load(open(f'C:\\Users\\AMahmud\\Classification_Analysis\\output\\models\\base\\{model}.sav', 'rb'))
    
    #loading the files for y variable-- ignore the name of the variable
    base_processed_train = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{model}_train.csv')
    base_processed_test = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{model}_test.csv')
    
    #loading the files for x variable-- ignore the name of the
    tml_df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\tml_processed\\tml_dataset_train_of_{model}.csv')
    tml_df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\tml_processed\\tml_dataset_test_of_{model}.csv')
    
    x_train = tml_df_train
    y_train = base_processed_train.pXC50
    x_test = tml_df_test
    y_test = base_processed_test.pXC50
    
    base_model.fit(x_train,y_train)
    y_pred = base_model.predict(x_test)
    
      #Accuracy Score Sumary via generating a txt file    
    Accuracy_score = accuracy_score(y_test, y_pred)
    
    def crt_txt(model, Accuracy_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\tml_case_Accuracy_scores.txt', "a")
        txt_file.write(f'{model} R2 is {Accuracy_score}\n')
        txt_file.close()
    crt_txt(model,Accuracy_score)
    
    #Precision Score Sumary via generating a txt file
    Precision_score = precision_score(y_test, y_pred)
    
    def crt_txt(model, Precision_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\tml_case_Precision_scores.txt', "a")
        txt_file.write(f'{model} mean squared score is {Precision_score}\n')
        txt_file.close()
    crt_txt(model,Precision_score)
    
    #Precision Score Sumary via generating a txt file
    Recall_score = recall_score(y_test, y_pred)
    
    def crt_txt(model, Recall_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\tml_case_Recall_scores.txt', "a")
        txt_file.write(f'{model} mean squared score is {Recall_score}\n')
        txt_file.close()
    crt_txt(model,Recall_score)
    
    
    tml_accuracy_results.append(Accuracy_score)
    tml_precision_results.append(Precision_score)
    tml_recall_results.append(Recall_score)
    

def main_3():
    
    for model in modelsets_3:
        tml_model_results(model)

main_3()


%store -r base_accuracy_results
%store -r base_precision_results
%store -r base_recall_results

#----------------------------------#
#Accuracy
ds_name = ['203', '204', '205', '206', '208', '210', '211', '214', '219', '220',
           '221', '222', '224', '225', '226', '228', '230', '233', '234', '247',
           '248', '249', '251', '253', '255', '256', '258', '259', '260', '261',
           '262', '264', '267', '268', '269', '270', '283', '284', '286', '287',
           '289' ,'298' ,'301', '302', '308',  '313', '318', '321', '322', '325', 
           '332', '333', '335', '338', '339', '340', '344', '1800', '1824', '1844', 
           '1862', '1868', '1871', '1914', '1957', '1974', '1981', '2034', '2208', '2276', 
           '2334', '2954', '2971', '3227', '3371', '3397', '3571','3650', '3706', '3717']

plt.plot(ds_name, base_accuracy_results, color='green', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='green', markersize=.5, label='Base')

plt.plot(ds_name, tml_accuracy_results, color='blue', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='blue', markersize=.5, label='TML')

plt.axhline(y = max(base_accuracy_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_accuracy_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = max(tml_accuracy_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_accuracy_results), color = 'b', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('Accuracy Performance')
plt.title('Classification: Base Vs TML Model Performance_80 Trained Models')
plt.legend()
plt.show() 


#Precision

plt.plot(ds_name, base_precision_results, color='green', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='green', markersize=.5, label='Base')

plt.plot(ds_name, tml_precision_results, color='blue', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='blue', markersize=.5, label='TML')

plt.axhline(y = max(base_precision_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_precision_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = max(tml_precision_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_precision_results), color = 'b', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('Precision Performance')
plt.title('Classification: Base Vs TML Model Performance_80 Trained Models')
plt.legend()
plt.show()


#Recall

plt.plot(ds_name, base_recall_results, color='green', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='green', markersize=.5, label='Base')

plt.plot(ds_name, tml_recall_results, color='blue', linestyle='solid', linewidth = .5,
		marker=',', markerfacecolor='blue', markersize=.5, label='TML')

plt.axhline(y = max(base_recall_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_recall_results), color = 'g', linestyle = '-', linewidth = 0.3)
plt.axhline(y = max(tml_recall_results), color = 'b', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(tml_recall_results), color = 'b', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('Recall Performance')
plt.title('Classification: Base Vs TML Model Performance_80 Trained Models')
plt.legend()
plt.show()


#----------------------------------#
#Mean Accuracy 
acc_b = pd.DataFrame(base_accuracy_results)
acc_t = pd.DataFrame(tml_accuracy_results)

Acc_error_percent = ((acc_b - acc_t)/acc_b)*100
Acc_error_percent.mean(axis=0)

#Mean Precision 
pres_b = pd.DataFrame(base_precision_results)
pres_t = pd.DataFrame(tml_precision_results)

Pres_error_percent = ((pres_b - pres_t)/pres_b)*100
Pres_error_percent.mean(axis=0)

#Mean Recall
rc_b = pd.DataFrame(base_recall_results)
rc_t = pd.DataFrame(tml_recall_results)

Rc_error_percent = ((rc_b - rc_t)/rc_b)*100
Rc_error_percent.mean(axis=0)
