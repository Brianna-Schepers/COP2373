# This program creates a money class that allows for addition, subtraction, and multiplication.

from decimal import Decimal


class Money(Decimal):

    # Allows for the decimal class to be mutable.

    def __new__(cls, v, units='USD'):

        return super(Money, cls).__new__(cls, v)

    # Defines how much money the user wants to start with and what currency.

    def __init__(self, v, units='USD'):

        self.units = units

        self.v = v

    # Allows the user to add money.

    def addition(self, v2):

        self.v += v2

        print(self.v, self.units)

    # Allows for the user to subtract money.

    def subtraction(self, v2):

        self.v -= v2

        print(self.v, self.units)

    # Allows for the user to multiply money.

    def multiplication(self, v2):

        self.v = self.v * v2

        print(self.v, self.units)


# Tests the operations of the money class.

def test():

    m = Money(10, 'USD')

    m.addition(5)

    m.subtraction(5)

    m.multiplication(5)


test()
