import random

class Deck:
    def __init__(self):
        self.deck = []

    
    def __len__(self):
        return len(self.deck)


    def generateCards(self):
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['♥', '♦', '♣', '♠']
        # Small deck for tests
        #values = ['A', '2', '3', '4', '5']
        #suits = ['♥']

        self.deck = [{'value': value, 'suit': suit} for value in values for suit in suits]

        for card in self.deck:
            if card['value'] == 'J' or card['value'] == 'Q' or card['value'] == 'K':
                card.update({'points': 10})
            elif card['value'] == 'A':
                card.update({'points': 1})
            else:
                card.update({'points': int(card['value'])})

        random.shuffle(self.deck)


    def showCard(self, dict):
        print("┌─────┐")
        print(f"|{dict['value']:<2}   |")
        print(f"|  {dict['suit']}  |")
        print(f"|   {dict['value']:>2}|")
        print("└─────┘") 


    def showDeck(self):
        for card in self.deck:
            self.showCard(card)

    def drawCard(self):
        # If all cards have been used, get a new deck of cards
        if len(self.deck) < 1:
            self.generateCards()
        return self.deck.pop()