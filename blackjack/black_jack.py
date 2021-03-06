# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades

import random

class Card(object):
    def __init__(self):
        self.color = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.value = range(1, 13)
        self.random_value = random.randint(1, 13)
        self.random_color = random.choice(self.color)
        self.chosen_card = str(self.random_value) + " " + str(self.random_color)


class Deck(object):
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards

    def create_list(self, number_of_cards):
        self.list_of_cards = []
        for n in range(self.number_of_cards):
            while card.color[n] == card.color[n - 1]:
                card.color[n - 1].color = card.random_color
            self.list_of_cards.append(Card().chosen_card)
        return self.list_of_cards


    def shuffle(self):
        random.shuffle(self.list_of_cards)
        return self.list_of_cards

    def draw(self):
        print(self.list_of_cards[-1])
        return self.list_of_cards.remove(self.list_of_cards[-1])



card = Card()
deck = Deck(4)
print(card.chosen_card)
print(deck.create_list(4))
print(deck.shuffle())
deck.draw()
print(deck.shuffle())
deck.draw()





#print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades

# top_card = deck.draw()
# print(top_card)
# print(deck)

# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
