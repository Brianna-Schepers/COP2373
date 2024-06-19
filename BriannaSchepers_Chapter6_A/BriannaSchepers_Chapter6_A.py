# This program gets phone numbers, social security numbers, and zip codes from users and detects if they're valid.

import re


# The main function used to get user input.

def main():
    phone_valid(input("Enter a phone number "))

    ssn_valid(input("Enter a ssn "))

    zip_valid(input("Enter a zip code"))


def phone_valid(phone_number):

    # Establishes a valid pattern for the phone number.

    phone = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'

    # Uses re.match to check if the format of the input matches the established format.

    if re.match(phone, phone_number):

        print("Phone number is valid.")

    else:

        print("Phone number is invalid.")


def ssn_valid(ssn):

    # Establishes a valid pattern for the social security number.
    social_security = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'

    # Uses re.match to check if the format of the input matches the established format.

    if re.match(social_security, ssn):

        print("Social security number is valid.")

    else:

        print("Social security number is invalid.")


def zip_valid(zipCode):

    # Establishes a valid pattern for the zip code.
    zip_code = r'\d\d\d\d\d$'

    # Uses re.match to check if the format of the input matches the established format.
    if re.match(zip_code, zipCode):

        print("Zip code is valid.")

    else:

        print("Zip code is invalid.")


main()
