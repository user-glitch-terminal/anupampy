import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_city1 = [3.2, 3.8, 4.1, 2.9, 2.5, 1.8, 1.5, 1.7, 2.0, 2.4, 3.0, 3.5]
rainfall_city2 = [2.5, 3.0, 3.6, 2.7, 2.1, 1.6, 1.4, 1.9, 2.2, 2.8, 3.2, 3.6]
plt.plot(months, rainfall_city1, marker = "o", color = "blue", label = "City 1")
plt.plot(months, rainfall_city2, marker = "s", color = "red", label = "City 2")
plt.title("Monthly Rainfall Comparison of 2 cities")
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.legend()
plt.grid()
plt.show()
 