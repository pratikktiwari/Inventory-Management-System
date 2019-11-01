from imports import *
from tkinter import ttk
def viewAllItems(user_name):
    vait=Tk()

    vait.title('View Sold Items | Inventory - Management')
    #vait.geometry("800x700")
    vait.resizable(0, 0)

    #L1
    L1 = Label(vait,text="Inventory Management",font = ( "bold" , 32 , ), fg="blue")
    L1.pack()

    #L2
    L2 = Label(vait,text="Viewing Sold Items",font = ( "bold" , 15 , ), fg="green")
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
            
    def view_data():
        rows = select_all_sold_items()
        for row in rows:
            print(row)
            tree.insert("", END, values=row)


    tree=ttk.Treeview(vait, column=("id", "Name", "Buyer", "Quantity","Total Price","Timestamp"), show='headings')
    tree.heading("#1", text="Id")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Buyer")
    tree.heading("#4", text="Quantity")
    tree.heading("#5", text="Total Price")
    tree.heading("#6", text="Timestamp")

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
    
    
    vait.mainloop()
#viewAllItems("admin")
