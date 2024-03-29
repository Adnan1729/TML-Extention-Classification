from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor 
import pickle
import matplotlib.pyplot as plt

# The Path where all the 500 or 1000 or 1500 or 2000 datasets are stored. "/500" shall be chnaged to "/1000" or "/1500" or "/2000" for scaling up. 
dir_path = r'/content/drive/MyDrive/Classification_Analysis/input/base_raw/500'
all_file_names = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        all_file_names.append(path)

datasets_3 = all_file_names

tml_accuracy_results = []
tml_precision_results = []
tml_recall_results = []

def tml_model_results(model):
    '''This function is where the TML predictions occurs. Here the target dataset gets input from the out of other datasets'''
    
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
