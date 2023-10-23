import random

class Card:
    def __init__(self, suit, value):
        self.Suit = suit
        self.Value = value

class Deck(Card):
    def __init__(self):
       self.cards = []
       suits = ['Hearts', 'Diamonds' , 'Clubs', 'Spades']
       values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

       for suit in suits:
           for value in values:
               self.cards.append(Card(suit, value))

    def shuffle (self):
        random.shuffle(self.cards)

    def deal (self):
        return self.cards.pop()

deck = Deck ()
deck.shuffle()

card = deck.deal()
print(card.Value, "of",  card.Suit)


    