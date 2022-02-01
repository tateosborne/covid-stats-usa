import sqlite3
from sqlite3 import Error


# This function connects to an SQLite database 'db_file'
def create_connection(db_file):
    conn = None
    try:
        # conn represents the database
        conn = sqlite3.connect(db_file)
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

# this function will take in the input from parser and format into a SQL query
def make_queries(query: str) -> str:
    key_words = query.split()
    formatted_query = ""

    # load data
    if key_words[0] == "load" and key_words[1] == "data":
        pass

    # system commands
    elif len(key_words) == 1:
        pass

    # nation-wide commands
    elif key_words[1] == "total":
        pass

    # general commands
    else:
        if key_words[0] == "cases":
            pass
        elif key_words[0] == "deaths":
            pass
        elif key_words[0] == "mortality":
            pass


    return formatted_query

# use formatted_query to gather the data to print to console
def retrieve_data(query: str) -> str:
    data = ""

    return data

if __name__ == '__main__':
    create_connection()
