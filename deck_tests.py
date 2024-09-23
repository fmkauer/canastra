from deck import Deck

def test_deck():
    deck = Deck()
    assert len(deck) == 54
    print(deck.draw())

test_deck()