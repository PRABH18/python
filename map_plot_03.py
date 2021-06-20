import matplotlib.pyplot as plt
user=['Prabhakar','Naveen','Ankit','Sapna','parm','Pratistha']
number=[445,754,523,985,645,812]
plt.axis("equal")
plt.pie(number,labels=user,radius=.4,explode=[0,0.04,0,0.07,0,0.06],autopct='%0.3f%%',startangle=154)
plt.legend (loc="best",shadow="true",fontsize="large")
plt.show()