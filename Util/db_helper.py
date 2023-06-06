import sqlite3
DB_CONNECTION = "InCollegeDB"


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


def add_user(first_name, last_name, username, password):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO Users (First_Name, Last_Name, Username, Password) VALUES (?, ?, ?, ?)"
    values = (first_name, last_name, username, password)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_user(username, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        delete_query = "DELETE FROM MOCK_USERS WHERE username = ?"
        values = (username,)
        cursor.execute(delete_query, values)
    else:
        delete_query = "DELETE FROM Users WHERE username = ?"
        values = (username,)
        cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_user(username, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        update_query = "UPDATE MOCK_USERS SET Username = ? WHERE Username = ?"
        values = (username, username)
        cursor.execute(update_query, values)
    else:
        update_query = "UPDATE Users SET Username = ? WHERE Username = ?"
        values = (username, username)
        cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_user(username):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE Username = ?"
    values = (username,)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def get_user_by_name(first_name, last_name):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE First_Name = ? AND Last_Name = ?"
    values = (first_name, last_name)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def count_users(is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        count_query = "SELECT COUNT(*) FROM MOCK_USERS"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]
    else:
        count_query = "SELECT COUNT(*) FROM Users"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]

    db_close(conn, cursor)

    return count


def add_job(title, description, employer, location, salary, created_by):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = \
        "INSERT INTO Jobs (Title, Description, Employer, Location, Salary, Created_By) VALUES (?, ?, ?, ?, ?, ?)"
    values = (title, description, employer, location, salary, created_by)
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


def count_jobs():
    conn, cursor = db_connect()

    count_query = "SELECT COUNT(*) FROM Jobs"
    cursor.execute(count_query)

    count = cursor.fetchone()[0]

    db_close(conn, cursor)

    return count


def add_current_user(username):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO CurrentUser (Username) VALUES (?)"
    values = (username,)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_current_user():
    conn, cursor = db_connect()

    delete_query = "DELETE FROM CurrentUser"
    cursor.execute(delete_query)

    db_close(conn, cursor)


def get_current_user():
    conn, cursor = db_connect()

    select_query = "SELECT * FROM CurrentUser"
    cursor.execute(select_query)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user