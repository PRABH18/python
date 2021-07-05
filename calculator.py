from tkinter import *

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnclear():
    global val
    val=""
    data.set("")

def btnequal():
    global val
    result=(eval(val))
    data.set(result)
root=Tk()
root.title("my_calculator")
root.geometry("330x310+500+200")
val=""
data=StringVar()
display=Entry(root,bd=8,textvariable=data,justify="right",bg="blue",font=("Ariel",20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btnsub=Button(root,text="-",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick('-'))
btnsub.grid(row=1,column=3)

btn4=Button(root,text="4",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btnadd=Button(root,text="+",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick('+'))
btnadd.grid(row=2,column=3)

btn1=Button(root,text="1",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btndiv=Button(root,text="/",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick('/'))
btndiv.grid(row=3,column=3)

btnc=Button(root,text="C",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=btnclear)
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick(0))
btn0.grid(row=4,column=1)
btnmul=Button(root,text="*",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=lambda:btnclick("*"))
btnmul.grid(row=4,column=2)




btnequ=Button(root,text="=",font=("Ariel",12,"bold"),height=2,width=6,bd=8,command=btnequal)
btnequ.grid(row=4,column=3)
root.mainloop()