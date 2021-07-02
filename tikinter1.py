from tkinter import *
root=Tk()

def msg():
    print("Good morning")

def msg2():
    print("Good Afternoon")
root.title("My First Window")
label=Label(root,text="Enter Your Name",bg="red",fg="yellow",
            font=("Comic Sans Ms",20,'bold'))
label.pack(side=TOP)

label1=Label(root,text="Enter Your Father Name",bg="red",fg="yellow",
            font=("Comic Sans Ms",20,'bold'))
label1.pack(side=BOTTOM)
#label1.pack(side=LEFT)
btn=Button(root,text="Click Me",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'),command=msg)
btn.pack()

btn1=Button(root,text="Msg ME",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'),command=msg2)
btn1.pack(fill=X)

txt=Entry(root,font=("Comic Sans Ms",20,'bold'))
txt.pack()

btn3=Button(root,text="Exit",fg="blue",bg="yellow",
           font=("Comic Sans Ms",20,'bold'),command=quit)
btn3.pack()
root.resizable(0,0)
root.geometry("400x400+300+150")
root.mainloop()