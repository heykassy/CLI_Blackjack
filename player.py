class Player:
    def __init__(self, deck):
        self.money = 1000
        self.deck = deck
        self.hand = []
        self.current_bet = 0


    def bet(self):
        try:
            self.current_bet = int(input(f"You currently own ${self.money}. How much would like to bet on this match? $"))
            while (self.current_bet > self.money):
                print(f"You don't have enough money for this bet. Please pick a value you can bet.")
                self.current_bet = int(input(f"You currently own ${self.money}. How much would like to bet on this match? $"))
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


    def check_hand_sum(self):
        hand_sum = sum(card['points'] for card in self.hand)

        if hand_sum == 21:
            return 21
        # If sum is higher than 21 but one of the cards is an Ace, Ace becomes 1
        elif hand_sum > 21:
            for card in self.hand:
                if card['points'] == 11:
                    card['points'] = 1
                    return hand_sum - 10
            return 0
        else:
            return hand_sum


    def showHand(self):
        for card in self.hand:
            self.deck.showCard(card)


    def choose_hit_stay_double(self, choice, player_points):
        while choice == 'h':
            player_points = self.hit()
            
            if player_points == 21 or player_points == 0:
                return player_points
            else:
                choice = ''
                while choice not in ['h', 's', 'd']:
                    if 9 <= player_points <= 11:
                        choice = input("Hit[h], Stay[s] or Double Down[d]? ").strip().lower()
                    else:
                        choice = input("Hit[h] or Stay[s]? ").strip().lower()

        if choice == 'd':
            player_points = self.double()
        
        return player_points


    def hit(self):
        self.hand.append(self.deck.drawCard())

        print("YOUR HAND")

        self.showHand()

        player_points = self.check_hand_sum()

        print("┌───────────┐")
        print(f"| Score: {player_points:<2} |")
        print("└───────────┘")
        print("-----------------------------------------------------")

        return player_points


    def double(self):
        self.hand.append(self.deck.drawCard())
        self.current_bet *= 2

        print("YOUR HAND")

        self.showHand()

        player_points = self.check_hand_sum()

        print("┌───────────┐")
        print(f"| Score: {player_points:<2} |")
        print("└───────────┘")
        print("-----------------------------------------------------")

        return player_points