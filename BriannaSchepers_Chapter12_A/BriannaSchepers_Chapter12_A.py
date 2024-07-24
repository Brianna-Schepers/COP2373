# This program uses numpy to perform mathematical functions on information from a csv file.
import csv
import numpy as np


def main():

    # Opens the csv file and puts the contents into an array.
    with open('grades.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    grades = np.array(data)

    print(grades[1:4])

    i = 0

    # Used to perform operations on the data from the exams individually.
    while i < 3:

        print("Exam", i + 1, "mean:", np.mean(grades[1:11, [i + 2]].astype(int)))

        print("Exam", i + 1, "median:", np.median(grades[1:11, [i + 2]].astype(int)))

        print("Exam", i + 1, "standard deviation:", round(np.std(grades[1:11, [i + 2]].astype(int)), 3))

        print("Exam", i + 1, "minimum:", np.min(grades[1:11, [i + 2]].astype(int)))

        print("Exam", i + 1, "maximum:", np.max(grades[1:11, [i + 2]].astype(int)), "\n")

        i += 1

    # Used to perform operations on the data from all the exams combined.

    print("All exams mean:", np.mean(grades[1:11, [2, 3, 4]].astype(int)))

    print("All exams median:", np.median(grades[1:11, [2, 3, 4]].astype(int)))

    print("All exams standard deviation:", round(np.std(grades[1:11, [2, 3, 4]].astype(int)), 3))

    print("All exams minimum:", np.min(grades[1:11, [2, 3, 4]].astype(int)))

    print("All exams maximum:", np.max(grades[1:11, [2, 3, 4]].astype(int)), "\n")

    # Gets the number of passing and failing grades respectively.

    passing_grades = (grades[1:11,[2,3,4]].astype(int) > 60).sum()

    failing_grades = (grades[1:11, [2, 3, 4]].astype(int) < 60).sum()

    print("Amount of passing scores:", passing_grades)

    print("Amount of failing scores:", failing_grades)

    print("Percent of passing grades", round((passing_grades / (passing_grades + failing_grades)) * 100, 2), "%")


main()

