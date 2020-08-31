"""
Name - Dishi Jain
Student ID - 30759307
Start Date - 24 August 2019
Last Date Of Modification - 8 September 2019
High Level Description -
This script calculates the food remaining in the town at the end of a single year's cycle only.
It does not consider the changes in population.
Changes to food includes consumption, throwing away rotten food and placing order for new food.
The script firsts read the values of food, population and year from the file town_start.txt
It then performs the operations on food and writes the final values into the file town_end.txt
"""

import math  # importing math library to use the function floor() for later calculations

with open("town_start.txt", "r") as start_object:       # opening the file town_start.txt with file handling of read
                                                        # permission and using the object name as start_object
    start_values = start_object.readlines()             # readlines() will read the entire data in the file as
                                                # strings, with delimiter of "\n" and store it in the list start_values
    food = int(start_values[0])             # Type casting to convert string into int for future manipulation of data
    population = int(start_values[1])
    year = int(start_values[2])             # storing values of list start_values in variables food, population, year

with open("town_end.txt", "w") as end_object:
    if population > 0:
        if food <= population:
            food = 0            # when food is less than or equal to population the entire food gets consumed by
                                    # the population. Hence food becomes equal to 0
        elif food > population:
            food_left = food - population                   # food left after consumption by population
            food_thrown = food_left * (1 / 5)               # food thrown is 1/5th of food left after consumption
            food = math.floor(food_left - food_thrown)      # food left after throwing rotten food

        food = math.floor(food + ((80 / 100) * population))     # new food order placed which is 80% of population
        year += 1

    end_object.write(str(food) + "\n" + str(population) + "\n" + str(year))     # writing onto the file using write()
                                    # type casting int to string values again as write() accepts string parameters only
