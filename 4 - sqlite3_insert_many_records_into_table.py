import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

many_customers = [
                    ('Wes', 'Brown', 'wes@brown.com'),
                    ('Steph', 'Kuewa', 'steph@kuewa.com'), 
                    ('Dan', 'Pas', 'dan@pas.com'),
                ]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)


#Commit Database
conn.commit()

#Close connection
conn.close()
