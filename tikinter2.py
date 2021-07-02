from tkinter import *
root=Tk()
root.title("My_Tkinter")
def msg1():
    print("Prabhakar Singh")

label=Label(root,text="Enter Your Name",font=("Ariel",25,'bold'),bg="red",fg="white")
label.pack(side=TOP)

txt=Entry(root,font=("Comic Sans Ms",20,'bold'))
txt.pack()

btn=Button(root,text="Click Me",fg="white",bg="blue",
           font=("Ariel",15,'bold'),command=msg1)
btn.pack()

#root.resizable(0,0)
root.geometry("400x400+500+90")
root.mainloop()