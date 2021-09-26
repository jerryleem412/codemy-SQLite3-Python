import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

c.execute("SELECT * FROM customers")

items = c.fetchall()

for item in items:
    print(item[0] + " " + item[1] + " " + item[2])

#Commit Database
conn.commit()

#Close connection
conn.close()
