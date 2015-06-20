# -*-coding:Utf-8 -*

from random import randrange
from math import ceil

MAX_NUMBER = 50
MONEY_START = 1000
WRONG_VALUE = -1

class CasinoPlayer:

    ##
    # @brief constructeur de la classe
    #        initialise les membres de la classe
    #
    def __init__(self):
        self.money = MONEY_START 

    ##
    # @brief tire un nombre au hasard
    #
    def get_random_number(self):
        return randrange(MAX_NUMBER + 1)

    ##
    # @brief retourne l'argent possédé par le joueur 
    #
    def get_money(self):
        return self.money

    ##
    # @brief vérifie le nombre proposé
    #
    def check_number(self, number):
        try:
            number = int(number)
        except:
            print number,  "must be an integer"
            return WRONG_VALUE

        if number < 0 or number > MAX_NUMBER:
            print "you must choose a number between 0 and", MAX_NUMBER
            return WRONG_VALUE

        print "you choose", number
        return number
    
    ##
    # @brief vérifie le montant de la mise
    #
    def check_bet(self, bet):
        
        if bet < 0 or bet > self.money:
            print "you must bet between 0 and your actual money", self.money
            return WRONG_VALUE
      
        return bet
            
    ##
    # @brief joue la mise et vérifie si le joueur gagne
    #
    def play(self, number, bet):
        print "------------------------------------------"
        print "you played ", number, "for", bet, "$"
        random_number = self.get_random_number()

        print random_number, "has been selected"
        
        won_money = 0
        if number == random_number:
            won_money = bet * 3
            print "Good guess !"
        elif number % 2 == random_number % 2:
            print "Fair game, same color !"
            won_money = ceil(bet / 2)
        else:
            won_money = -bet

        self.money += won_money
        
        if won_money > 0:
            print "You won", won_money, "$ Congratulations !"
        else:
            print "You lose, better luck next time :)"

        print "your actual money is", self.money


##
# pour tester la classe en s'amusant :)
#
if __name__ == "__main__":
    player = CasinoPlayer()

    while player.get_money() > 0:
        played_number = WRONG_VALUE
        played_bet = WRONG_VALUE
        
        while played_number == WRONG_VALUE:
            played_number = input("Please choose a number between 0 and " + str(MAX_NUMBER) + ": ")
            played_number = player.check_number(played_number)

        while played_bet == WRONG_VALUE:
            played_bet = input("Please choose a bet between 1 and " + str(player.money) + ": ")
            played_bet = player.check_bet(played_bet)

        player.play(played_number, played_bet)

    print "Bye Bye"
