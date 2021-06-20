import matplotlib.pyplot as plt
import numpy as np
company=['Reliance','Tata','Amazon','Flipkart','Microsoft','Other']
revenue=[2500,1400,2600,1200,3200,300]
profit=[1200,500,700,480,1100,110]
xpos=np.arange(len(company))
print(xpos)

plt.bar(xpos-0.2,revenue,label="revenue",color="orange",width=0.4)
plt.bar(xpos+0.2,profit,label="profit", color="red",width=0.4)
plt.xticks(xpos,company)
plt.xlabel("company")
plt.ylabel("revenue in million")
plt.title("Profit and loss")
plt.grid()
plt.legend()
plt.show()