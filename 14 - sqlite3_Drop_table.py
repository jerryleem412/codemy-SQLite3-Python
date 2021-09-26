import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer_backup.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()



#Drop Table
c.execute("DROP TABLE customers") 


c.execute("SELECT * from customers") #This will fails cause table is now gone

items = c.fetchall()

for item in items:
    print(item)


#Close connection
conn.close()
