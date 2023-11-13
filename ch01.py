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
print(Card('7', 'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

"""
Example 1-2. A simple two-dimensional vector class
"""

import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print('v1 + v2 =', v1 + v2)
