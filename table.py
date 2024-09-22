from typing import List

from cards import Card, Value
from player import Player
from waste import Waste
from deck import Deck

class Table():
    def __init__(self, players: List[Player], deck_amount: int = 2):
        self.players: List[Player] = players
        self.deck: Deck = Deck(deck_amount)
        self.waste: Waste = Waste()
        self.team1_sequences = []
        self.team2_sequences = []
        self.deal()
        self.current_player_index = 0

    def play_turn(self, player: Player):
        """Manages a player's turn during the game."""
        print("\nWaste pile:")
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

        print(f"You drew: {player.hand[-1]}")
        print(f"\n{player.name}'s hand:")
        for i, card in enumerate(player.hand):
            if i == len(player.hand) - 1:
                print(f"> {card} <")
            else:
                print(card)
        self.show_sequences()

        # 2. Play cards (optional)
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
                    selected_cards = []
                    while True:
                        # Display player's hand
                        print(f"\n{player.name}'s hand:")
                        for i, card in enumerate(player.hand):
                            if card in selected_cards:
                                print(f"> {i}: {card} <")
                            else:
                                print(f"{i}: {card}")

                        # Get player's card choice
                        try:
                            card_index = input(
                                "Enter the index of the card to add to the sequence (0-based, 'c' to confirm, 'q' to cancel): "
                            )
                            if card_index == 'c':
                                if len(selected_cards) >= 3:
                                    # Validate the new sequence
                                    if self.is_valid_move(selected_cards[0], selected_cards):
                                        # Determine which team the player belongs to
                                        if (self.players.index(player) + 1) % 2 == 0:
                                            self.team2_sequences.append(selected_cards.copy())
                                        else:
                                            self.team1_sequences.append(selected_cards.copy())
                                        # Remove cards from the player's hand
                                        for card in selected_cards:
                                            player.hand.remove(card)
                                        print("New sequence created successfully!")
                                        break
                                    else:
                                        print("Invalid sequence. Please select valid cards.")
                                else:
                                    print("A sequence must have at least 3 cards.")
                            elif card_index == 'q':
                                break
                            else:
                                card_index = int(card_index)
                                # Add or remove card from selection
                                if 0 <= card_index < len(player.hand):
                                    card = player.hand[card_index]
                                    if card in selected_cards:
                                        selected_cards.remove(card)
                                    else:
                                        selected_cards.append(card)
                                else:
                                    print("Invalid card index.")
                        except (ValueError, IndexError) as e:
                            print(f"Invalid input: {e}")
                    break
                elif choice == 'a':
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
                else:
                    print("Invalid choice. Please enter 's' or 'a'.")

        # 3. Discard a card
        while True:
            try:
                card_index = int(input("Enter the index of the card to discard (0-based): "))
                card_to_discard = player.hand[card_index]
                player.discard(self.waste, card_to_discard)
                break
            except (ValueError, IndexError) as e:
                print(f"Invalid input: {e}")


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
        # TODO: Implement logic to check if a team has more than 1500 points and requires a 100+ points first play


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

        return True
