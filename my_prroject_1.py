from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import pymysql
#import pymysql

singh=Tk()
singh.title("Hotel Management System")


width=singh.winfo_screenwidth()
#print(width)
height=singh.winfo_screenheight()
#print(height)
#############Database connectivity#######################
singhTv=ttk.Treeview(height=10,column=('Item Name','Rate','Type'))

############for char input
def only_char_input(P):
    if P.isalpha() or P=='':
        return True
    return False
callback=singh.register(only_char_input)

#######################
def only_numeric_input(P):
    if P.isdigit() or P=='':
        return True
    return False
callback2=singh.register(only_numeric_input)

def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="my_collage")
    mycursor=conn.cursor()

####################clear_screen##########################
def clear_screen():
    global singh
    for widgets in singh.winfo_children():
        widgets.grid_remove()
##########log_out###################
def logout():
    clear_screen()
    mainheading()
    loginwindow()
def mainheading():
    label=Label(singh,text="Hotel Singh Management System",fg="white",bg="Red",font=("comic sans ms",33,"bold",),padx=400,pady=10)
    label.grid(row=0,columnspan=5)
mainheading()

usernameVar=StringVar()
passwordVar=StringVar()

def loginwindow():

    usernameVar.set("")
    passwordVar.set("")
    labellogin=Label(singh,text="Admin Log In",font=("ariel",35,"bold","underline"))
    labellogin.grid(row=1,column=1,columnspan=2,padx=50,pady=50)

    usernamelabel=Label(singh,text="User Name",font=("ariel",25,"bold"))
    usernamelabel.grid(row=2,column=1,padx=25,pady=5)

    passwordlabel=Label(singh,text="User Password",font=("ariel",25,"bold"))
    passwordlabel.grid(row=3,column=1,padx=20,pady=5)

    usernameEntry=Entry(singh,textvariable=usernameVar,font=("ariel",25))
    usernameEntry.grid(row=2,column=2,padx=50,pady=20)

    passwordEntry = Entry(singh,show="*", textvariable=passwordVar, font=("ariel", 25))
    passwordEntry.grid(row=3, column=2, padx=50, pady=20)


    loginButton=Button(singh,text="Login",width=25,height=2,bd=4,fg="white",bg="green",command=adminlogin)
    loginButton.grid(row=4, column=1, padx=5, pady=80,columnspan=2)

def welcomewindow():
    clear_screen()
    mainheading()
    welcome = Label(singh, text="Welcome Admin", font=("ariel", 35, "bold", "underline"))
    welcome.grid(row=1, column=1, columnspan=2, padx=50, pady=50)

    logoutButton = Button(singh, text="Logout", width=20, height=2, bd=5, fg="white", bg="green", command=logout)
    logoutButton.grid(row=4, column=1, padx=5, pady=80, columnspan=2)

    manageRes = Button(singh, text="Manage Hotel", width=20, height=2, bd=5, fg="white", bg="green", command=addItemWindow)
    manageRes.grid(row=5, column=0, padx=5, pady=80, columnspan=2)

    billGen = Button(singh, text="Bill Genration", width=20, height=2, bd=5, fg="white", bg="green",command=billWindow)
    billGen.grid(row=5, column=2, padx=5, pady=80, columnspan=2)

########back Button##############
def back():
    clear_screen()
    mainheading()
    welcomewindow()


def additemprocess():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    query="insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)"
    val=(name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Save Item","Item Saved Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()


#####################################
def getItemInTreeview():
    # to delete already inserted data
    records=singhTv.get_children()
    for x in records:
        singhTv.delete(x)

    conn=pymysql.connect(host="localhost",user="root",db="my_collage")
    mycursor=conn.cursor(pymysql.cursors.DictCursor)
    query1="select * from itemlist"
    mycursor.execute(query1)
    data=mycursor.fetchall()
    #print(data)
    for row in data:
        singhTv.insert('','end',text=row['item_name'],values=(row["item_rate"],row['item_type']))
    conn.close()
    singhTv.bind("<double-1>",onDoubleClick)


###############Double click
def onDoubleClick(event):
    item=singhTv.selection()
    itemNameVar1=singhTv.item(item,"text")
    item_detail = singhTv.item(item, "values")
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])
########################################
def updateitem():
    name=itemnameVar.get()
    rate=  itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que="update itemlist set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(que,val)
    conn.commit()
    messagebox.showinfo("Updation Confirmation","Item Updated Sucessfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()
 #####################Delete Item####################

def deleteitem():
    name=itemnameVar.get()
    rate=  itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que1="delete from itemlist where item_name=%s"
    val=(name)
    mycursor.execute(que1,val)
    conn.commit()
    messagebox.showinfo("Delete Confirmation","Item Deleted Sucessfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()
###########bill Window#########################
global x
x=datetime.now()
datetimeVar=StringVar()
datetimeVar.set(x)
customerNameVar=StringVar()
mobileVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
cost=StringVar()
qtyvariable=StringVar()
###################### combo data ##############################
def combo_input():
    dbconfig()
    mycursor.execute('select item_name from itemlist')
    data=[]
    for row in mycursor.fetchall():
        data.append(row[0])
    return data
######## option call back ###################
def optiCallBack(*args):
    global itemname
    itemname=combovariable.get()
    #print(itemname)
    aa=ratelist()
    print(aa)
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j
################ option call back2 ##############################
def optiCallBack2(*args):
    global qty
    qty=qtyvariable.get()
    final=int(v)*int(qty)
    cost.set(final)
######################## Rate List
def ratelist():
    dbconfig()
    que2="select item_rate from itemlist where item_name=%s"
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    print(data)
    return data

def billWindow():
    clear_screen()
    mainheading()
    billitem=Label(singh, text="Gentrate Bill", font=("ariel", 35, "bold","underline"))
    billitem.grid(row=1, column=1, columnspan=2, padx=5, pady=20)

    logoutButton = Button(singh, text="Logout", width=20, height=2, bd=5, fg="white", bg="green", command=logout)
    logoutButton.grid(row=3, columnspan=1)

    backButton = Button(singh, text="Back", width=20, height=2, bd=5, fg="white", bg="green", command=back)
    backButton.grid(row=4, columnspan=1)

    dateTimeLabel=Label(singh,text="Date and Time",font=("ariel",20,"bold"))
    dateTimeLabel.grid(row=2,column=1,padx=20,pady=5)

    dateTimeEntry=Entry(singh,textvariable=datetimeVar,font=("ariel",20,"bold"))
    dateTimeEntry.grid(row=2,column=2,padx=20,pady=5)

    customerNameLabel = Label(singh, text="Customer Name", font=("ariel", 20, "bold"))
    customerNameLabel.grid(row=3, column=1, padx=20, pady=5)

    customerNameEntry = Entry(singh, textvariable=customerNameVar, font=("ariel", 20, "bold"))
    customerNameEntry.grid(row=3, column=2, padx=20, pady=5)

    customerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    mobileLabel = Label(singh, text="Customer Mobile", font=("ariel", 20, "bold"))
    mobileLabel.grid(row=4, column=1, padx=20, pady=5)

    mobileEntry = Entry(singh, textvariable=mobileVar, font=("ariel", 20, "bold"))
    mobileEntry.grid(row=4, column=2, padx=20, pady=5)

    mobileEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    selectLabel = Label(singh, text="Select Item", font=("ariel", 20, "bold"))
    selectLabel.grid(row=5, column=1, padx=20, pady=5)

    l=combo_input()
    c=ttk.Combobox(singh,values=l,textvariable=combovariable,font=("ariel", 20, "bold"))
    c.set("Select Item")
    combovariable.trace('w',optiCallBack)
    c.grid(row=5,column=2,padx=20,pady=5)

    rateLabel = Label(singh, text="Item Rate", font=("ariel", 20, "bold"))
    rateLabel.grid(row=6, column=1, padx=20, pady=5)

    rateEntry = Entry(singh, textvariable=baserate, font=("ariel", 20, "bold"))
    rateEntry.grid(row=6, column=2, padx=20, pady=5)

    qtyLabel = Label(singh, text="Select Quantity", font=("ariel", 20, "bold"))
    qtyLabel.grid(row=7, column=1, padx=20, pady=5)

    global qtyvariable
    l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    qty = ttk.Combobox(singh, values=l2, textvariable=qtyvariable, font=("ariel", 20, "bold"))
    qty.set("Select Quantity")
    qtyvariable.trace('w', optiCallBack2)
    qty.grid(row=7, column=2, padx=20, pady=5)

    costLabel = Label(singh, text="Cost", font=("ariel", 20, "bold"))
    costLabel.grid(row=8, column=1, padx=20, pady=5)

    costEntry = Entry(singh, textvariable=cost, font=("ariel", 20, "bold"))
    costEntry.grid(row=8, column=2, padx=20, pady=5)

#####################################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemtypeVar=StringVar()
####################################
def addItemWindow():
    clear_screen()
    mainheading()
    additem = Label(singh, text="Insert Item", font=("ariel", 35, "bold", "underline"))
    additem.grid(row=1, column=1, columnspan=2, padx=5, pady=20)

    itemnameLabel=Label(singh,text="Item Name",font=("ariel", 25, "bold"))
    itemnameLabel.grid(row=2,column=1,padx=20,pady=5)

    itemrateLabel = Label(singh, text="Item Rate (INR)", font=("ariel", 25, "bold"))
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemtypeLabel = Label(singh, text="Item Type", font=("ariel", 25, "bold"))
    itemtypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry=Entry(singh,textvariable=itemnameVar)
    itemnameEntry.grid(row=2,column=2,padx=20,pady=5)

### for validation
    itemnameEntry.configure(validate="key",validatecommand=(callback,"%P"))

    itemrateEntry = Entry(singh, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)

    itemrateEntry.configure(validate="key", validatecommand=(callback2, "%P"))


    itemtypeEntry = Entry(singh, textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4, column=2, padx=20, pady=5)

    itemtypeEntry.configure(validate="key", validatecommand=(callback, "%P"))


    additemButton=Button(singh,text="Add Item",width=20,height=2,bd=4,fg="white",bg="green",command=additemprocess)
    additemButton.grid(row=3, column=3,columnspan=1)

    updateButton = Button(singh, text="Update", width=20, height=2, bd=4, fg="white", bg="green",command=updateitem)
    updateButton.grid(row=4, column=3, columnspan=1)

    deleteButton = Button(singh, text="Delete", width=20, height=2, bd=4, fg="white", bg="green", command=deleteitem)
    deleteButton.grid(row=4, column=3, columnspan=1)

    logoutButton = Button(singh, text="Logout", width=20, height=2, bd=5, fg="white", bg="green", command=logout)
    logoutButton.grid(row=3, columnspan=1)

    backButton = Button(singh, text="Back", width=20, height=2, bd=5, fg="white", bg="green", command=back)
    backButton.grid(row=4, columnspan=1)

    ########Treeview###########
    singhTv.grid(row=8,column=0,columnspan=3)
    # style=ttk.style(singh)
    # style.theme_use('calm')
    # style.configure("Treeview",fieldbackground="green")
    scrollBar=Scrollbar(singh,orient="vertical",command=singhTv.yview)
    scrollBar.grid(row=8,column=2,sticky="NSE")

    singhTv.configure(yscrollcommand=scrollBar.set)
    singhTv.heading('#0',text="Item Name")
    singhTv.heading('#1',text="Rate")
    singhTv.heading('#2',text="Type")

    getItemInTreeview()

def adminlogin():
    dbconfig()
    username=usernameVar.get()
    password=passwordVar.get()
    que="select * from user_info where user_id=%s and user_pass=%s"
    val=(username,password)
    mycursor.execute(que,val)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True

    conn.close()
    if flag==True:
        welcomewindow()
    else:
        messagebox.showerror("Invalid User Credential","Incorrect User Name Or Password ")
        usernameVar.set("")
        passwordVar.set("")

mainheading()
loginwindow()


singh.geometry("%dx%d+0+0"%(width,height))
singh.mainloop()