# Connecting a databse

# Modules
import pyodbc

# Create a trusted (safe) connection
connection = pyodbc.connect()

# Create a cursor object
cursor = connection.cursor()
cursor.execute()

# Retrive Query results from cursor
while 1:
  row = cursor.fetchone()
  if not row:
    break
  print(row.version)

# Close cursor and connection
cursor.close()
connection.close()