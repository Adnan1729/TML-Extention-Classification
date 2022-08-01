import pandas as pd
from sklearn.model_selection import train_test_split

def split_and_save_dataset(dataset, perc = 0.3):
    df = pd.read_csv(f'../input/raw/{dataset}.csv', index_col=0, header=0)
    train, test = train_test_split(df, test_size = perc)

    train.to_csv(f'../input/processed/{dataset}_train.csv')
    test.to_csv(f'../input/processed/{dataset}_test.csv')

def main():
    datasets = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205']
    for dataset in datasets:
        split_and_save_dataset(dataset)

if __name__ == '__main__':
    main()