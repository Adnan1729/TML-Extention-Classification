%run raw.py 

datasets = [CHEMBL203, CHEMBL204, CHEMBL205, CHEMBL228, CHEMBL233, CHEMBL251, CHEMBL253, CHEMBL260, CHEMBL267, CHEMBL339]
names = ['CHEMBL203', 'CHEMBL204', 'CHEMBL205', 'CHEMBL228', 'CHEMBL233', 'CHEMBL251', 'CHEMBL253', 'CHEMBL260', 'CHEMBL267', 'CHEMBL339']

for i,j in zip(datasets,names):
    x = i.drop(columns=['molecule_id','pXC50')
    y = i.pXC50
        
    # rus = RandomUnderSampler(sampling_strategy="not minority") # String
    rus = RandomUnderSampler(sampling_strategy=1, random_state=41) # Numerical value
    x_res, y_res = rus.fit_resample(x, y)
    
    #Remove low variance features
    #replace with x_res, y_res from now on
    remove_low_variance(x_res, threshold=0.1)
                        break
    
#fix_random_state=42
models = {}
for data, name in zip(data_sets, names):

    #Data splitting
    x_train, x_test, y_train, y_test = train_test_split(x_res, y_res, test_size=0.2, random_state=42)
    x_train.shape, x_test.shape
                        break
