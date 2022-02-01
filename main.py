import system_calls

#Function that returns a string which is the numbered word of a larger string seperated by spaces

def parse_word(string, num_word):
    for i in num_word:
        hit_space = False
        out_string = ""
        while not hit_space:
            letter = 
            out_string +=

    hit_space = False

def get_output(user_input_list):
    input_size = len(user_input_list)

    # checks for system calls by user
    if input_size == 1:
        if user_input_list[0] == 'help':
            system_calls.help_user()
        elif user_input_list[0] == 'quit':
            quit()
        elif user_input_list[0] == 'date':
            # do we also want to have this print out our source?
            # possibly worth changing name of command if we do that
            print("Our data was collected on 2/18/2021")

    if input_size == 2:
        if user_input_list[0] == 'load' and user_input_list[1] == 'data':
            print('Loading data...')
            # TODO: follow up on the above print statement
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
        # some_var? = get_output(user_input_list)

