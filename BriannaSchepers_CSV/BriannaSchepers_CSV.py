# This program lets a person enter in students name and 3 exam grades in a csv file formatted as a table.
import csv


def write():

    with open("grades.csv", "w", newline='') as f:

        students = int(input('How many students would you like to enter? '))

        csv_writer = csv.writer(f)

        # Writes the header for the csv file.
        csv_writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # This for loop gets the user data and writes it to the csv file.
        for x in range(students):

            first_name = input("Please enter the students first name: ")

            last_name = input("Please enter the students last name: ")

            # The input for the grades is converted to an int.

            exam1 = int(input("Please enter the students exam 1 score: "))

            exam2 = int(input("Please enter the students exam 2 score: "))

            exam3 = int(input("Please enter the students exam 3 score: "))

            csv_writer.writerow([first_name, last_name, exam1, exam2, exam3])


# This function displays the csv in tabular format.
def show():

    with open("grades.csv", "r") as f:

        csv_reader = csv.reader(f)

        print('|', "-"*87,'|')

        # Left adjusts the items in the row and adds spaces between them.
        for row in csv_reader:

            print('| {:<15} | {:<15} | {:<15} | {:<15} | {:<15} |'.format(*row))

            # Allows for the table separators to be printed.
            print('|','-'*15, '|','-'*15, '|','-'*15, '|','-'*15, '|', '-'*15,'|')


write()

show()
