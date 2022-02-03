import system_calls
import covid19_database
from os.path import exists
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


