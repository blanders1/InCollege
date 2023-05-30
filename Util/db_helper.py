import sqlite3
DB_CONNECTION = "InCollegeDB.db"


def db_connect():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_CONNECTION)
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


def remove_user(user_id):
    conn, cursor = db_connect()

    delete_query = "DELETE FROM Users WHERE id = ?"
    values = (user_id,)
    cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_user(user_id, name, email, phone_number):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET Name = ?, Email = ?, PhoneNumber = ? WHERE id = ?"
    values = (name, email, phone_number, user_id)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_user(user_id):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE id = ?"
    values = (user_id,)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def add_job(company, position, salary):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO Jobs (Company, Position, Salary) VALUES (?, ?, ?)"
    values = (company, position, salary)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_job(job_id):
    conn, cursor = db_connect()

    delete_query = "DELETE FROM Jobs WHERE id = ?"
    values = (job_id,)
    cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_job(job_id, company, position, salary):
    conn, cursor = db_connect()

    update_query = "UPDATE Jobs SET Company = ?, Position = ?, Salary = ? WHERE id = ?"
    values = (company, position, salary, job_id)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_job(job_id):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Jobs WHERE id = ?"
    values = (job_id,)
    cursor.execute(select_query, values)

    job = cursor.fetchone()

    db_close(conn, cursor)

    return job
