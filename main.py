import system_calls
import covid19_database
from os.path import exists


def get_input(user_input_list):
    input_size = len(user_input_list)

    # checks for system calls by user

    if user_input_list[0] == 'help':
        system_calls.help_user()

    elif user_input_list[0] == 'quit':
        quit()

    elif user_input_list[0] == 'date':
        print("Our data was collected on 2/18/2021")

    elif user_input_list[0] == 'load' and user_input_list[1] == 'data':
        if exists()
        print('Loading data...')

        covid19_database.insert_values('covid_data', 'county_data.csv', 'state_data.csv')
        print('Done!')

    # acutal parsing here

    elif user_input_list[0] == 'cases':
        print('showing cases')

    elif user_input_list[0] == 'deaths':
        print('showing deaths')

    elif user_input_list[0] == 'mortality':
        print('showing mortality')
    # TODO: Follow these statements down so it can support more possible phrases

    # NOTE: NO REAL SWITCH STATEMENT IN PYTHON 3.9
    # Dictionaries maybe?


if __name__ == '__main__':
    running = True #Variable to hold whether the user wants to be playing.

    print("Welcome to our COVID data searcher!")
    print('Type "load data" if this is your first time running this.')
    print('Type "help" for a how-to guide on structuring queries.\n')

    while running:
        user_input = input('Enter your Query: ')
        # turns user input to lowercase and splits along spaces
        user_input_list = user_input.lower().split(" ")



        get_input(user_input_list)


