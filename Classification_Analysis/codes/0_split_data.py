import pandas as pd
from sklearn.model_selection import train_test_split
import os


# The Path where all the 500 or 1000 or 1500 or 2000 datasets are stored. "/500" shall be chnaged to "/1000" or "/1500" or "/2000" for scaling up. 
dir_path = r'/content/drive/MyDrive/Classification_Analysis/input/base_raw/500'
all_file_names = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        all_file_names.append(path)


datasets = all_file_names

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
