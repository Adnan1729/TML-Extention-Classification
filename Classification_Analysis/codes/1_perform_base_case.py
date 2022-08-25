rom sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd
import pickle

datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL206', 'CHEMBL208', 'CHEMBL210', 'CHEMBL211', 'CHEMBL214', 'CHEMBL219', 'CHEMBL220',
'CHEMBL221', 'CHEMBL222', 'CHEMBL224', 'CHEMBL225', 'CHEMBL226', 'CHEMBL228', 'CHEMBL230', 'CHEMBL233', 'CHEMBL234', 'CHEMBL247',
'CHEMBL248', 'CHEMBL249', 'CHEMBL251', 'CHEMBL253', 'CHEMBL255', 'CHEMBL256', 'CHEMBL258', 'CHEMBL259', 'CHEMBL260', 'CHEMBL261',
'CHEMBL262', 'CHEMBL264', 'CHEMBL267', 'CHEMBL268', 'CHEMBL269', 'CHEMBL270', 'CHEMBL283', 'CHEMBL284', 'CHEMBL286', 'CHEMBL287',
'CHEMBL289', 'CHEMBL298', 'CHEMBL301', 'CHEMBL302', 'CHEMBL308', 'CHEMBL313', 'CHEMBL318', 'CHEMBL321', 'CHEMBL322', 'CHEMBL325',
'CHEMBL332', 'CHEMBL333', 'CHEMBL335', 'CHEMBL338', 'CHEMBL339', 'CHEMBL340', 'CHEMBL344', 'CHEMBL1800', 'CHEMBL1824', 'CHEMBL1844',
'CHEMBL1862', 'CHEMBL1868', 'CHEMBL1871', 'CHEMBL1914', 'CHEMBL1957', 'CHEMBL1974', 'CHEMBL1981', 'CHEMBL2034', 'CHEMBL2208', 'CHEMBL2276',
'CHEMBL2334', 'CHEMBL2954', 'CHEMBL2971', 'CHEMBL3227', 'CHEMBL3371', 'CHEMBL3397', 'CHEMBL3571', 'CHEMBL3650', 'CHEMBL3706', 'CHEMBL3717',
'CHEMBL3837', 'CHEMBL3952', 'CHEMBL4005', 'CHEMBL4124', 'CHEMBL4235', 'CHEMBL4282', 'CHEMBL4296', 'CHEMBL4354', 'CHEMBL4630', 'CHEMBL4722',
'CHEMBL4794', 'CHEMBL4805', 'CHEMBL4822', 'CHEMBL1293228', 'CHEMBL1741171', 'CHEMBL1907607', 'CHEMBL1907608', 'CHEMBL1907610', 'CHEMBL2093869', 'CHEMBL2094108']

#Defining the RF base model with default settings 
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
