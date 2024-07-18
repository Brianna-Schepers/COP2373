import math
from math import cos, radians


def get_hypotenuse():

    # Gets the user to input the angle and the length of the adjacent.

    angle = float(input("Enter the nearest angle in degrees: "))

    length = float(input("Enter the length of the adjacent side: "))

    # Uses cos from the math package to calculate the hypotenuse.

    hypotenuse = length/cos(radians(angle))

    print("The hypotenuse length is", round(hypotenuse, 3))


get_hypotenuse()
