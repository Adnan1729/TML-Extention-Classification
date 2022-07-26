%run 1_perform_base_case.py

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
