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
            choice = self.player_choose(player_points)

            while choice == 'h':
                print("YOUR HAND")

                self.player.hit()
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

                elif player_points == 0:
                    print("*-=Bust=-*")
                    self.loseMatch()
                    continue

                else:
                    choice = self.player_choose(player_points)

            if choice == 'd':
                print("\n")
                print("YOUR HAND")

                self.player.double()
                self.player.showHand()

                player_points = self.player.check_hand_sum()

                print("┌───────────┐")
                print(f"| Score: {player_points:<2} |")
                print("└───────────┘")
                print("-----------------------------------------------------")

                if player_points == 21:
                    print("*-=Blackjack=-*")
                    self.winMatch()
                    break

                elif player_points == 0:
                    print("*-=Bust=-*")
                    self.loseMatch()
                    break


        sys.exit("Sorry, you lost the game! See you next time!")

    def player_choose(self, player_points):
        choice = ''
        while choice not in ['h', 's', 'd']:
            if 9 <= player_points <= 11:
                choice = input("Hit[h], Stay[s] or Double Down[d]? ").strip().lower()
            else:
                choice = input("Hit[h] or Stay[s]? ").strip().lower()
        return choice

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