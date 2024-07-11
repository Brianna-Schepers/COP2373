# This program lets the user perform basic money tasks using inheritance.
from decimal import Decimal


class Money(Decimal):

    # Allows for the decimal class to be mutable.

    def __new__(cls, amount, units='USD'):

        return super(Money, cls).__new__(cls, amount)

    # Defines how much money the user wants to start with and what currency.

    def __init__(self, amount, units='USD'):

        self.units = units

        self.amount = amount

    # Allows the user to add money.

    def addition(self, v2):

        self.amount += v2

    # Allows for the user to subtract money.

    def subtraction(self, v2):

        self.amount -= v2

    # Allows for the user to multiply money.

    def multiplication(self, v2):

        self.amount = self.amount * v2

        print(self.amount, self.units)


class BankAcct(Money):

    def __new__(cls, name, account_number, amount, interest_rate):

        return super(Money, cls).__new__(cls, amount)

    # Allows for all instances of the class to include these variables.

    def __init__(self, name, account_number, amount, interest_rate):

        self.name = name

        self.account_number = account_number

        self.amount = amount

        self.interest_rate = interest_rate

    # Lets the user change the interest rate

    def rate_change(self, new_interest):

        self.interest_rate = new_interest

    # Lets the user withdrawal money using the subtraction method in the money class.

    def subtraction(self, v2):

        super().subtraction(v2)

        print("Your current balance is: $", self.amount)

    # Lets the user deposit money using the addition method in the money class.

    def addition(self, v2):

        super().addition(v2)

        print("Your current balance is: $", self.amount)

    # Displays the current balance.
    def balance(self):

        print("Your current balance is: $", self.amount)

    # Calculates and displays the interest based on the days given.
    def calc_interest(self, days):

        interest_amt = self.amount * (self.interest_rate / 100) * days

        print("Your interest amount is: $", interest_amt)


# Tests to see if the methods in BankAcct work.

def test():

    info = BankAcct("Brianna ", 1234, 100, 1.25)

    info.subtraction(50)

    info.addition(200)

    info.rate_change(1.0)

    info.balance()

    info.calc_interest(4)


test()
