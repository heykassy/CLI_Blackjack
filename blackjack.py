import sys
from pyfiglet import Figlet
from deck import Deck
from player import Player
from dealer import Dealer

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generateCards()
        self.player = Player(self.deck)
        self.dealer = Dealer(self.deck)


    def play(self):
        print(Figlet(font='standard').renderText('Blackjack'))

        while self.player.money != 0:
            self.player.bet()

            print('-===================================================-')
            
            self.player.first_draw()

            print("YOUR HAND")
            self.player.showHand()
            
            player_points = self.player.check_hand_sum()
            
            print("┌───────────┐")
            print(f"| Score: {player_points:<2} |")
            print("└───────────┘")
            print("-----------------------------------------------------")

            if player_points == 21:
                print("*-=Blackjack=-*")
                self.winMatch()
                continue
            
            self.dealer.first_draw()

            dealer_points = self.dealer.check_hand_sum()
            
            print("DEALER'S HAND")
            self.dealer.deck.showCard(self.dealer.hand[0])
            print("┌─────┐")
            print("|     |")
            print("|     |")
            print("|     |")
            print("└─────┘") 
            print("-----------------------------------------------------")


            # Choose next step: Hit, Stay, Double
            choice = ''
            while choice not in ['h', 's', 'd']:
                if 9 <= player_points <= 11:
                    choice = input("Hit[h], Stay[s] or Double Down[d]? ").strip().lower()
                else:
                    choice = input("Hit[h] or Stay[s]? ").strip().lower()

            player_points = self.player.choose_hit_stay_double(choice, player_points)

            if player_points == 21:
                print("*-=Blackjack=-*")
                self.winMatch()
                continue
            elif player_points == 0:
                print("*-=Bust=-*")
                self.loseMatch()
                continue


            # Dealer reveals cards, score and hit/stay
            print("DEALER'S HAND")
            self.dealer.showHand()
            
            print("┌───────────┐")
            print(f"| Score: {dealer_points:<2} |")
            print("└───────────┘")
            print("-----------------------------------------------------")

            while 0 < dealer_points <= 16:
                print("Dealer chose to HIT")
                dealer_points = self.dealer.hit(dealer_points)
            
            if dealer_points == 21:
                print("*-= Dealer Blackjack=-*")
                self.loseMatch()
                continue
            elif dealer_points == 0:
                print("*-=Dealer Bust=-*")
                self.winMatch()
                continue
            else:
                print("Dealer chose to STAY")

            # If no bust nor blackjack so far, compare scores to see who wins
            print("-----------------------------------------------------")
            print("Comparing hands:")
            print("PLAYER            DEALER")
            print("┌───────────┐     ┌───────────┐")
            print(f"| Score: {player_points:<2} |     | Score: {dealer_points:<2} |")
            print("└───────────┘     └───────────┘")

            if player_points > dealer_points:
                self.winMatch()
            elif player_points < dealer_points:
                self.loseMatch()
            else:
                self.push()


        print(Figlet(font='digital').renderText("Sorry, you lost the game!"))
        print("See you next time!")
        

    def winMatch(self):
        print('You won this match')
        print('-===================================================-')
        self.player.money += (self.player.current_bet * 2)
        # Jump current while loop and loops again

    def loseMatch(self):
        print('You lost this match')
        print('-===================================================-')
        # Jump current while loop and loops again

    def push(self):
        print("*-=Push=-*")
        print("It's a tie")
        print('-===================================================-')
        self.player.money += self.player.current_bet

Blackjack().play()