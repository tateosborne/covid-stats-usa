import system_calls
import covid19_database
from os.path import exists
def get_input(user_input_list, loaded):
    datatype = ""
    state = ""
    county = ""
    if user_input_list[0] == 'load' and user_input_list[1] == 'data':
        if exists('covid_data.db'):
            print('Loading data...')
            covid19_database.insert_values()
            print('Done!')
            loaded = True
    elif user_input_list[0] == 'quit':
        print('Quitting')
        quit()
    elif loaded:
        if (user_input_list[0] in 'cases', 'deaths', 'mortality') & (exists(user_input_list[1])):
            if user_input_list[1] == 'total':
                return covid19_database.make_queries(user_input_list[0], None, None)
            else:



def get_state(user_input_list) -> str:
    state = user_input_list[2]
    if not len(state) == 2:
        return 'False'
    return state

def get_county(user_input_list) -> str:
    county = ""
    for i in range (4, len(user_input_list)):
        if i == 4:
            county = user_input_list[i]
        else:
            county += " "+user_input_list[i]
    return county

if __name__ == '__main__':
    running = True #Variable to hold whether the user wants to be playing.

    print("Welcome to our COVID data searcher!")
    print('Type "load data" if this is your first time running this.')
    print('Type "help" for a how-to guide on structuring queries.\n')
    loaded = False
    while running:
        user_input = input('Enter your Query: ')
        # turns user input to lowercase and splits along spaces
        user_input_list = user_input.lower().split(" ")
        print(get_input(user_input_list, loaded))


