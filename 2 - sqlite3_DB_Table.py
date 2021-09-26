import sqlite3

#conn = sqlite3.connect(':memory:')  #creates a temp db in memory.
conn = sqlite3.connect('customer.db') #Creates or connects  End up with a customer.db file in current directory 

#Create cursor
c = conn.cursor()

#Create a Table
#The six double quets are to create a "doc string" that allows multiple SQL statements in a single string.
#SQLITE has 5 data types: NULL, INTEGER(1, 5, 789), REAL(1.564, 694.96544343 1.0), TEXT, BLOB(raw data)
c.execute("""CREATE TABLE customers (
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )""")

#Commit Database
conn.commit()

#Close connection
conn.close()
