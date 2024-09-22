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

    def play_card(self, card: Card, target_sequence: list, sequence_index: int):
        if card in self.hand:
            self.hand.remove(card)
            target_sequence[sequence_index].append(card)
        else:
            raise ValueError("Card not in hand")

    def choose_sequence(self, team_sequences: list):
        while True:
            print("Available sequences:")
            for i, sequence in enumerate(team_sequences):
                print(f"{i+1}. {sequence}")
            try:
                choice = int(input("Choose a sequence to add to (enter the number): ")) - 1
                if 0 <= choice < len(team_sequences):
                    return choice
                else:
                    print("Invalid sequence choice. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
