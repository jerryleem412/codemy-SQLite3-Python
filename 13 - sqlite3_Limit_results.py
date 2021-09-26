import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

#Limit returned results
c.execute("SELECT rowid, * FROM customers LIMIT 2") #limits 2 results


items = c.fetchall()

for item in items:
    print(item)


#Close connection
conn.close()
