import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

#Update records, use the primary key vs a column name, in this case rowid
c.execute("""UPDATE customers SET first_name = 'John' 
            WHERE rowid = '2'


    """)

#Commit Database
conn.commit()


c.execute("SELECT rowid, * FROM customers") 
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'mckee'")  #Like allows search for upper and lower and like names.  You can use % as a wild card, eample 'mc%'


items = c.fetchall()

for item in items:
    print(item)


#Close connection
conn.close()
