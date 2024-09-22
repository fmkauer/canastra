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
            if not self.is_valid_sequence(player.hand[:3]):
                raise ValueError("Invalid sequence")
        else:
            # Adding to existing sequence - validate card
            if not self.is_valid_sequence(target_sequence + [card]):
                raise ValueError("Invalid card for this sequence")

        player.play_card(card, team_sequences, sequence_index)

    def is_valid_sequence(self, sequence: List[Card]) -> bool:
        """
        Check if a played sequence is valid according to Canastra rules.

        Args:
            sequence: A list of Card objects representing the played sequence.

        Returns:
            True if the sequence is valid, False otherwise.
        """
        # Check if the sequence has at least three cards
        if len(sequence) < 3:
            return False

        # Check if all cards have the same suit, considering wildcards
        wildcards = 0
        base_suit = None
        for card in sequence:
            if card.value == Value.JOKER or card.value == Value.TWO:
                wildcards += 1
            elif base_suit is None:
                base_suit = card.suit
            elif card.suit != base_suit:
                return False

        # Check if there are enough natural cards (non-wildcards)
        if len(sequence) - wildcards < 3:
            return False

        return True

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

    def check_canastra(self, sequence: List[Card]):
        """
        Check if a sequence forms a Canastra and apply scoring rules.

        Args:
            sequence: A list of Card objects representing the sequence.

        Returns:
            True if a Canastra is formed, False otherwise.
        """
        if len(sequence) < 7:
            return False

        # Check if the Canastra is clean or dirty
        is_clean = all(card.value != Value.TWO for card in sequence)

        # Apply scoring rules based on Canastra type
        if is_clean:
            # TODO: Implement scoring logic for clean Canastra
            print("Clean Canastra formed!")
        else:
            # TODO: Implement scoring logic for dirty Canastra
            print("Dirty Canastra formed!")

        return True
