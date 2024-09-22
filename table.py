from deck import Deck
from player import Player
from waste import Waste
from cards import Card
from typing import List

class Table():
    def __init__(self, players: List[Player], deck_amount: int = 2):
        self.players: List[Player] = players
        self.deck: Deck = Deck(deck_amount)
        self.waste: Waste = Waste()
        self.deal()

    def deal(self):
        for _ in range(13):
            for player in self.players:
                player.draw(self.deck)