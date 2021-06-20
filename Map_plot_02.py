import matplotlib.pyplot as plt
days=[1,2,3,4,5,6]
max_temp=[43,75,35,54,45,56]
min_temp=[23,43,15,43,12,45]
plt.plot(days,max_temp, color='red' ,linewidth=2,label="max")
plt.plot(days,min_temp,color='blue',linewidth=1,label="min" )
plt.xlabel("Day")
plt.ylabel("Temprature")
plt.title("Weather Info")
plt.legend (loc="best",shadow="true",fontsize="large")
plt.grid()
plt.show()