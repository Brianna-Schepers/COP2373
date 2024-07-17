import random

# This program allows the user to deal and redraw poker cards.

class Deck:
    def __init__(self, size):

        self.card_list = [i for i in range(size)]

        self.cards_in_play_list = []

        self.discards_list = []

        random.shuffle(self.card_list)

    def deal(self):

        if len(self.card_list) < 1:

            random.shuffle(self.discards_list)

            self.card_list = self.discards_list

            self.discards_list = []

            print('Reshuffling...!!!')

        new_card = self.card_list.pop()

        self.cards_in_play_list.append(new_card)

        return new_card

    def new_hand(self):

        self.discards_list += self.cards_in_play_list

        self.cards_in_play_list.clear()

    # This method is used to redraw specific cards in the hand.
    def redraw(self):

        # Asks the user for what cards they want to redraw.

        numbers = input("Enter the numbers of which cards you want to replace separated by commas:")

        numbers_list = numbers.split(',')

        # Puts numbers into a list with int values for easier operations.

        numbers_list = [int(i) for i in numbers_list]

        # Checks to see if the numbers in numbers_list equal indexes in the current hand.

        for i in sorted(numbers_list, reverse=True):

            del self.cards_in_play_list[i-1]

            # For every matching index removed this adds a new card to the current hand.

            new_card = self.card_list.pop()

            self.cards_in_play_list.append(new_card)

        # Returns the cards_in_play_list to properly display the current hand.

        return self.cards_in_play_list


def main():

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
             '10', 'J', 'Q', 'K', 'A']

    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    my_deck = Deck(52)

    for i in range(5):

        d = my_deck.deal()

        r = d % 13

        s = d // 13

        print(ranks[r], 'of', suits[s])
    print()

    # Uses the list returned by the redraw method to print out the result of the drawing.

    for i in my_deck.redraw():

        r = i % 13

        s = i // 13
        print(ranks[r], 'of', suits[s])
    print()


main()
