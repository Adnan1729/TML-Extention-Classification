%run 0_split_data.py
#fix_random_state=42
models = {}
for data, name in zip(data_sets, names):  
    #Model building
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(x_train, y_train)
    models[name] = model
