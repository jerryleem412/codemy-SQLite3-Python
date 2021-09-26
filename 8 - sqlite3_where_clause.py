import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

c.execute("SELECT * FROM customers WHERE last_name = 'McKee'") 
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'mckee'")  #Like allows search for upper and lower and like names.  You can use % as a wild card, eample 'mc%'


items = c.fetchall()

for item in items:
    print(item)


#Commit Database
conn.commit()

#Close connection
conn.close()
