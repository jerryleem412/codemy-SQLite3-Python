import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

#Order results default is Ascending can change with "SELECT rowid, * FROM customers ORDER BY rowid DESC"
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid=3") #can use AND


items = c.fetchall()

for item in items:
    print(item)


#Close connection
conn.close()
