def help_user():
    print("------Possible Commands------")
    print("Start with the data you're trying to find.\n")
    print("cases - deaths - mortality\n")
    print("Then, chose how broad of a scope you want the data.\n")
    print("total - state [abbreviation]\n")
    print("Then finally, if you want to search for a specific county, name it.")
    print("NOTE: it is possible to just search for state data, and not county data.\n")
    print("County [name]\n")
    print("For example, a command to search for number of COVID deaths in Chittenden County, Vermont would look like "
          "this: ")
    print("deaths state VT county Chittenden\n")
    print("A command to search for COVID mortality in Connecticut would look like this:")
    print("mortality state CT\n")
    print("And finally, you can search for nationwide totals in any given category like this:")
    print("cases total\n")
    print("------System Commands------")
    print('Type "quit" to exit.')
    print('Type "date" to show when our data was collected.')
    # maybe we want this^ command to be named source, then show the NYT website and the date?
    print('Type "load data" to load the data. NOTE: You only need to do this once per computer.')
    return 'Type "help" to see this all again.'

# help_user()
