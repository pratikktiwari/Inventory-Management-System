from imports import *
from tkinter import ttk
def viewAllItems(user_name):
    vait=Tk()

    vait.title('View Items | Inventory - Management')
    #vait.geometry("800x700")
    vait.resizable(0, 0)

    #L1
    L1 = Label(vait,text="Inventory Management",font = ( "bold" , 32 , ), fg="blue")
    L1.pack()

    #L2
    L2 = Label(vait,text="Viewing Items",font = ( "bold" , 15 , ), fg="green")
    L2.pack()
    #L3 empty
    L3 = Label(vait,text="")
    L3.pack()
    def callGoIndex():
        try:
            vait.destroy()
            import index
            index.main_scr(user_name)
        except:
            print("Cannot go back")
    def refreshScreen():
        try:
            vait.destroy()
            import viewAllItems
            viewAllItems.viewAllItems("adimn")
        except:
            print("Cannot destroy")
    def increaseQuantity():
        item_name=E1.get()
        item_qty=E2.get()
        if item_name!='' and item_qty!='':
            if item_qty.isdigit() and check_if_item_name_exists(item_name)==True:
                item_qty=int(item_qty)
                increase_quantity_from_name(item_name,item_qty)
                L10.config(text="Increment Successfull")
            else:
                L10.config(text="Please enter valid values")
        else:
            L10.config(text="Please fill all fields")
            
    def view_data():
        rows = select_all_inventory_items()
        for row in rows:
            print(row)
            tree.insert("", END, values=row)


    L4 = Label(vait, text="Enter the item name and quantity to sell item",fg="green",bg="yellow")
    L4.pack()
    L5 = Label(vait, text="Item Name")
    L5.pack()
    E1=Entry(vait)
    E1.pack()
    L6= Label(vait, text="Quanity of new items")
    L6.pack()
    E2=Entry(vait)
    E2.pack()
    
    L10 = Label(vait, pady="3")
    L10.pack()
    B3 = Button(vait,text="Increase Quantity",fg="white", bg="green", command=increaseQuantity)
    B3.pack()
    L11 = Label(vait, pady="3")
    L11.pack()
    tree=ttk.Treeview(vait, column=("id", "Name", "Quantity", "Price","Desc"), show='headings')
    tree.heading("#1", text="Id")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Quantity")
    tree.heading("#4", text="Price")
    tree.heading("#5", text="Desc")

    tree.tag_configure('odd', background='red')
    tree.tag_configure('even', background='green')

    ttk.Style().configure("Treeview", background="#383838", 
    foreground="white", fieldbackground="red",margin=1,border=1)

    ttk.Style().configure("Treeview.Heading",background="blue", foreground="blue", relief="flat")
    ttk.Style().configure("Treeview.Heading",relief=[('active','groove'),('pressed','sunken')])

    tree.pack()
    view_data()
    
    B15 = Button(text="Go Back", command=callGoIndex, fg="white", bg="green")
    B15.pack()
    B16 = Button(text="Refresh", command=refreshScreen, fg="white", bg="green")
    B16.pack()
    
    vait.mainloop()
#viewAllItems("admin")
