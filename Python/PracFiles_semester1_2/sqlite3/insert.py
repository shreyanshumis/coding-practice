import sqlite3

conn = sqlite3.connect('shrey.db')
cursor = conn.cursor()
  
# Queries to INSERT records.
cursor.execute(f'''INSERT INTO Student VALUES ('1','Raju', '19', 'Mumbai','10000')''')
  
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM Student''')
for row in data:
    print(row)
  
# Commit your changes in the database    
conn.commit()
  
# Closing the connection
conn.close()