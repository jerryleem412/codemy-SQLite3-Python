from sqlite3.dbapi2 import sqlite_version_info
import sqlite3_App_functions as database

#Add record
#database.add_one("Laura", "Smith", "lsmith@smith.com")


#delete record 
#database.delete_one('6')

#Add many records
# stuff = [
#     ('Brenda','Smitherton','bsmitherton@smitherton.com'),
#     ('Joshua','Raintree','jraintree@raintree.com')
# ]
# database.add_many(stuff)

#show all records
#database.show_all()

database.email_lookup('jraintree@raintree.com')




