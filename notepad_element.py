from tkinter import *
root=Tk()
root.config(bg="yellow")
def get_text_data():
    result=text.get(1.0,END)
    print(result)

def get_select_text_data():
    result=text.selection_get()
    print(result)

def clear_text():
    text.delete(1.0,END)

def position():
    res=text.selection_get()
    pos=text.search(res,1.0,stopindex=END)
    print(pos)

text=Text(root,height=10,width=50,wrap=WORD,padx=10,pady=10,
          selectbackground='red')
text.pack()
text.insert(INSERT,"Hi Welocome You All")

btn=Button(root,text="print data",command=get_text_data)
btn.pack()

btn2=Button(root,text="print selected data",command=get_select_text_data)
btn2.pack()

btn3=Button(root,text="clear text",command=clear_text)
btn3.pack()

btn4=Button(root,text="select element position",command=position)
btn4.pack()
root.geometry("400x400+150+150")
root.mainloop()