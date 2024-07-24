# This program creates a database with population information.
# Then it calculates the population growth to create a matplotlib plot
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


# The main function used to create the database and the population table.
def main():

    population = sqlite3.connect('population_BS.db')

    # Creates the population table and establishes the fields of the table.

    population.execute('''CREATE TABLE population
             (City,
             Year  int,
             Population  float);
             ''')

    population.execute("INSERT INTO population VALUES ('Miami', 2023, 6265000)")

    population.execute("INSERT INTO population VALUES ('Tampa', 2023, 403364)")

    population.execute("INSERT INTO population VALUES ('Jacksonville', 2023, 1330000)")

    population.execute("INSERT INTO population VALUES ('Orlando', 2023, 2071000)")

    population.execute("INSERT INTO population VALUES ('Sarasota', 2023, 464223)")

    population.execute("INSERT INTO population VALUES ('Pensacola', 2023, 53724)")

    population.execute("INSERT INTO population VALUES ('Naples', 2023, 19704)")

    population.execute("INSERT INTO population VALUES ('Clearwater', 2023, 116850)")

    population.execute("INSERT INTO population VALUES ('Gainesville', 2023, 138741)")

    population.execute("INSERT INTO population VALUES ('Fort Myers', 2023, 84694)")

    population.commit()

    population.close()


# The function used to calculate the population growth.
def population_growth():

    population = sqlite3.connect('population_BS.db')

    i = 0

    # A while loop to calculate population growth and add the values to new columns in population.
    while i < 20:

        population.execute(f'''ALTER TABLE population ADD COLUMN Year_{i+1} float;''')

        population.execute(f'''UPDATE population SET Year_{i+1} = population * POWER((1+.02),{i+1});''')
        i += 1

    population.commit()

    population.close()


# The function to display the population growth visually from user input.
def show_population_growth():

    population = sqlite3.connect('population_BS.db')

    statement = '''SELECT city FROM population'''

    population_cursor = population.cursor()

    population_cursor.execute(statement)

    output = population_cursor.fetchall()

    # Displays the cities the user can choose from.

    for row in output:

        print(row[0])

    city = input('What city would you like to see the population growth for?: ')

    population_cursor.execute(f'''SELECT DISTINCT Year_1, Year_2, Year_3, Year_4, Year_5,
     Year_6, Year_7, Year_8, Year_9, Year_10, Year_11, Year_12, Year_13, Year_14,
     Year_15, Year_16, Year_17, Year_18, Year_19, Year_20 FROM population WHERE UPPER(City)= UPPER('{city}');''')

    result = population_cursor.fetchall()

    population_value = np.array([])

    years = np.array([2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031,
                      2032, 2034, 2035, 2036, 2037, 2038, 2039, 2040,
                      2041, 2043, 2043, 2044])

    # Appends data from the population table to an array so it can be used on a plot.
    for i in result:

        population_value = np.append(population_value, i)

    plt.plot(years, population_value)

    plt.show()


main()

population_growth()

show_population_growth()
