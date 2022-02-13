import sqlite3
from sqlite3 import Error


# This function connects to an SQLite database 'db_file'
def create_connection():
    # Variable declaration/definition
    db_file = "covid_data.db"

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
            ([county] TEXT, [state_name] TEXT, [cases] INTEGER, [deaths] INTEGER)
        ''')

        # Create the table of state statistics
        # Table parameters are state, cases, deaths
        c.execute('''
            CREATE TABLE IF NOT EXISTS State_Data
            ([state_name] TEXT, [cases] INTEGER, [deaths] INTEGER)
        ''')
        conn.commit()
    # If there is an error, display which one
    except Error as e:
        print("Error Raised in Create Connection")
        print(e)
    finally:
        if conn:
            conn.close()


# This function executes data entry from a csv file, line by line, into the database
# Previously created. This allows us to adjust data and re-enter it, so long as
# The CSV file format follows that of the DB credentials in the above method
def insert_values():

    # Variable declaration/definitions
    db_file = "covid_data.db"
    county_csv = 'county_data.csv'
    state_csv = 'state_data.csv'

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        # Now read in the csv file, split the data elements by line, and then
        # by comma. Convert necessary list elements from strings to ints, and insert
        # them into the table
        infile_county = open(county_csv, 'r')
        for line in infile_county:
            line = line.rstrip("\n")
            line = line.rstrip(line[-1])
            split_str = line.split(',')
            county_formatted = split_str[0]
            state_formatted = split_str[1]
            cases_formatted = int(split_str[2])
            deaths_formatted = int(split_str[2])
            insert_with_param = '''INSERT INTO county_data (county, state_name, cases, deaths) 
                    VALUES (?, ?, ?, ?)'''
            data_tuple = (county_formatted, state_formatted, cases_formatted, deaths_formatted)
            c.execute(insert_with_param, data_tuple)
            conn.commit()
        # Close the file
        infile_county.close()

        # Repeat for the state csv_file
        infile_state = open(state_csv, 'r')
        for line in infile_state:
            line = line.rstrip("\n")
            line = line.rstrip(line[-1])
            split_str = line.split(',')
            state_formatted = split_str[0]
            cases_formatted = int(split_str[1])
            deaths_formatted = int(split_str[2])
            insert_with_param = '''INSERT INTO state_data (state_name, cases, deaths)
                        VALUES (?, ?, ?)'''
            data_tuple = (state_formatted, cases_formatted, deaths_formatted)
            c.execute(insert_with_param, data_tuple)
            conn.commit()

        # Close the file
        infile_state.close()

    # If there is an error, display which one
    except Error as e:
        print("Error Raised in Insert Values")
        print(e)
    finally:
        if conn:
            conn.close()


# this function will take in the input arguments from parser and format into a SQL query
def make_queries(datatype: str, state: str, county: str) -> str:

    formatted_query = ""

    # Total
    if state == "" and county == "":
        formatted_query = f"SELECT '{datatype}' FROM state_data"

    # state
    elif county == "":
        formatted_query = f"SELECT '{datatype}' FROM state_data WHERE state_name='{state}'"

    # county
    elif state != "" and county != "":
        formatted_query = f"SELECT '{datatype}' FROM county_data WHERE state_name='{state}' AND county='{county}'"
        formatted_query.encode('unicode_escape')
    return retrieve_data(formatted_query)

# use formatted_query to gather the data to print to console
def retrieve_data(query: str) -> str:
    db_file = "covid_data.db"
    # conn represents the database
    conn = sqlite3.connect(db_file)
    # print(sqlite3.version)

    # Retrieve data from the desired table
    c = conn.cursor()
    c.execute(query)

    data_str = ""
    data_list = c.fetchall()
    for d in data_list:
        data_str += (str(d) + " ")
    c.close()

    return data_str


def print_db():
    db_file = "covid_data.db"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("SELECT * FROM County_Data")
    print(cur.fetchall())
