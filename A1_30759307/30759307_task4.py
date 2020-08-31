"""
Name - Dishi Jain
Student ID - 30759307
Start Date - 24 August 2019
Last Date Of Modification - 8 September 2019
High Level Description -
The script firsts read the values of food, population and year from the file town_start.txt
It then performs the operations on population and writes the final values into the file town_end.txt
Calculations on food and population are calculated for a maximum of 100 years from the start year.
Changes to food includes consumption, throwing away rotten food and placing order for new food.
Changes to population includes increasing population by 30% each year and decreasing the population by 40% every 18th
year for drafting of football players. Year 0 is considered as draft year.
"""

import math             # importing math library to use the function floor() for later calculations
with open("town_start.txt", "r") as start_object:       # opening the file town_start.txt with file handling of read
                                                        # permission and using the object name as start_object
    start_values = start_object.readlines()             # readlines() will read the entire data in the file as
                                                # strings, with delimiter of "\n" and store it in the list start_values
    food = int(start_values[0])                # Type casting to convert string into int for future manipulation of data
    population = int(start_values[1])
    year = int(start_values[2])                # storing values of list start_values in variables food, population, year
final_year = year + 100           # stores the maximum value of year till which the calculations will be done i.e +100
with open("town_end.txt", "w") as end_object:       # creating a new file town_end.txt with write permissions
                                                    # using the object name as end_object
    while(population >  0 and year < final_year):       # runs till population is greater than 0 and till 100 years
                                                            # from start year
        if food <= population:
            population = food         # if food is less than population then the value of food will feed only a limited
                                      # population(1 food unit feeds 1 person). Remaining population will leave the town
            food = 0                  # all food gets consumed hence food = 0
        elif food > population:
            food_left = food - population                          # food left after consumption by population
            food_thrown = food_left * (1/5)                        # food thrown is 1/5th of food left after consumption
            food = math.floor(food_left - food_thrown)             # food left after throwing rotten food
        population = math.floor(population + ((30 / 100) * population))         # population increases by 30%
        if year % 18 == 0:                                         # Every 18th year population reduces by 40%
            population = math.floor(population - ((40 / 100) * population))
        food = math.floor(food + ((80 / 100) * population))         # new food order placed which is 80% of population
        year += 1
    end_object.write(str(food) + "\n" + str(population) + "\n" + str(year))       # writing onto the file using write()
                                    # type casting int to string values again as write() accepts string parameters only
