import system_calls
import covid19_database
from os.path import exists


def get_input(user_input_list, loaded):
    datatype = ""
    state = ""
    county = ""

    # system calls
    if user_input_list[0] == 'load':
        if not exists('covid_data.db'):
            print('Loading data...')
            covid19_database.create_connection()
            covid19_database.insert_values()
            loaded = True
            return "Done"
        else:
            return "Database is already Loaded"
    elif user_input_list[0] == 'quit':
        print('Quitting')
        quit()
    elif user_input_list[0] == 'help':
        system_calls.help_user()
    elif user_input_list[0] == 'date':
        print("Our data was collected on 2/18/21")

    elif len(user_input_list) >= 1:
        if user_input_list[0] in {'cases', 'deaths', 'mortality'}:
            datatype = user_input_list[0]
            if user_input_list[1] == 'total':
                return covid19_database.make_queries(datatype, "", "")
            elif len(user_input_list) == 3:
                return covid19_database.make_queries(datatype, get_state(user_input_list).upper(), "")
            elif len(user_input_list) > 4:
                return covid19_database.make_queries(datatype, get_state(user_input_list).upper(), get_county(user_input_list))
    return "Incorrect Syntax, try again"


# checks to see if state is formatted correctly, then separates for ease of use
def get_state(user_input_list) -> str:
    state = user_input_list[2]
    # checks length of state name to ensure validity
    if not len(state) == 2:
        print("State input should be in abbreviated form (i.e. VT)")
        return ""
    return state


# takes seperated names of counties, then returns to main with complete name
def get_county(user_input_list) -> str:
    # default value for county
    county = ""
    # runs through user_input_list from start of county name to end of list
    for i in range(4, len(user_input_list)-1):
        # for first part of county, no space for separation, but there is for rest
        if i == 4:
            county = user_input_list[i]
        else:
            county += " " + user_input_list[i]
    # case for invalid county entry
    if county == "":
        print("Invalid county specified")
        return ""
    return county


if __name__ == '__main__':
    running = True  # Variable to hold whether the user wants to be playing.

    print("Welcome to our COVID data searcher!")
    print('Type "load" if this is your first time running this.')
    print('Type "help" for a how-to guide on structuring queries.\n')
    loaded = False
    while running:
        user_input = input('Enter your Query: ')
        # turns user input to lowercase and splits along spaces
        user_input_list = user_input.lower().split(" ")
        print(get_input(user_input_list, loaded))

