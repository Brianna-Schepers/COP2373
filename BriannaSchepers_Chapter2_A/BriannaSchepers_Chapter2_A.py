# This program reads an email and determines the chances of the email being spam.
def spam_detector():

    spamScore = 0

    # Establishes an empty list to add any words that cause the input to be flagged as spam.

    words = []

    file = open("Spam_Words.txt", "r")

    # Puts each line in the file into a list.

    spam_words = [line.strip() for line in file]

    user = input('Please enter an email message: ').lower()

    # Creates a for loop that runs for the length of the spam_words list.

    for i in range(len(spam_words)):

        # For each item in spam_words this counts the instances of them in the user input.

        count = user.count(spam_words[i])

        # Adds to the count for each spam word or phrase detected.

        spamScore += count

        # If any spam words or phrases are found this adds them to the empty words list from earlier.
        if count > 0:

            words.append(spam_words[i])

    print("Your spam score is: ", spamScore)

    print("Spam suspicion: ", words)

    # This creates an if statement to determine the chance of spam based on the spam score.

    if spamScore <= 1:

        print("Its not likely to be spam")

    elif spamScore <= 4:

        print("There is a chance of it being spam")

    else:

        print("It is most likely spam")


spam_detector()
