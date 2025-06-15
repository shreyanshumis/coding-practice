import sqlite3

# Connect to the database (will create a new database if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, salary REAL)''')
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ("Shreyanshu M", 5000.0))
cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ("Khushi J", 6000.0))
conn.commit()
#========================================
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Employee Data:")
for row in rows:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Salary:", row[2])
    print()
cursor.close()
conn.close()
