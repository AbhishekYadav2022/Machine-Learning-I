from matplotlib import pyplot as plt
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [45567, 50384, 55483, 70736, 75756, 85736, 85555, 90495, 95584, 100473, 110643]
py_dev_y = [55567, 55384, 65483, 75736, 85756, 87736, 95555, 100495, 105584, 106473, 114643]
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.plot(ages_x, dev_y, 'k--', label='All Devs')
plt.plot(ages_x, py_dev_y, 'b', label='Python')
plt.legend()
plt.show()