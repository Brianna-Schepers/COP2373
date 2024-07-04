# This program lets a user enter in their banking information and perform basic banking tasks.

class BankAcct:

    # Allows for all instances of the class to include these variables.

    def __init__(self, name, account_number, amount, interest_rate):

        self.name = name

        self.account_number = account_number

        self.amount = amount

        self.interest_rate = interest_rate

    # Lets the user change the interest rate

    def rate_change(self, new_interest):

        self.interest_rate = new_interest

    # Lets the user withdrawal money and displays the new balance.

    def withdrawal(self, withdrawal_amount):

        self.amount -= withdrawal_amount

        print("Your new balance is: $", self.amount)

    # Lets the user deposit money and displays the new balance.

    def deposit(self, deposit_amount):

        self.amount += deposit_amount

        print("Your new balance is : $", self.amount)

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

    info.withdrawal(50)

    info.deposit(200)

    info.rate_change(1.0)

    info.balance()

    info.calc_interest(4)


test()
