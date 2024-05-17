# This program asks the user to ask questions and displays random responses to simulate a 8ball.
import random

# This function is used to create the txt file.


def eight_ball():

    with open("8ball_responses.txt", "w") as f:

        # Writes all the requested text going to a new line after every phrase.

        f.write("Yes,of course!\nWithout a doubt,yes.\n"
                "You can count on it.\nFor sure!\n"
                "Ask me later!\nI'm not sure.\n"
                "I can't tell you right now.\nI'll tell you after my nap.\n"
                "No way!\nI don't think so.\n"
                "Without a doubt, no.\nThe answer is clearly NO!")


# The main function that interacts with the user.
def main():

    # Establishes cont as y so the while loop can get started.

    cont = 'y'

    file = open("8ball_responses.txt", "r")

    # This uses the line.strip method to add the phrases to a list with no whitespace.

    phrases = [line.strip() for line in file]

    # Uses a while loop to run til the user wants to exit the program by typing n.

    while cont == "Y" or cont == "y":

        input("Ask a yes or no question")

        # Selects a random item from phrases.

        print(random.choice(phrases))

        cont = input("Do you want to continue y/n?")

        # Makes sure the user cannot enter anything other than y or n.
        if cont != "y" and cont != "n":

            print("Invalid input")

            cont = input("Do you want to continue y/n?")


eight_ball()

main()
