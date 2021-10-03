from tkinter import *
import pymysql
from tkinter import messagebox,filedialog
from tkinter import ttk
from datetime import datetime
taz=Tk()
width=taz.winfo_screenwidth()
# print(width)
heigth=taz.winfo_screenwidth()
# print(heigth)
tazTV=ttk.Treeview(columns=('Item Name'"Rate","type"))
tazTV1=ttk.Treeview(columns=('Date''Name','Type','Rate','Total'))
###########clear screen#############

def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()

 ############## char input###########

def only_char_input(P):
    if P.isalpha() or P=='':
        return True
    return False

callback=taz.register(only_char_input)

 ############## digit input###########

def only_numeric_input(P):
    if P.isdigit() or P=='':
        return True
    return False

callback2=taz.register(only_numeric_input)

############## logout ###########
def logout():
    clear_screen()
    mainheading()
    loginwindow()


##############database connection########
def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="myhotel")
    mycursor=conn.cursor()

label=Label(taz,text="Hotel Management System",fg="red",bg="yellow",font=("comic sans Ms",30,"bold"),padx=420,pady=10)
label.grid(row=0,columnspan=4)

def mainheading():
    label = Label(taz, text="Hotel Management System", fg="red", bg="yellow", font=("comic sans Ms", 30, "bold"),
                  padx=420, pady=10)
    label.grid(row=0, columnspan=4)

usernameVar=StringVar()
passwordVar=StringVar()


def loginwindow():
    usernameVar.set("")
    passwordVar.set("")

    labellogin = Label(taz, text="Admin Log in",font=("ariel", 25, "bold"))
    labellogin.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    usernameLabel=Label(taz,text="User Name",font=("ariel", 12, "bold"))
    usernameLabel.grid(row=2,column=1,padx=20,pady=5)

    passwordLabel = Label(taz, text="User Password",font=("ariel", 12, "bold"))
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordEntry = Entry(taz, textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton=Button(taz,text="Login",font=("ariel", 10, "bold"),width=20,fg="green",bd=10,command=adminLogin)
    loginButton.grid(row=4,column=1,columnspan=2,padx=20,pady=5)
##########  back button#############

def back():
    clear_screen()
    mainheading()
    welcomewindow()

    ########################
def getItemInTreeview():
   ## $to delete already inserted data
   records=tazTV.get_children()
   for x in records:
       tazTV.delete(x)
   conn=pymysql.connect(host="localhost",user="root",db="myhotel")
   mycursor=conn.cursor(pymysql.cursors.DictCursor)
   query1="select * from item_list"
   mycursor.execute(query1)
   data=mycursor.fetchall()
   # print(data)
   for row in data:

           tazTV.insert('','end',text=row['item_name'],values=(row["item_rate"],row['item_type']))
   conn.close()
   tazTV.bind("<Double-1>",OnDoubleClick)

   ################ double click############
def OnDoubleClick(event):
    item=tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemtypeVar.set(item_detail[1])

    ############### update item##############
def updateItem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que="update item_list set item_rate=%s,item_type=%s where item_name=%s"
    val=(rate,type,name)
    mycursor.execute(que,val)
    conn.commit()
    messagebox.showinfo("updation Confirmation","Item Updated successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")

    getItemInTreeview()

################# delete item ##########
   ############### update item##############
def deleteItem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    que1="delete from item_list where item_name=%s"
    val3=(name)
    mycursor.execute(que1,val3)
    conn.commit()
    messagebox.showinfo("Delete Confirmation","Item Deleted successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()

    ############## bill window #########
global x
x=datetime.now()
datetimeVar=StringVar()
datetimeVar.set(x)
costomerNameVar=StringVar()
mobileVar=StringVar()
combovariable=StringVar()
baserate=StringVar()
cost=StringVar()
qtyvariable=StringVar()

#############combo data #############
def combo_input():
    dbconfig()
    mycursor.execute("select item_name from item_list")
    data=[]
    for row in mycursor.fetchall():
        data.append(row[0])
    return data
############## optionOnCallBack#######
def optionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    # print(itenname)
    aa=rateList()
    print(aa)
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v=j

##################### optionCallBack2  ###
def optionCallBack2(*args):
    global qty
    qty=qtyvariable.get()
    total=int (v) * int (qty)
    cost.set(total)

    ############ rateList#######
def rateList():
    dbconfig()
    que2="select item_rate from item_list where item_name=%s"
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    print(data)
    return data

def billWindow():
     clear_screen()
     mainheading()
     billItem = Label(taz, text="Generate Bill", font=("ariel", 25, "bold"))
     billItem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

     logoutButton = Button(taz, text="Logout", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=logout)
     logoutButton.grid(row=2, column=0, columnspan=1, )

     backButton = Button(taz, text="Back", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=back)
     backButton.grid(row=3, column=0, columnspan=1, )

     printButton = Button(taz, text="Print Bill", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=printbill)
     printButton.grid(row=5, column=0, columnspan=1, )

     dateTimeLabel=Label(taz,text="Date & Time",font=("ariel", 15, "bold"))
     dateTimeLabel.grid(row=2,column=1,padx=20,pady=5)

     dateTimeEntry=Entry(taz,textvariable=datetimeVar,font=("ariel", 15, "bold"))
     dateTimeEntry.grid(row=2,column=2,padx=20,pady=5)

     costomerNameLabel = Label(taz, text="Costomer Name", font=("ariel", 15, "bold"))
     costomerNameLabel.grid(row=3, column=1, padx=20, pady=5)

     costomerNameEntry = Entry(taz, textvariable=costomerNameVar, font=("ariel", 15, "bold"))
     costomerNameEntry.grid(row=3, column=2, padx=20, pady=5)
     # for validation
     costomerNameEntry.configure(validate="key", validatecommand=(callback, "%P"))

     mobileLabel = Label(taz, text="Contact no", font=("ariel", 15, "bold"))
     mobileLabel.grid(row=4, column=1, padx=20, pady=5)

     mobileEntry = Entry(taz, textvariable=mobileVar, font=("ariel", 15, "bold"))
     mobileEntry.grid(row=4, column=2, padx=20, pady=5)
     # for validation
     mobileEntry.configure(validate="key", validatecommand=(callback2, "%P"))

     selectLabel = Label(taz, text="Select Item", font=("ariel", 15, "bold"))
     selectLabel.grid(row=5, column=1, padx=20, pady=5)

     l=combo_input()
     c=ttk.Combobox(taz,values=l,textvariable=combovariable, font=("ariel", 15, "bold"))
     c.set("select Item")
     combovariable.trace('w',optionCallBack)
     c.grid(row=5,column=2,padx=20,pady=5)

     rateLabel = Label(taz, text="Item Rate", font=("ariel", 15, "bold"))
     rateLabel.grid(row=6, column=1, padx=20, pady=5)

     rateEntry = Entry(taz, textvariable=baserate, font=("ariel", 15, "bold"))
     rateEntry.grid(row=6, column=2, padx=20, pady=5)

     qtyLabel = Label(taz, text="Select Quantity", font=("ariel", 15, "bold"))
     qtyLabel.grid(row=7, column=1, padx=20, pady=5)

     global qtyvariable
     l2 = [1,2,3,4,5]
     qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable, font=("ariel", 15, "bold"))
     qty.set("select Quantity")
     qtyvariable.trace('w',optionCallBack2)
     qty.grid(row=7, column=2, padx=20, pady=5)

     costlabel = Label(taz, text="Cost", font=("ariel", 15, "bold"))
     costlabel.grid(row=8, column=1, padx=20, pady=5)

     costEntry = Entry(taz, textvariable=cost, font=("ariel", 15, "bold"))
     costEntry.grid(row=8, column=2, padx=20, pady=5)

     billButton=Button(taz,text="Save Bill",width=20,bd=10,fg="red",bg="yellow",command=saveBill)
     billButton.grid(row=9,column=2,padx=20,pady=5)

     ##################### save bill ######

def saveBill():
    dt=datetimeVar.get()
    costname=costomerNameVar.get()
    mobile = mobileVar.get()
    item_name=itemname
    itemrate=v
    itemqty=qtyvariable.get()
    total=cost.get()
    print(dt,costname)
    dbconfig()
    insqu="insert into bill_info(datetime,costomer_name,contact_no,item_name,item_rate,item_qty,cost)" \
    "values(%s,%s,%s,%s,%s,%s,%s)"
    val2=(dt,costname,item_name,mobile,itemrate,itemqty,total)
    mycursor.execute(insqu,val2)
    conn.commit()
    messagebox.showinfo("Save Data","Saved Bill Successfully")
    costomerNameVar.set("")
    mobileVar.set("")
    itemnameVar.set("")
    cost.set("")

    ############ print bill ###########
def printbill():
    clear_screen()
    mainheading()
    printlabel = Label(taz, text="Bill Details", font=("ariel", 15, "bold"))
    printlabel.grid(row=1,columnspan=2, column=1, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1,)

    backButton = Button(taz, text="Back", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=back)
    backButton.grid(row=3, column=3, columnspan=1, )

    clickbutton = Button(taz, text="Double Click to Treeview to Print Bill", font=("ariel", 15, "bold"))
    clickbutton.grid(row=2, columnspan=2, column=1, padx=50, pady=10)

    #####tree view######
    tazTV1.grid(row=5, column=0, columnspan=4)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview", fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=5, column=5, sticky="NSE")
    tazTV1.configure(yscrollcommand=scrollBar.set)
    tazTV1.heading("#0", text="Date/Time")
    tazTV1.heading("#1", text="Name")
    tazTV1.heading("#2", text="Mobile")
    tazTV1.heading("#3", text="Selected Food")
    tazTV1.heading("#4", text="Total Cost")
    displaybill()

    #################################
##################  display bill ############
def  displaybill():
    ## $to delete already inserted data
    records = tazTV1.get_children()
    for x in records:
        tazTV1.delete(x)
    conn = pymysql.connect(host="localhost", user="root", db="myhotel")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query1 = "select * from bill_info"
    mycursor.execute(query1)
    data = mycursor.fetchall()
    # print(data)
    for row in data:
        tazTV1.insert('', 'end', text=row['datetime'], values=(row["costomer_name"], row['contact_no'],row['item_name'],row['cost']))
    conn.close()
    tazTV1.bind("<Double-1>", OnDoubleClick2)

    ###########################  OnDoubleClick2#######################
def  OnDoubleClick2(event):
    item = tazTV1.selection()
    global itemnameVar11
    itemnameVar11 = tazTV1.item(item, "text")
    item_detail = tazTV1.item(item, "values")
    recpt()
    ##############recpt()###################
def recpt():
    billstring=""
    billstring+="=========== My Hotel Bill ===========\n\n"
    billstring += "=========== Customer Detail ===========\n\n"
    dbconfig()
    query3="select * from bill_info where datetime='{}';".format(itemnameVar11)
    mycursor.execute(query3)
    data=mycursor.fetchall()
    print(data)
    for row in data:
        billstring+="{}{:<20}{:<10}\n".format("Date/Time","",row[1])
        billstring += "{}{:<20}{:<10}\n".format("customer_name","",row[2])
        billstring += "{}{:<20}{:<10}\n".format("contact_no","",row[3])
        billstring+="\n================= Item Detail ============\n"
        billstring+="{:<10}{:<10}{:<15}{:<15}".format("Item Name","Rate","Quantity","Total Cost")
        billstring+="\n{:<10}{:<10}{:<25}{:<25}".format(row[4],row[5],row[6],row[7])
        billstring+="===================================================\n"
        billstring += "{}{:<10}{:<15}{:<10}\n".format("Total Cost"," "," ",row[7])
        billstring+="\n\n Thanks Please Visit Again =====================\n"

    bilfile=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if bilfile is None:
        messagebox.showerror("File Name Error","Invalid File Name")
    else:
        bilfile.write(billstring)
        bilfile.close()




#########################################################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemtypeVar=StringVar()

def addItemWindow():
    clear_screen()
    mainheading()
    addItem = Label(taz, text="Insert Item", font=("ariel", 25, "bold"))
    addItem.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    itemnameLabel= Label(taz, text="Item Name", font=("ariel", 20, "bold"))
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate", font=("ariel", 20, "bold"))
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemtypeLabel = Label(taz, text="Item Type", font=("ariel", 20, "bold"))
    itemtypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry=Entry(taz,textvariable=itemnameVar)
    itemnameEntry.grid(row=2,column=2,padx=20,pady=5)
    #for validation
    itemnameEntry.configure(validate="key",validatecommand=(callback,"%P"))

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    # for validation
    itemrateEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    itemtypeEntry = Entry(taz, textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4, column=2, padx=20, pady=5)


    addItemButton=Button(taz,text="Add Item",width=20,fg="green",bd=10,command=additem)
    addItemButton.grid(row=2,column=3,columnspan=1)

    updateItemButton = Button(taz, text="Update Item", width=20, fg="green", bd=10, command=updateItem)
    updateItemButton.grid(row=3, column=3, columnspan=1)

    deleteItemButton = Button(taz, text="Delete Item", width=20, fg="green", bd=10, command=deleteItem)
    deleteItemButton.grid(row=4, column=3, columnspan=1)

    logoutButton = Button(taz, text="Logout", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=logout)
    logoutButton.grid(row=2, column=0, columnspan=1,)

    backButton = Button(taz, text="Back", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=back)
    backButton.grid(row=3, column=0, columnspan=1, )
    #####tree view######
    tazTV.grid(row=6,column=0,columnspan=3)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",fieldbackground="green")
    scrollBar=Scrollbar(taz,orient="vertical",command=tazTV.yview())
    scrollBar.grid(row=8,column=2,sticky="NSE")
    tazTV.configure(yscrollcommand=scrollBar.set)
    tazTV.heading("#0",text="Item Name")
    tazTV.heading("#1", text="Item Rate")
    tazTV.heading("#2", text="Item Type")

    getItemInTreeview()

def additem():
    name=itemnameVar.get()
    rate=itemrateVar.get()
    type=itemtypeVar.get()
    dbconfig()
    query="insert into item_list(item_name,item_rate,item_type)values(%s,%s,%s)"
    val=(name,rate,type)
    mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("Save Item","item Saved Successfully")
    itemnameVar.set("")
    itemrateVar.set("")
    itemtypeVar.set("")
    getItemInTreeview()
def welcomewindow():
    clear_screen()
    mainheading()
    welcome = Label(taz, text="Welcome Admin", font=("ariel", 25, "bold"))
    welcome.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", font=("ariel", 10, "bold"), width=20, fg="green", bd=10, command=logout)
    logoutButton.grid(row=4, column=1, columnspan=2, padx=20, pady=5)

    manageRest = Button(taz, text="Manage Hotel", width=20, fg="green", bd=2, command=addItemWindow)
    manageRest.grid(row=5, column=1, columnspan=2, padx=20, pady=5)

    BillGen = Button(taz, text="Bill Generate", width=20, fg="green", bd=2, command=billWindow)
    BillGen.grid(row=6, column=1, columnspan=2, padx=20, pady=5)

def adminLogin():
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
        messagebox.showerror("Invalid User Credeltial","Either User Name or Password incorrect")
        usernameVar.set("")
        passwordVar.set("")

mainheading()
loginwindow()
taz.title("Hotel Management")
taz.geometry("%dx%d+0+0"%(width,heigth))
taz.mainloop()