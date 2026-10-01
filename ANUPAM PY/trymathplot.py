
import matplotlib.pyplot as plt
s = ["Hari Ram","Tika Ram ","Asshh","Topi lal"]
m = [60,70,80,90]

plt.plot(s,m , marker= "o",color = "blue")
plt.title("Monthly Rainfall Comparison of 2 cities")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid(True)

plt.xlim(11,100)
plt.ylim(11,100)
plt.show()