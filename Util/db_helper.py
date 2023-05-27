import sqlite3
DB_CONNECTION = "InCollegeDB.db"


def db_connect():
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    return conn, cursor


def db_close(conn, cursor):
    # Commit the transaction to save the changes
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()


def add_user(name, email, phone_number):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO Users (Name, Email, PhoneNumber) VALUES (?, ?, ?)"
    values = (name, email, phone_number)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)

def remove_user():
    conn, cursor = db_connect()

    db_close(conn, cursor)

def edit_user():
    conn, cursor = db_connect()

    db_close(conn, cursor)


def add_job(company, position, salary):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO Jobs (Company, Position, Salary) VALUES (?, ?, ?)"
    values = (company, position, salary)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)

def remove_job():
    conn, cursor = db_connect()

    db_close(conn, cursor)

def edit_job():
    conn, cursor = db_connect()

    db_close(conn, cursor)
