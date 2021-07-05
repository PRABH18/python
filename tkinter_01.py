from tkinter import *
root=Tk()
canvas=Canvas(root,height=500,width=500,bg="red")
canvas.create_text(300,50,text="Canvas window layout",
                   font="Times 20 italic bold",fill="yellow")
canvas.create_line(0,0,500,500,fill="white",width=10)
canvas.create_rectangle(250,250,100,100,fill="yellow",outline="blue",width="10")
canvas.create_oval(250,250,100,100,fill="white",outline="blue",width="10")
# arc #polygon
canvas.pack()
root.geometry("600x600+150+150")
root.mainloop()