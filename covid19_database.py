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

# This function executes data entry from a csv file, line by line, into the database
# Previously created. This allows us to adjust data and re-enter it, so long as
# The CSV file format follows that of the DB credentials in the above method
def insert_values(db_file, county_csv, state_csv):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        # Now read in the csv file, split the data elements by line, and then
        # by comma. Convert necessary list elements from strings to ints, and insert
        # them into the table
        infile_county = open(county_csv, 'r')
        for line in infile_county:
            split_str = line.split(',')
            c.execute('''
                INSERT INTO County_Data (county, state, cases, deaths)
                
                    VALUES
                    (split_str[0], split_str[1], int(split_str[2]), int(split_str[3]))
            ''')
        # Close the file
        infile_county.close()

        # Repeat for the state csv_file
        infile_state = open(state_csv, 'r')
        for line in infile_state:
            split_str = line.split(',')
            c.execute('''
                    INSERT INTO State_Data (state, cases, deaths)

                        VALUES
                        (split_str[0], int(split_str[1]), int(split_str[2]),)
                    ''')
        # Close the file
        infile_state.close()

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
def retrieve_data(db_file: str, query: str) -> str:
    data = ""

    c.execute(query)

    return data

if __name__ == '__main__':
    create_connection()
