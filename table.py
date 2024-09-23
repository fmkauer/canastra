from typing import List, Tuple

from cards import Card, Value
from player import Player
from waste import Waste
from deck import Deck

class Table:
    def __init__(self, players: List[Player], teams_amount: int):
        if len(players) != 4:
            raise ValueError("There must be 4 players")
        if teams_amount != 2:
            raise ValueError("There must be 2 teams")
        self.players = players
        self.teams_amount = teams_amount
        self.deck = Deck(2)
        self.waste = Waste()
        self.team1_sequences = []
        self.team2_sequences = []
        self.current_player_index = 0
        self.deal()
        self.card_values = {
            Value.A: 15,
            Value.TWO: 20,
            Value.THREE: 5,
            Value.FOUR: 5,
            Value.FIVE: 5,
            Value.SIX: 5,
            Value.SEVEN: 10,
            Value.EIGHT: 10,
            Value.NINE: 10,
            Value.TEN: 10,
            Value.J: 10,
            Value.Q: 10,
            Value.K: 10,
            Value.JOKER: 20,
        }

    def play_turn(self, player: Player):
        """Manages a player's turn during the game."""
        print("\nLixo:")
        self.waste.show()
        print(f"\n{player.name}'s hand:")
        player.show_hand()

        # 1. Draw a card
        if len(player.hand) > 1:
            draw_choice = input("Draw a card from the deck (d) or take the waste pile (w)? ").lower()
            if draw_choice == 'd':
                player.draw(self.deck)
            elif draw_choice == 'w':
                player.draw_from_waste(self.waste)
            else:
                print("Invalid choice. Drawing from the deck by default.")
                player.draw(self.deck)
        else:
            player.draw(self.deck)

        self.play_card(player)

        # 3. Discard a card
        self.discard_card(player)


    def play_card_to_sequence(self, player: Player, card: Card, team_sequences: list, sequence_index: int):
        player.play_card(card, team_sequences, sequence_index)

    def is_valid_move(self, card: Card, sequence: List[Card]) -> bool:
        """
        Check if playing a card to a sequence is a valid move in Canastra.

        Args:
            card: The Card object being played.
            sequence: A list of Card objects representing the sequence.

        Returns:
            True if the move is valid, False otherwise.
        """
        # If the sequence is empty, it's always valid to start a new one
        if not sequence:
            return True

        # Check if the card's suit or value matches the sequence, considering wildcards
        wildcards = [Value.JOKER, Value.TWO]
        base_suit = sequence[0].suit if sequence[0].value not in wildcards else None

        if card.value in wildcards or card.suit == base_suit:
            return True

        return False

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
            # Implement scoring logic for clean Canastra, adding points to the team score
            print("Clean Canastra formed!")
            return 200
        else:
            # Implement scoring logic for dirty Canastra, adding points to the team score
            print("Dirty Canastra formed!")
            return 100

    def calculate_sequence_score(self, sequence: List[Card]) -> int:
        """Calculates the score of a sequence."""
        score = 0
        sequence.sort()  # Sort the sequence to ensure cards are in order
        for card in sequence:
            score += self.card_values[card.value]
        if len(sequence) >= 7:
            for i in range(1, len(sequence)):
                if sequence[i].value == Value.TWO and sequence[i - 1].value == Value.THREE and sequence[i].suit == sequence[i - 1].suit:
                    score += 100  # Dirty Canastra with TWO as wildcard
                    break
            else:
                score += 200 if all(card.value != Value.TWO for card in sequence) else 100
        return score

    def calculate_team_score(self, team_sequences: List[List[Card]]) -> int:
        """Calculates the total score for a team."""
        total_score = 0
        for sequence in team_sequences:
            total_score += self.calculate_sequence_score(sequence)
        return total_score

    def get_round_scores(self) -> Tuple[int, int]:
        """Calculates and returns the scores for both teams for the current round."""
        team1_score = self.calculate_team_score(self.team1_sequences)
        team2_score = self.calculate_team_score(self.team2_sequences)
        return team1_score, team2_score

    def discard_card(self, player: Player):
        while True:
            try:
                card_index = int(input("Enter the index of the card to discard (0-based): "))
                card_to_discard = player.hand[card_index]
                player.discard(self.waste, card_to_discard)
                return
            except (ValueError, IndexError) as e:
                print(f"Invalid input: {e}")

    def get_cards_for_new_sequence(self, player: Player):
        starting = True
        while starting:
            try:
                # Display player's hand
                print(f"\n{player.name}'s hand:")
                for i, card in enumerate(player.hand):
                    print(f"{i}: {card}")
                card_index = int(input("Enter the index of the card to play (0-based): "))
                card_to_play = player.hand[card_index]

                # Determine which team the player belongs to
                if (self.players.index(player) + 1) % 2 == 0:
                    team_sequences = self.team2_sequences
                else:
                    team_sequences = self.team1_sequences

                # Attempt to play the card
                if self.is_valid_move(card_to_play, team_sequences[0]):
                    team_sequences.append([card_to_play])
                    print("Card played successfully!")
                    starting = False
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError) as e:
                print(f"Invalid input or move: {e}")

    
    def play_card(self, player: Player):
        playing = True
        while playing:
            play_card = input("Do you want to play a card? (y/n): ").lower()
            if play_card == 'y':
                # Display player's hand and team sequences
                print(f"\n{player.name}'s hand:")
                for i, card in enumerate(player.hand):
                    if i == len(player.hand) - 1:
                        print(f"> {i}: {card} <")
                    else:
                        print(f"{i}: {card}")
                self.show_sequences()

                # Choose to start a new sequence or add to an existing one
                while True:
                    choice = input("Start a new sequence (s) or add to an existing one (a)? ").lower()
                    if choice == 's':
                        self.get_cards_for_new_sequence(player)
                        break
                    elif choice == 'a':
                        adding = True
                        while adding:
                            try:
                                # Display player's hand
                                print(f"\n{player.name}'s hand:")
                                for i, card in enumerate(player.hand):
                                    print(f"{i}: {card}")
                                card_index = int(input("Enter the index of the card to play (0-based): "))
                                card_to_play = player.hand[card_index]

                                # Determine which team the player belongs to
                                if (self.players.index(player) + 1) % 2 == 0:
                                    team_sequences = self.team2_sequences
                                else:
                                    team_sequences = self.team1_sequences

                                sequence_index = player.choose_sequence(team_sequences)

                                # Attempt to play the card
                                if self.is_valid_move(card_to_play, team_sequences[sequence_index]):
                                    self.play_card_to_sequence(player, card_to_play, team_sequences, sequence_index)
                                    print("Card played successfully!")
                                else:
                                    print("Invalid move. Try again.")
                                    break  # Exit the loop if the card was played successfully
                            except (ValueError, IndexError) as e:
                                print(f"Invalid input or move: {e}")
                            
                            keep_adding = input("Do you want to add another card? (y/n): ").lower()
                            if keep_adding != 'y':
                                adding = False
                        break
                    else:
                        print("Invalid choice. Please enter 's' or 'a'.")
                
            else:
                playing = False