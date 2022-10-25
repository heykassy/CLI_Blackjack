from player import Player

class Dealer(Player):
    def __init__(self, deck):
        self.money = 100000
        self.deck = deck
        self.hand = []