def insert_db(item_name, item_quantity, item_price, item_dec):
        item_name = item_name.lower()
        item_name = item_name.title()
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        #c.execute('DROP TABLE inventory')
        c.execute('CREATE TABLE IF NOT EXISTS inventory(item_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT UNIQUE, item_quantity INTEGER(10), item_price INTEGER(10), item_desc TEXT)')

        try:
                param_query = """INSERT INTO `inventory` ('item_name','item_quantity','item_price','item_desc') VALUES (?,?,?,?);"""
                data_tuple = (item_name, item_quantity, item_price, item_dec)
                c.execute(param_query, data_tuple)
                conn.commit()
        except:
                print("Cannot Insert in DB/ Value Duplicacy")
        #c.execute('SELECT * FROM inventory')
        #z=c.fetchall()
        #print(z)

        conn.close()

#insert_db('apsarA peNcil', 20, 2, 'Apsara Pencil')
###################################################################

def insert_db_sold(item_name, item_buyer, item_quantity, item_total_price):
        item_name = item_name.lower()
        item_name = item_name.title()
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        #c.execute('DROP TABLE inventory')
        c.execute('CREATE TABLE IF NOT EXISTS sold_data(sell_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT, item_buyer TEXT, item_quantity INTEGER(5), item_total_price INTEGER(5),sell_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')

        try:
                param_query = """INSERT INTO `sold_data` ('item_name','item_buyer','item_quantity','item_total_price') VALUES (?,?,?,?);"""
                data_tuple = (item_name, item_buyer, item_quantity, item_total_price)
                c.execute(param_query, data_tuple)
                conn.commit()
        except:
                print("Cannot Insert in DB")
        c.execute('SELECT * FROM inventory')
        z=c.fetchall()
        print(z)

        conn.close()

#insert_db('apsarA peNcil', 20, 2, 'Apsara Pencil')
###################################################################

def reduce_quantity_from_name(item_name,sub_qty):
        item_name = item_name.lower()
        item_name = item_name.title()
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        update_query = """UPDATE inventory SET item_quantity=? WHERE item_name=?"""
        prev_qty = select_single_row_item(2,item_name)
        #pass -1 for decrementing by one
        #else pass required factor to decrement
        if (sub_qty==-1):
                sub_qty=prev_qty-1
        else:
                if(prev_qty<sub_qty):
                        sub_qty=prev_qty
                else:
                        sub_qty=prev_qty-sub_qty
                
        update_data=(sub_qty,item_name)
        c.execute(update_query, update_data)
        conn.commit()
        conn.close()
################################################################

###################################################################

def increase_quantity_from_name(item_name,sub_qty):
        item_name = item_name.lower()
        item_name = item_name.title()
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        update_query = """UPDATE inventory SET item_quantity=? WHERE item_name=?"""
        prev_qty = select_single_row_item(2,item_name)
        #pass -1 for decrementing by one
        #else pass required factor to decrement
        if (sub_qty==-1):
                sub_qty=prev_qty+1
        else:
                if(prev_qty<10000):
                        sub_qty=prev_qty+sub_qty
                else:
                        sub_qty=prev_qty
                
        update_data=(sub_qty,item_name)
        c.execute(update_query, update_data)
        conn.commit()
        conn.close()


def check_if_item_name_exists(item_name):
        item_name = item_name.lower()
        item_name = item_name.title()
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        select_query = """SELECT item_name FROM inventory WHERE item_name = ?"""
        c.execute(select_query, (item_name,))
        record = c.fetchone()
        conn.close()
        if type(record) is tuple:
                return True
        else:
                return False
#print(check_if_item_name_exists("Apsara pencil"))
###################################################################
def get_price_from_item_name(item_name):
        item_name = item_name.lower()
        item_name = item_name.title()
        if check_if_item_name_exists(item_name)==True:
                import sqlite3
                conn = sqlite3.connect('inventory.db')
                c = conn.cursor()
                _query=('SELECT item_price FROM inventory WHERE item_name=?')
                c.execute(_query, (item_name,))
                items_tuple = c.fetchone()
                conn.close()
                return items_tuple[0]
        else:
                return "No Such Item"

#print(get_price_from_item_name("Apsara Pl"))

########################################################################            
def select_all_inventory_items():
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute('SELECT * FROM inventory')
        items_tuple = c.fetchall()
        conn.close()
        return items_tuple

#print(select_all_inventory_items())
##################################################################
def select_all_sold_items():
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute('SELECT * FROM sold_data')
        items_tuple = c.fetchall()
        conn.close()
        return items_tuple

#print(select_all_inventory_items())
###################################################################

def select_all_inventory_item_names():
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        c.execute('SELECT item_name,item_price FROM inventory')
        items_tuple = c.fetchall()
        conn.close()
        return items_tuple
#print(select_all_inventory_item_names())
###################################################################

def select_single_row(item_id):
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        select_query = """SELECT * FROM inventory WHERE item_id = ?"""
        c.execute(select_query, (item_id,))
        record = c.fetchone()
        conn.close()
        return record

#print(select_single_row(2))
##################################################################

def select_single_row_item(col_id,item_name):
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        select_query = """SELECT * FROM inventory WHERE item_name = ?"""
        c.execute(select_query, (item_name,))
        record = c.fetchone()
        conn.close()
        #col_id - 1-item_name, 2-item_quantity, 3-item_price, 4-item_desc
        return record[col_id]

#print(select_single_row_item(2,2))

##################################################################
def increment_quantity(item_id,add_qty):
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        update_query = """UPDATE inventory SET item_quantity=? WHERE item_id=?"""
        prev_qty = select_single_row_item(2,item_id)
        #pass -1 for incrementing by one
        #else pass required factor to increment
        if (add_qty==-1):
                add_qty=prev_qty+1
        else:
                add_qty=prev_qty+add_qty
                
        update_data=(add_qty,item_id)
        c.execute(update_query, update_data)
        conn.commit()
        conn.close()

#increment_quantity(2,3)
##################################################################

def decrement_quantity(item_id,sub_qty):
        import sqlite3
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        update_query = """UPDATE inventory SET item_quantity=? WHERE item_id=?"""
        prev_qty = select_single_row_item(2,item_id)
        #pass -1 for decrementing by one
        #else pass required factor to decrement
        if (sub_qty==-1):
                sub_qty=prev_qty-1
        else:
                if(prev_qty!=0):
                        sub_qty=prev_qty-sub_qty
                
        update_data=(sub_qty,item_id)
        c.execute(update_query, update_data)
        conn.commit()
        conn.close()
        
#decrement_quantity(2,4)
