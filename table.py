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

    def play_card_to_sequence(self, player: Player, card: Card, team_sequences: list, sequence_index: int):
        target_sequence = team_sequences[sequence_index]
        if card not in player.hand:
            raise ValueError("Card not in hand")

        if len(target_sequence) == 0:
            # New sequence - needs at least 3 cards
            if len(player.hand) < 3:
                raise ValueError("Not enough cards to start a new sequence")
            # TODO: Validate that the 3 cards are a valid sequence
        else:
            # Adding to existing sequence - validate card
            # TODO: Implement validation for adding to existing sequence
            pass

        player.play_card(card, team_sequences, sequence_index)

    def deal(self):
        for _ in range(13):
            for player in self.players:
                player.draw(self.deck)

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.players[self.current_player_index]

    def show_sequences(self):
        print("Team 1 Sequences:")
        for sequence in self.team1_sequences:
            print(sequence)
        print("Team 2 Sequences:")
        for sequence in self.team2_sequences:
            print(sequence)
