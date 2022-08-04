import matplotlib.pyplot as plt

ds_name = ["203", "204", "205", "228", "233", 
     "251", "253", "260", "267", "339"]

plt.plot(ds_name, base_r2_results, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=5)

plt.axhline(y = max(base_r2_results), color = 'r', linestyle = '-', linewidth = 0.3)
plt.axhline(y = min(base_r2_results), color = 'r', linestyle = '-', linewidth = 0.3)

plt.ylim(0,1)
plt.xlabel('Dataset_CHEMBLxxx')
plt.ylabel('R2 Performance')
plt.title('Base Model Performance')
plt.show()
