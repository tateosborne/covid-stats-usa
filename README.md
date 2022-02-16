# Warm-Up Project, Group 5
###   Jack McCallum, Noah Jacobson, Josh Baker, Tate Osborne
###### CS 205 · _February 16, 2022_

For the warm-up project in CS205, we decided to model our project
around United States COVID-19 data. The data we use was collected on February 18, 2021.

##### There are two sets:
- One contains the numbers concerning the states in the United States.
- One contains the numbers concerning all counties in the United States

Both data sets contains fields `cases` and `deaths`.

The syntax of the user input is fairly strict; it must follow the format of the following:
```
[datatype] state [state abbreviation] county [county name]
```
- `datatype`: either `cases`, `deaths`, or `mortality`
  - `cases`- the number of cases in the specified region
  - `deaths` - the number of deaths in the specified region
  - `mortality` - the mortality rate in the specified region (i.e. ratio of `deaths`:`cases`)
- `state abbreviation`: the two-letter abbreviation of any state in the United States
- `county name`: the county name; do not include the word "county"

_Note that the user input is not case-sensitive_

There are extra commands, such as the following:
- `load` - Upon first use of the project, type `load` to load the .csv files into the database
- `help` - Returns example inputs that the user can use
- `date` - Returns the date of when the data was collected
- `source` - Returns a citation for where we found the data from
- `quit` - Exits the program
