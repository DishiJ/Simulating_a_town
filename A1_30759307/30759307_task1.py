"""
Name - Dishi Jain
Student ID - 30759307
Start Date - 24 August 2019
Last Date Of Modification - 8 September 2019
High Level Description -
This python script reads a file called town_start.txt. After reading the values of the file town_start.txt.
The code will store it in the variables named as -
food
population
year
The python code then writes the values into another file called town_end.txt in the same format
"""

with open("town_start.txt", "r") as start_object:   # opening the file town_start.txt with file handling of
                                                        # read permission and using the object name as start_object
    data = start_object.read()          # read() will read the entire data in the file as a string and store it in data
    start_values = data.split()         # split() will split the string "data" with a delimiter of "\n" and store each
                                                    # value in the list start_values
    food = int(start_values[0])         # the list start_values stores the values as strings. Type casting to convert
                                                        # string into int for future manipulation of data
    population = int(start_values[1])
    year = int(start_values[2])         # storing values of list start_values in variables food, population, year

with open("town_end.txt", "w") as end_object:   # creating a new file town_end.txt with write permissions using
                                                # the object name as end_object
    for values in data:                 # for loop to iterate through the values present in the list data
        end_object.write(values)        # writing onto the file using write()
