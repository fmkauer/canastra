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
        self.team1_sequences = []
        self.team2_sequences = []
        self.deal()
        self.current_player_index = 0

    def play_card_to_sequence(self, player: Player, card: Card, team_sequences: list):
        # TODO: Implement logic to find the correct sequence based on card and existing sequences
        target_sequence = team_sequences[0]  # Placeholder, replace with actual logic
        player.play_card(card, target_sequence)

    def deal(self):
        for _ in range(13):
            for player in self.players:
                player.draw(self.deck)

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.players[self.current_player_index]
