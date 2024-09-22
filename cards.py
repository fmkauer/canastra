# create card releated functions
# possible suits: hearts, diamonds, clubs, spades
# possible values: A, 2-10, J, Q, K

from __future__ import annotations
from enum import Enum

class Suit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    CLUBS = "♣"
    SPADES = "♠"
    JOKER = "joker"

class Value(Enum):
    A = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    J = "J"
    Q = "Q"
    K = "K"
    JOKER = "joker"

class Card:
    def __init__(self, suit: Suit, value: Value):
        if not isinstance(suit, Suit):
            raise ValueError(f"Invalid suit: {suit}")
        if not isinstance(value, Value):
            raise ValueError(f"Invalid value: {value}")
        self.suit = suit
        self.value = value
        self.real_value = self.get_real_value()

    def __repr__(self):
        return "Joker" if self.value == Value.JOKER else f"{self.value.value}{self.suit.value}"
    
    def __lt__(self, other: Card):
        if isinstance(other, Card):
            # When comparing, compare the suits and the real values, the suits are compared first, being H, D, C, S
            if self.suit == other.suit:
                return self.real_value < other.real_value
            else:
                return self.suit.value < other.suit.value

    def get_real_value(self):
        if self.value == Value.JOKER:
            return 0
        elif self.value.value == Value.A.value:
            return 1
        elif self.value.value == 'J':
            return 11
        elif self.value.value == 'Q':
            return 12
        elif self.value.value == 'K':
            return 13
        else:
            return int(self.value.value)
