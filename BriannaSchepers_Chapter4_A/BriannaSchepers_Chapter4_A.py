# This program reads an email and determines the chances of the email being spam.
import time


def spam_detector():

    spamScore = 0

    # Establishes an empty list to add any words that cause the input to be flagged as spam.

    words = []

    spam_words = ['free money', 'prize', 'free gift', 'fast cash', 'earn money',
                  'apply now', 'urgent', 'winner', 'no cost', 'no interest', 'cash',
                  'deal', 'loans', 'offer', 'investment', 'discount', 'click now',
                  'action required', 'free membership', 'get paid', 'giveaway',
                  'money back', 'one time', 'risk-free', 'act now' 'exclusive',
                  'click here', 'you have been selected', 'congratulations', 'no fees']

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


def make_timer(func):
    def wrapper(*args, **kwargs):

        t1 = time.time()

        ret_val = func(*args, **kwargs)

        t2 = time.time()

        print('Time elapsed was', t2 - t1)

        return ret_val

    return wrapper


spam_detector = make_timer(spam_detector)

spam_detector()
