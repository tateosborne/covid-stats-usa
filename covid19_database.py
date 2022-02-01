import sqlite3
from sqlite3 import Error

# This function connects to an SQLite database 'db_file'
def create_connection(db_file):
    conn = None
    try:
        # conn represents the database
        conn  = sqlite3.connect(db_file)
        print(sqlite3.version)
    # If there is an error, display which one
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    create_connection()