import system_calls
import covid19_database
from os.path import exists

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
        print(get_input(user_input_list))


