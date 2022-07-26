%run 1_perform_base_case.py

#Base Models 
BaseModel_203_RSquared = model_203.score(x_203_test, y_203_test)
BaseModel_204_RSquared = model_204.score(x_204_test, y_204_test)
BaseModel_205_RSquared = model_205.score(x_205_test, y_205_test)
BaseModel_228_RSquared = model_228.score(x_228_test, y_228_test)
BaseModel_233_RSquared = model_233.score(x_233_test, y_233_test)
BaseModel_251_RSquared = model_251.score(x_251_test, y_251_test)
BaseModel_253_RSquared = model_253.score(x_253_test, y_253_test)
BaseModel_260_RSquared = model_260.score(x_260_test, y_260_test)
BaseModel_267_RSquared = model_267.score(x_267_test, y_267_test)
BaseModel_339_RSquared = model_339.score(x_339_test, y_339_test)

# naming the y-axis components
A = [BaseModel_203_RSquared,BaseModel_204_RSquared,BaseModel_205_RSquared,BaseModel_228_RSquared,
     BaseModel_233_RSquared,BaseModel_251_RSquared,BaseModel_253_RSquared,BaseModel_260_RSquared,
     BaseModel_267_RSquared,BaseModel_339_RSquared]
y = A 
# # naming the y-axis components
B = ["203", "204", "205", "228", "233", 
     "251", "253", "260", "267", "339"]
x= B

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5)

# setting y axis range
plt.ylim(0,1)

# naming the x axis
plt.xlabel('Dataset_CHEMBLxxx')

# naming the y axis
plt.ylabel('R2 Values')

# giving a title to my graph
plt.title('Base Model Performance')

# function to show the plot
plt.show()
