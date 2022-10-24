rom sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd
import pickle
import os

# The Path where all the 500 or 1000 or 1500 or 2000 datasets are stored. "/500" shall be chnaged to "/1000" or "/1500" or "/2000" for scaling up. 
dir_path = r'/content/drive/MyDrive/Classification_Analysis/input/base_raw/500'
all_file_names = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        all_file_names.append(path)

datasets = all_file_names

#Defining the RF base model with default settings. Here only RFClassifier is demonstrated but several other models were used. 
base_model = RandomForestClassifier()

base_accuracy_results = []
base_precision_results = []
base_recall_results = []

def read_and_fit_dataset(dataset):
    
    df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_train.csv')
    df_test = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_test.csv')
    
    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = df_train.pXC50
    x_test = df_test.drop(columns = ['molecule_id','pXC50'])
    y_test = df_test.pXC50
    
    base_model.fit(x_train,y_train)
    pickle.dump(base_model, open(f'C:\\Users\\AMahmud\\Classification_Analysis\\output\\models\\base\\{dataset}.sav', "wb"))
    y_pred = base_model.predict(x_test)
    
     #Accuracy Score Sumary via generating a txt file    
    Accuracy_score = accuracy_score(y_test, y_pred)
    
    def crt_txt(dataset, Accuracy_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\base_case_Accuracy_scores.txt', "a")
        txt_file.write(f'{dataset} R2 is {Accuracy_score}\n')
        txt_file.close()
    crt_txt(dataset,Accuracy_score)
    
    #Precision Score Sumary via generating a txt file
    Precision_score = precision_score(y_test, y_pred)
    
    def crt_txt(dataset, Precision_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\base_case_Precision_scores.txt', "a")
        txt_file.write(f'{dataset} mean squared score is {Precision_score}\n')
        txt_file.close()
    crt_txt(dataset,Precision_score)
    
    #Precision Score Sumary via generating a txt file
    Recall_score = recall_score(y_test, y_pred)
    
    def crt_txt(dataset, Recall_score):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\base_case_Recall_scores.txt', "a")
        txt_file.write(f'{dataset} mean squared score is {Recall_score}\n')
        txt_file.close()
    crt_txt(dataset,Recall_score)
    
    
    base_accuracy_results.append(Accuracy_score)
    base_precision_results.append(Precision_score)
    base_recall_results.append(Recall_score)

    
def main_01():   
    for dataset in datasets:
        read_and_fit_dataset(dataset)

main_01()

%store base_accuracy_results
%store base_precision_results
%store base_recall_results
