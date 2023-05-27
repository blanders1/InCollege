import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('InCollegeDB.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS Users (
    Name TEXT,
    Email TEXT,
    PhoneNumber TEXT
)
'''
cursor.execute(create_table_query)

# Execute a query to insert data into the table
insert_query = "INSERT INTO Users (Name, Email, PhoneNumber) VALUES (?, ?, ?)"
values = ('John Doe', 'johndoe@example.com', '1234567890')
cursor.execute(insert_query, values)

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()