import sqlite3

#Query the database and return all records
def show_all():
    #Connect to Database
    conn = sqlite3.connect('customer.db') 
    #Create cursor
    c = conn.cursor()

    #Query Database
    c.execute("SELECT * from customers") 

    items = c.fetchall()
    for item in items:
        print(item)

    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()

#Add a new record
def add_one(first, last, email):
    #Connect to Database
    conn = sqlite3.connect('customer.db') 
    #Create cursor
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()

#define add many
def add_many(list):
    #Connect to Database
    conn = sqlite3.connect('customer.db') 
    #Create cursor
    c = conn.cursor()

    #delete record
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()  


#delete record
def delete_one(id):
    #Connect to Database
    conn = sqlite3.connect('customer.db') 
    #Create cursor
    c = conn.cursor()

    #delete record
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()   

#Where clause
def email_lookup(email):
        #Connect to Database
    conn = sqlite3.connect('customer.db') 
    #Create cursor
    c = conn.cursor()

    #delete record
    c.execute("SELECT * from customers WHERE email = (?)", (email,))

    items = c.fetchall()
    for item in items:
        print(item)
  
    #Close Connection
    conn.close()   

