import pandas as pd

Datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL206', 'CHEMBL208', 'CHEMBL210', 'CHEMBL211', 'CHEMBL214', 'CHEMBL219', 'CHEMBL220',
'CHEMBL221', 'CHEMBL222', 'CHEMBL224', 'CHEMBL225', 'CHEMBL226', 'CHEMBL228', 'CHEMBL230', 'CHEMBL233', 'CHEMBL234', 'CHEMBL247',
'CHEMBL248', 'CHEMBL249', 'CHEMBL251', 'CHEMBL253', 'CHEMBL255', 'CHEMBL256', 'CHEMBL258', 'CHEMBL259', 'CHEMBL260', 'CHEMBL261',
'CHEMBL262', 'CHEMBL264', 'CHEMBL267', 'CHEMBL268', 'CHEMBL269', 'CHEMBL270', 'CHEMBL283', 'CHEMBL284', 'CHEMBL286', 'CHEMBL287',
'CHEMBL289', 'CHEMBL298', 'CHEMBL301', 'CHEMBL302', 'CHEMBL308', 'CHEMBL313', 'CHEMBL318', 'CHEMBL321', 'CHEMBL322', 'CHEMBL325',
'CHEMBL332', 'CHEMBL333', 'CHEMBL335', 'CHEMBL338', 'CHEMBL339', 'CHEMBL340', 'CHEMBL344', 'CHEMBL1800', 'CHEMBL1824', 'CHEMBL1844',
'CHEMBL1862', 'CHEMBL1868', 'CHEMBL1871', 'CHEMBL1914', 'CHEMBL1957', 'CHEMBL1974', 'CHEMBL1981', 'CHEMBL2034', 'CHEMBL2208', 'CHEMBL2276',
'CHEMBL2334', 'CHEMBL2954', 'CHEMBL2971', 'CHEMBL3227', 'CHEMBL3371', 'CHEMBL3397', 'CHEMBL3571', 'CHEMBL3650', 'CHEMBL3706', 'CHEMBL3717',
'CHEMBL3837', 'CHEMBL3952', 'CHEMBL4005', 'CHEMBL4124', 'CHEMBL4235', 'CHEMBL4282', 'CHEMBL4296', 'CHEMBL4354', 'CHEMBL4630', 'CHEMBL4722',
'CHEMBL4794', 'CHEMBL4805', 'CHEMBL4822', 'CHEMBL1293228', 'CHEMBL1741171', 'CHEMBL1907607', 'CHEMBL1907608', 'CHEMBL1907610', 'CHEMBL2093869', 'CHEMBL2094108']D

def run_check(dataset): 
    df_train = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_train.csv')

    x_train = df_train.drop(columns = ['molecule_id','pXC50'])
    y_train = (df_train.pXC50)
    
    count = y_train.value_counts(normalize = True).reset_index()
    one = '{:.2f}'.format(round(((count.at[0,"pXC50"])*100),2)) # How did I know one is at index 0? I manually checked few iterations, always the 1 is stored in index 0.
    zero = '{:.2f}'.format(round(((count.at[1,"pXC50"])*100),2))
    
    def crt_txt(dataset,one,zero):
        txt_file = open('C:\\Users\\AMahmud\\Classification_Analysis\\output\\results\\90th_Percentile_Imbalance.txt', "a")
        txt_file.write(f'{dataset}: 0 at {zero}% and 1 at {one}%\n')
        txt_file.close()
    crt_txt(dataset,one,zero)
    
def check_balance():
    for dataset in datasets:
        run_check(dataset)
        
check_balance()
