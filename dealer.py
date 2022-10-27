from player import Player

class Dealer(Player):
    def __init__(self, deck):
        self.money = 100000
        self.deck = deck
        self.hand = []

    def hit(self, dealer_points):
        self.hand.append(self.deck.drawCard())

        print("DEALER'S HAND")

        self.showHand()

        dealer_points = self.check_hand_sum()

        print("┌───────────┐")
        print(f"| Score: {dealer_points:<2} |")
        print("└───────────┘")
        print("-----------------------------------------------------")

        return dealer_points
        