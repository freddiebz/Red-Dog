#Author: Frederica Zhang
#Date: Oct. 15, 2018
#Purpose: Play a game of Red Dog with the user
#T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T+T

import random

class TwoCard:
    def __init__ (self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        

#Author: Frederica Zhang
#Date: Oct. 15, 2018
#Purpose: Get a random integer between 2-14 to represent a card
#Parameters: none
#Returns: A random integer between 2-14
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def getCard():

    intCard = random.randint(2,14)
    return intCard


#Author: Frederica Zhang
#Date: Oct. 15, 2018
#Purpose: Create a hand for the user
#Parameters: none
#Returns: Two integers (as a TwoCard object)
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def getHand():

    card1 = getCard()
    card2 = getCard()
    cardHand = TwoCard(card1, card2)
    return cardHand


#Author: Frederica Zhang
#Date: Oct. 15, 2018
#Purpose: Print the user's hand
#Parameters: Two integers(as a TwoCard object)
#Returns: nothing
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def printHand(cardHand):

    print("Your Hand So Far Is:", end = " ")

    printCard(cardHand.card1)
    print(",", end = " ")

    printCard(cardHand.card2)
    print()


#Author: Frederica Zhang
#Date: Oct. 16, 2018
#Purpose: Determine the user's type of hand
#Parameters: Two integers(as a TwoCard object)
#Returns: Type of hand
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def handType(cardHand):

    if cardHand.card1 == cardHand.card2:
        handType = 1
    elif cardHand.card1 == cardHand.card2 - 1 or cardHand.card1 == cardHand.card2 + 1:
        handType = 2
    else:
        handType = 3

    return handType


#Author: Frederica Zhang
#Date: Oct. 17, 2018
#Purpose: Determine the spread of two cards
#Parameters: Two integers(as a TwoCard object)
#Returns: Spread of hand
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def spread(cardHand):

    spread = cardHand.card1 - cardHand.card2 - 1    
    return spread


#Author: Frederica Zhang
#Date: Oct. 17, 2018
#Purpose: Determine the payout for the user
#Parameters: An integer (spread)
#Returns: Payoff factor
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def payout(spread):

    if spread == 1:
        payout = 5
    elif spread == 2:
        payout = 4
    elif spread == 3:
        payout = 2
    else:
        payout = 1
    
    return payout
    

#Author: Frederica Zhang
#Date: Oct. 18, 2018
#Purpose: Determine if the third card is between the first two
#Parameters: Two integers(as a TwoCard object), another integer(card3)
#Retuns: True or false(for if the third card is between the first two)
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def between(cardHand, card3):

    if cardHand.card1 < card3 or card3 < cardHand.card2:
        inRange = False
    else:
        inRange = True

    return inRange


    #NOT PART OF ASSIGNMENT... but it made it easier JUST LIKE A FUNCTION SHOULD so :)
#Author: Frederica Zhang
#Date: Oct. 20, 2018
#Purpose: Edit for a postive integer between a min. and a max. value
#Parameters: One string(strPrompt), two integers (low and high)
#Returns: A positive integer between a min. and a max. value
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def getPositiveInteger(strPrompt, high, low):

    number = -1
    firstInput = True
    
    while number < low or number > high:
        if firstInput == False:
            print("That is not a bet you can pay!!")
            
        strNumber = input(strPrompt)
        
        while not strNumber.isdigit():
            print("That is not a bet you can pay!!")
            strNumber = input(strPrompt)
        number = int(strNumber)
        firstInput = False

    return number


#Author: Frederica Zhang
#Date: Oct. 18, 2018
#Purpose: Sort a TwoCard object in descending order
#Parameters: Two integers(as a TwoCard object)
#Retuns: Nothing
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def sort(cardHand):

    if cardHand.card1 < cardHand.card2:
        cardHand.card1, cardHand.card2 = cardHand.card2, cardHand.card1


#Author:Frederica Zhang
#Date: Oct. 19, 2018
#Purpose: Print a card
#Parameters: An integer(card)
#Returns: Nothing
#~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~
def printCard(card):

    intSuit = random.randint(1,4)

    if card >= 11:
        if card == 11:
            print("J", end = "")
        elif card == 12:
            print("Q", end = "")
        elif card == 13:
            print("K", end = "")
        elif card == 14:
            print("A", end = "")
    else:
        print(card, end = "")
    
    if intSuit == 1:
        print("♠", end = " ")
    elif intSuit == 2:
        print("♥", end = " ")
    elif intSuit == 3:
        print("♣", end = " ")
    else:
        print("♦", end = " ")

#~~~MAIN PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Welcome to Red Dog!!")
print("We've given you $100 to start off with.")
purse = 100
go = "r"

while go == "r" and purse > 0:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    bet = getPositiveInteger("Place your bet (full dollars only): $", purse, 1)
    purse = purse - bet
    print("You now have $%0.2f in your wallet." % (purse))
    print()
    
    playersHand = getHand()
    printHand(playersHand)
    sort(playersHand)
    print()
    
    if handType(playersHand) == 1:   #PAIR
        print("A pair! Let's see what the third card is...")
        thirdCard = getCard()
        printCard(thirdCard)
        print()
        if thirdCard == playersHand.card1:
            purse = purse + bet * 11
            print("Three of a kind! You get 11 times your original bet back!" \
                   "($%0.2f)" % (bet*11))
        else:
            purse = purse + bet
            print("Tie! You get to take back your money. ($%0.2f)" % (bet))

    elif handType(playersHand) == 2: #CONSECUTIVE
        purse = purse + bet
        print("Tie! You get to take back your money. ($%0.2f)" % (bet))

    else:                            #NON-CONSECUTIVE
        winRange = spread(playersHand)

        if purse > 0:
            print("You have", winRange, "different numbered card(s) that would let you win.")
            if purse < bet:
                raiseBet = getPositiveInteger("How much would you like to raise your bet by? " \
                                               "(full dollars only) $", purse, 0)
            else:
                raiseBet = getPositiveInteger("How much would you like to raise you bet by? " \
                                               "(maximum $%0.2f, full dollars only) $" % (bet), bet, 0)
            bet = bet + raiseBet
            purse = purse - raiseBet
            print("Your bet is now $%0.2f." % (bet))
        else:
            print("You have no more money in your wallet to raise your bet.")
        print()

        thirdCard = getCard()
        payoutFactor = payout(winRange)
        print("Your third card is", end= " ")
        printCard(thirdCard)
        print()

        if between(playersHand, thirdCard):
            purse = purse + bet * payoutFactor
            if winRange >= 1 and winRange <= 3:
                print("Win! You get %i times your bet back! ($%0.2f)" \
                       % (payoutFactor, bet*payoutFactor))
            else:
                print("Win! You get your bet back! ($%0.2f)" % (bet))
        else:
            print("You lose! That's $%0.2f gone now. :)" % (bet))

    print()
    print("You now have $%0.2f in your wallet." % (purse))
    if purse == 0:
        #give some money so the user can keep playing
        print("  _____")
        print(" | $50 |")
        print("~~~~~~~~~~~")
        print("Wait is that a $50 bill on the ground? Let's just add that to your wallet. :)")
        purse = purse + 50
        print()
        print("You now have $%0.2f in your wallet." % (purse))
    go = input("Enter r to play again. Enter e to end the game: ")
    while not(go == "r" or go == "e"):
        go = input("Enter r to play again. Enter e to end the game: ")

print("Thanks for playing!!")
        
         
    


