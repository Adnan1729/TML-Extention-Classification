# importing all necessary libraries and dataframes
from google.colab import drive 
import pandas as pd

#Importing the largest 10 csv files form google drive: 203, 204, 205, 228, 233, 251, 253, 260, 267, 339. 
drive.mount('/content/drive')
data_203 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL203.csv')
data_204 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL204.csv')
data_205 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL205.csv')
data_228 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL228.csv')
data_233 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL233.csv')
data_251 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL251.csv')
data_253 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL253.csv')
data_260 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL260.csv')
data_267 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL267.csv')
data_339 = pd.read_csv ('/content/drive/MyDrive/Ross King Research Work/QSAR Raw Data Summer 2022/CHEMBL339.csv')
