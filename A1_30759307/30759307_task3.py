"""
Name - Dishi Jain
Student ID - 30759307
Start Date - 24 August 2019
Last Date Of Modification - 8 September 2019
High Level Description -
This script calculates the population of the town at the end of a single year's cycle.
It does not perform any changes to food.
Changes to population includes increasing population by 30% each year and decreasing the population by 40% every 18th
year for drafting of football players. Year 0 is considered as draft year.
The script firsts read the values of food, population and year from the file town_start.txt
It then performs the operations on population and writes the final values into the file town_end.txt
"""

import math         # importing math library to use the function floor() for later calculations
with open("town_start.txt", "r") as start_object:       # opening the file town_start.txt with file handling of read
                                                        # permission and using the object name as start_object
    start_values = start_object.readlines()             # readlines() will read the entire data in the file as
                                                # strings, with delimiter of "\n" and store it in the list start_values
    food = int(start_values[0])                # Type casting to convert string into int for future manipulation of data
    population = int(start_values[1])
    year = int(start_values[2])                # storing values of list start_values in variables food, population, year

with open("town_end.txt", "w") as end_object:       # creating a new file town_end.txt with write permissions
                                                    # using the object name as end_object
    if population > 0:                          # only runs the script if population is greater than 0
        if food <= population:
            population = food         # if food is less than population then the value of food will feed only a limited
                                      # population(1 food unit feeds 1 person). Remaining population will leave the town
        population = math.floor(population + ((30 / 100) * population))     # population increases by 30%
        if year % 18 == 0:                                     # Every 18th year population reduces by 40%
            population = math.floor(population - ((40 / 100) * population))
        year += 1

    end_object.write(str(food) + "\n" + str(population) + "\n" + str(year))     # writing onto the file using write()
                                    # type casting int to string values again as write() accepts string parameters only
