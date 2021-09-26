import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

#Delete records, use the primary key vs a column name, in this case rowid
c.execute("""DELETE from customers WHERE rowid = '6'


    """)

# c.execute("DELETE from custromers WHERE rowid = 6") #Can use this as well.

#Commit Database
conn.commit()


c.execute("SELECT rowid, * FROM customers") 
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'mckee'")  #Like allows search for upper and lower and like names.  You can use % as a wild card, eample 'mc%'


items = c.fetchall()

for item in items:
    print(item)


#Close connection
conn.close()
