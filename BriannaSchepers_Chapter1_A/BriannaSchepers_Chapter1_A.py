# This program sells a pre-determined amount of cinema tickets.
# Each person is only allowed up to 4 tickets
# The program also keeps track of the amount of buyers and ends once tickets run out.
def cinema_tickets():

    # Establishes the constants of the program.

    TICKETS = 20

    LIMIT = 4

    buyers = 0

    i = 0

    # This while loop runs until the amount of tickets reaches zero.

    while i < TICKETS:

        amount = int(input("How many tickets would you like? "))

        # Increments the amount of buyers for each loop.
        buyers += 1

        # Makes sure the user cannot buy more tickets than the limit.

        if LIMIT < amount:

            print("That's too many tickets!")

            # Decreases BUYERS for an accurate total.
            buyers -= 1

        # Makes sure the user cannot buy more tickets than available.

        elif amount > TICKETS:

            print("Theres not enough tickets.")

            # Decreases the amount of buyers to compensate for extra loop.

            buyers -= 1

        # Subtracts the tickets bought from the ticket total.
        # Displays the ticket total after every loop.

        else:
            TICKETS = TICKETS - amount

            print("Remaining tickets: ", TICKETS)

            # If the tickets reach zero it displays that there are no more tickets.
            # Also displays the amount of people who bought tickets.
            # After this statement the while loop is ended.
            if TICKETS == 0:

                print("There's no more tickets.")

                print("Buyers: ", buyers)


# Calls the cinema_tickets function

cinema_tickets()
