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
            CREATE TABLE IF NOT EXISTS county_data 
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
            insert_with_param = '''INSERT INTO county_data (county, state_name, cases, deaths) VALUES (?, ?, ?, ?)'''
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
            insert_with_param = '''INSERT INTO state_data (state_name, cases, deaths) VALUES (?, ?, ?)'''
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
    if datatype == 'mortality':
        datatype = 'cases, deaths'
    if state == "" and county == "":
        formatted_query = f"SELECT {datatype} FROM state_data"

    # state
    elif county == "":
        formatted_query = f"SELECT {datatype} FROM state_data WHERE state_name='{state}'"

    # county
    elif state != "" and county != "":
        # Note: the below line only works if the county is one word long, get_county in main.py fixes this issue
        # county = county[0].upper() + (county[1:]) #Make first character upper
        formatted_query = f"SELECT {datatype} FROM county_data WHERE state_name='{state}' AND county='{county}'"
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

    data_int = 0
    data_list = c.fetchall()
    if len(data_list) == 0:
        return "No data for request found"
    elif len(data_list[0]) == 2:
        d = data_list[0]
        return f'{d[1]/d[0]:.4f}' + "%"
    else:
        for d in data_list:
            d_int = d[0]
            data_int += d_int
        c.close()
        return str(data_int)




def print_db():
    db_file = "covid_data.db"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("SELECT * FROM county_data")
    output = cur.fetchall()
    for i in range(len(output)):
        print(output[i])
def test_query():
    db_file = "covid_data.db"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute('SELECT "cases" FROM state_data WHERE state_name="VT"')
    output_string = cur.fetchall()
    print(cur.fetchall())
