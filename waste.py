from cards import Card

class Waste():
    def __init__(self):
        self.__cards = []
    
    def __repr__(self):
        return f"Trash with {len(self.__cards)} cards"
    
    def add(self, card: Card):
        self.__cards.append(card)
    
    def show(self):
        for card in self.__cards:
            print(card)
    
    def take(self):
        tmp = self.__cards
        self.__cards = []
        return tmp