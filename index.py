from imports import *
def main_scr(user_name):
    top = Tk()
    top.title("Inventory Management")

    def callViewAllItems():
        try:
            top.destroy()
            import viewAllItems
            viewAllItems.viewAllItems(user_name)
        except:
            print("Cannot destroy")
    def callAddNewItem():
        try:
            top.destroy()
            import addNewItem
            addNewItem.addNewItem(user_name)
        except:
            print("cannot destroy")
    def callViewSoldRecords():
        try:
            top.destroy()
            import viewSoldRecords
            viewSoldRecords.viewAllItems(user_name)
        except:
            print("Cannot destroy")
    def callSellItem():
        try:
            top.destroy()
            import sellItem
            sellItem.sellItem(user_name)
            print("Records selling called")
        except:
            print("Cannot destroy")
    def  callLogOut():
        try:
            top.destroy()
            import adminLogin
            adminLogin.adminLogin()
        except:
            print("Cannot Log out")
    #top.geometry('700x700')
    photo = PhotoImage(file = 'ires/inventory.PNG')
    photo = photo.subsample(1)
    lbl = Label(top,image = photo)
    lbl.image = photo
    lbl.grid(row=0,column=0, columnspan=12,rowspan=10)

    #new label begins here

    #L4 name akash
    L4 = Label(top,text="Akash Andotra",font = ( "bold" , 14 , ), fg="blue")
    L4.grid(row=1,column=0)
    #L5 name gaurav
    L5 = Label(top,text="Gaurav Yadav",font = ( "bold" , 14 , ), fg="blue")
    L5.grid(row=2,column=0)

    #L1
    L1 = Label(top,text="Inventory Management",font = ( "bold" , 32 , ), fg="blue")
    L1.grid(row=11,column=0, columnspan=12,rowspan=2)

    #L2
    L2 = Label(top,text="Choose from the options below",font = ( "bold" , 15 , ), fg="green")
    L2.grid(row=13,column=0, columnspan=12,rowspan=2)
    #L3 empty
    L3 = Label(top,text="")
    L3.grid(row=15,column=0, columnspan=12,rowspan=2)
    #B1
    B1 = Button(top, text = 'View All Items',command=callViewAllItems, fg="white", bg="green")
    B1.grid(row=17,column=0,padx=3,pady=3,columnspan=2)
    #B2
    B2 = Button(top, text = 'Add new Product',command=callAddNewItem,  fg="white", bg="green")
    B2.grid(row=17,column=3,padx=3,pady=3,columnspan=2)
    #B3
    B3 = Button(top, text = 'Sell Item',command=callSellItem,  fg="white", bg="green")
    B3.grid(row=17,column=6,padx=3,pady=3,columnspan=2)
    #B4
    B4 = Button(top, text = 'View Sold Records',command=callViewSoldRecords,  fg="white", bg="green")
    B4.grid(row=17,column=9,padx=3,pady=3,columnspan=2)
    #B5
    B5 = Button(top, text = 'Log Out',command=callLogOut,  fg="white", bg="green")
    B5.grid(row=17,column=12,padx=3,pady=3,columnspan=2)
    #L5 empty

    L5 = Label(top,text="")
    L5.grid(row=18,column=0, columnspan=12,rowspan=2)
    #top mainloop
    top.resizable(0,0)
    top.mainloop()


    

