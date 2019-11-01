from imports import *
from tkinter import ttk
def addNewItem(user_name):
    addWin=Tk()

    addWin.title('View Items | Inventory - Management')
    #vait.geometry("800x700")
    addWin.resizable(0, 0)

    #L1
    L1 = Label(addWin,text="Inventory Management",font = ( "bold" , 32 , ), fg="blue")
    L1.pack()

    #L2
    L2 = Label(addWin,text="Add Items",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    L3 = Label(addWin,text="")
    L3.pack()
    def callGoIndex():
        try:
            addWin.destroy()
            import index
            index.main_scr(user_name)
        except:
            print("Cannot go back")
    def saveToDB():
        print('saved')
        item_name=E1.get()
        item_quantity=E2.get()
        item_price=E3.get()
        item_dec=E4.get()
        item_name_exists = check_if_item_name_exists(item_name)
        if (item_name!='' and item_quantity!='' and item_price!='' and item_dec!=''):
            if item_name_exists==False:
                insert_db(item_name, item_quantity, item_price, item_dec)
                L9.config(text="Added successfully")
            else:
                L9.config(text="That item already exists")
        else:
            L9.config(text="Please enter valid values")

    
    L4=Label(addWin, text="Item Name")
    L4.pack()
    E1=Entry(addWin, bd=5)
    E1.pack()

    L5=Label(addWin, text="Item Quantity")
    L5.pack()
    E2=Entry(addWin, bd=5)
    E2.pack()

    L6=Label(addWin, text="Item Price")
    L6.pack()
    E3=Entry(addWin, bd=5)
    E3.pack()

    L7=Label(addWin, text="Item Desc")
    L7.pack()
    E4=Entry(addWin, bd=5)
    E4.pack()

    #L8 empty
    L9 = Label(addWin,text="")
    L9.pack()

    B10 = Button(addWin,text="Add Item", command=saveToDB,fg="white", bg="green")
    B10.pack()
    B11 = Button(addWin,text="Go Back", command=callGoIndex,fg="white", bg="green",padx="12")
    B11.pack(side="right")

    #L8 empty
    L8 = Label(addWin,text="")
    L8.pack()

    #L9 empty
    L9 = Label(addWin,text="")
    L9.pack()
    addWin.mainloop()
#addNewItem("admin")
