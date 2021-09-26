import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

c.execute("SELECT * FROM customers")

print(c.fetchall())

#Commit Database
conn.commit()

#Close connection
conn.close()
