import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[43,75,65,34,45,86]
plt.plot(x,y, color='red',linewidth=5,linestyle='dotted')
plt.xlabel("Day")
plt.ylabel("Temprature")
plt.title("Weather Info")
plt.show()