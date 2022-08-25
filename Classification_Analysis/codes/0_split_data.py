import pandas as pd
from sklearn.model_selection import train_test_split


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

def split_and_save_dataset(dataset, perc = 0.3):
    
    df = pd.read_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_raw\\{dataset}.csv', index_col=0, header=0)
    
    median_val = df['pXC50'].median()
    
    df.loc[df['pXC50'] <= median_val, 'pXC50'] = 0
    df.loc[df['pXC50'] > median_val, 'pXC50'] = 1
 
    
    train, test = train_test_split(df, test_size = perc)
    train.to_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_train.csv')
    test.to_csv(f'C:\\Users\\AMahmud\\Classification_Analysis\\input\\base_processed\\{dataset}_test.csv')

def main():
   
    for dataset in datasets:
        split_and_save_dataset(dataset)

if __name__ == '__main__':
    main()
