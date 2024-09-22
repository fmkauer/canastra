from deck import Deck
from cards import Card
from typing import List
from waste import Waste

class Player():
    def __init__(self, name):
        self.name = name
        self.hand: List[Card] = []
    
    def __repr__(self):
        return f"{self.name} has {len(self.hand)} cards"
    
    def draw(self, deck: Deck):
        self.hand.append(deck.draw())

    def show_hand(self):
        for card in self.hand:
            print(card)
    
    def discard(self, trash: Waste, card: Card):
        self.hand.remove(card)
        trash.add(card)

    def draw_from_waste(self, waste: Waste):
        self.hand.extend(waste.take())
