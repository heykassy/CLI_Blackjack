class Player:
    def __init__(self, deck):
        self.money = 1000
        self.deck = deck
        self.hand = []
        self.current_bet = 0


    def bet(self):
        try:
            self.current_bet = int(input(f"You currently own {self.money}. How much would like to bet on this match? "))
            while (self.current_bet > self.money):
                print(f"You don't have enough money for this bet. Please pick a value you can bet.")
                self.current_bet = int(input(f"You currently own {self.money}. How much would like to bet? "))
            if self.current_bet <= 0:
                raise ValueError
            self.money -= self.current_bet

        except(ValueError):
            print('Please input a valid number')
            self.bet()


    def first_draw(self):
        self.hand = []
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())


    # Check sum for blackjack and (if not blackjack) return player's next options
    def check_hand_sum(self):
        # Sum all cards in hand
        hand_sum = sum(card['points'] for card in self.hand)

        #If blackjack, player/dealer wins
        if hand_sum == 21 or (hand_sum == 11 and (any(card['points'] == 1) for card in self.hand)):
            return 21
        # If bust, player/dealer loses
        elif hand_sum > 21:
            return 0
        else:
            return hand_sum


    def showHand(self):
        for card in self.hand:
            self.deck.showCard(card)


    def hit(self):
        self.hand.append(self.deck.drawCard())


    def double(self):
        self.hand.append(self.deck.drawCard())
        self.current_bet *= 2