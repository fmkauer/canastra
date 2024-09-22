# create deck related functions
from cards import Card, Suit, Value
import random
class Deck():
    def __init__(self, deck_amount: int = 1) -> None:
        if deck_amount < 1:
            raise ValueError("Deck amount must be at least 1")
        self.__cards = []
        self.build(deck_amount)
        self.shuffle()

    def __repr__(self):
        return f"Deck with {len(self.__cards)} cards"
    
    def build(self, amount: int):
        for _ in range(amount):
            for suit in Suit:
                for value in Value:
                    if value == Value.JOKER and suit == Suit.JOKER:
                        self.__cards.append(Card(Suit.JOKER, Value.JOKER))
                        self.__cards.append(Card(Suit.JOKER, Value.JOKER))
                    else:
                        if suit != Suit.JOKER and value != Value.JOKER:
                            self.__cards.append(Card(suit, value))
                random.shuffle(self.__cards)
    
    def shuffle(self):
        random.shuffle(self.__cards)
    
    def draw(self) -> Card:
        return self.__cards.pop()
