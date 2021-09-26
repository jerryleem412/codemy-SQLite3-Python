import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

c.execute("SELECT rowid, * FROM customers") #rowid is the hidden priary key sqlite3 auto creates.

items = c.fetchall()

for item in items:
    print(item)


#Commit Database
conn.commit()

#Close connection
conn.close()
