# -*-coding:Utf-8 -*

from random import randrange
from math import ceil

MAX_NUMBER = 50
MONEY_START = 1000
WRONG_VALUE = -1

##
# @brief vérifie le nombre proposé
#
def check_number(number, value_min, value_max):
    try:
        number = int(number)
    except:
        print number,  "must be an integer"
        return WRONG_VALUE

    if number < value_min or number > value_max:
        print "you must choose a number between", value_min, "and", value_max
        return WRONG_VALUE

    print "you choose", number
    return number

##
# @brief jouons a la roulette
#
def play():
    money = MONEY_START

    # tant qu'il nous reste de l'argent
    while money > 0:
        number = WRONG_VALUE
        bet = WRONG_VALUE

        print "You have", money, "$"
        print "\n"
        
        # choisissons un nombre à jouer
        while number == WRONG_VALUE:
            number = input("Please choose a number between 0 and " + str(MAX_NUMBER) + ": ")
            number = check_number(number, 0, MAX_NUMBER)

        # choisissons une mise
        while bet == WRONG_VALUE:
            bet = input("Please choose a bet between 1 and " + str(money) + ": ")
            bet = check_number(bet, 0, money)

    
        print "------------------------------------------"
        print "you played ", number, "for", bet, "$"

        random_number = randrange(MAX_NUMBER + 1)
        print "->", random_number, "<-"

        # on calcule le montant gagné (ou perdu)
        won_money = 0
        if number == random_number:
            won_money = bet * 3
            print "Good guess !"
        elif number % 2 == random_number % 2:
            print "Fair game, same color !"
            won_money = ceil(bet / 2)
        else:
            won_money = -bet

        money += won_money
        
        if won_money > 0:
            print "You won", won_money, "$ Congratulations !"
        else:
            print "You lose, better luck next time :)"



if __name__ == "__main__":
    play()
