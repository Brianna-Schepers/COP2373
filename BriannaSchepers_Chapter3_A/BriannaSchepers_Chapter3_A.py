# This code gets a users monthly expenses and shows them the total, highest, and lowest amounts.
import functools


def main():

    # Establishes the cont variable for the while loop to function.

    cont = 'y'

    # Empty lists created to store user input.

    expense = []

    cost = []

    # A while loop so the user can add expenses till they want to end the loop.

    while cont.lower() == 'y':

        print("Please enter a list of your monthly expenses, include the type of expense and the amount. ")

        userExpense = input("Type of expense: ")

        # Adds the user input to the empty expenses list for later use.

        expense.append(userExpense)

        userCost = int(input("Cost of expense: "))

        # Adds the user input to the cost list for later use.

        cost.append(userCost)

        cont = input("Do you want to input another expense? y/n? ")

    # Uses the reduce method to get the total of the cost list.

    print('\nTotal expenses: ', functools.reduce(lambda x, y: x + y, cost))

    # Prints the name and cost of the highest expense using reduce methods.

    print('The highest expense is', expense[cost.index(functools.reduce(max, cost))],
          "costing $", functools.reduce(max, cost))

    # Prints the name and cost of the lowest expense using reduce methods.

    print('The lowest expense is', expense[cost.index(functools.reduce(min, cost))],
          "costing $", functools.reduce(min, cost))


main()
