"""
Example 1-1. A deck as a sequence of playing cards
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(f'{beer_card=}')

deck = FrenchDeck()
print(f'{len(deck)=}')

print(f'{deck[0]=}')
print(f'{deck[-1]=}')

# NBVAL_IGNORE_OUTPUT
from random import choice


print(f'{choice(deck)=}')
print(f'{deck[:3]=}')
print(f'{deck[12::13]=}')

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

print(Card('Q', 'hearts') in deck)
