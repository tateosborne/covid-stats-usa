import sqlite3
from sqlite3 import Error

# This function connects to an SQLite database 'db_file'
def create_connection(db_file):
    conn = None
    try:
        # conn represents the database
        conn  = sqlite3.connect(db_file)
        print(sqlite3.version)

        # Insert the tables to the database
        c = conn.cursor()

        # Create the table of county statistics
        # Table parameters are county, state, deaths
        c.execute('''
        CREATE TABLE IF NOT EXISTS County_Data 
        ([county] TEXT, [state] TEXT, [cases] INTEGER PRIMARY KEY, [deaths] INTEGER PRIMARY KEY)
        ''')

        # Create the table of state statistics
        # Table parameters are state, cases, deaths
        c.execute('''
        CREATE TABLE IF NOT EXISTS State_Data
        ([state] TEXT, [cases] INTEGER PRIMARY KEY, [deaths] INTEGER PRIMARY KEY)
        ''')
        conn.commit()
    # If there is an error, display which one
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    create_connection()