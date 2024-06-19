# This program counts the number of sentences in a string.

import re


def main():

    count = 0

    s = '''See the U.S.A. today. It's right here, not
a world away. Average temp. is 66.5.'''

    # Establishes the criteria for a new sentence.

    pat = r'[A-Z 1-9].*?[.!?](?= [A-Z 1-9]|$)'

    # Used to find the sentences in the string.

    m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)

    # Prints the sentences in new lines.

    for i in m:

        print('->', i)

        count += 1

    print("There are", count, "sentences.")


main()
