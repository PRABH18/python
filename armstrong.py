from math import *
print("xyz")
a,b,c=(input("enter the no"))
#print("a=",a,"b=",b,"c=",c)
d=a+b+c
print("d=",d)
f=int(a)
g=int(b)
h=int(c)
print(f)
print(g)
print(h)
A=f**3
B=g**3
C=h**3
print("a qube=",A)
print("b qube=",B)
print("c qube=",C)
i=A+B+C
print(i)
j=int(d)
print(j)
if i==j:
    print("yes its armstrong no")
else:
    print("its not armstrong no")

    self.color_menu = Menu(self.main_menu, tearoff=False)
    self.main_menu.add_cascade(label="Color", menu=self.file_menu)
    self.color_menu.add_command(label="Background color", command=self.change_bgcolor)
    self.color_menu.add_command(label="Fore ground color", command=self.change_fgcolor)
