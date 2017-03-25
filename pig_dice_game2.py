#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Pig Dice Game 2"""

import random,time,argparse

#---------------------Here we starting a game by choosing yes on the question-----------------------------
def startNewGame():
    start = raw_input("Start New Game? Y or N ->  ")

    if start == 'Y' or start == 'y' or start == 'Yes' or start == 'yes' or start == 'YES':
        playerFactory = PlayerFactory()
        player1 = playerFactory.makeplayer(player1type)
        player2 = playerFactory.makeplayer(player2type)
        die = Dice()

        if not args.timed:
            newgame = Game(player1, player2, die)
        else:
            newgame = TimedGameProxy(player1, player2, die)

parser = argparse.ArgumentParser(description='Play Pig - 1 Player or 2 Player')
parser.add_argument("--player1", type=str, help="player1 'human' or 'computer'?")
parser.add_argument("--player2", type=str, help="player2 'human' or 'computer'?")
parser.add_argument("--timed", help="Timed Game?")
args = parser.parse_args()

#------------------This function gives us an option to either hold the dice of roll it--------------------
class Dice():
    def __init__(x):
        x.value = int()
        seed = 0

    def roll(x):
        x.value = random.randint(1, 6)

#---------------------------This function let us know who will go first-------------------------------------
class Game():
    def __init__(x, player1, player2, die):
        x.ts = 0
        x.die = die
        x.player1 = player1
        x.player2 = player2
        x.player1.score = 0
        x.player2.score = 0
        x.player1.ts = x.ts
        x.player2.ts = x.ts
        x.player1.name = "1st player"
        x.player2.name = "2nd player"

        CoinFlip = random.randint(1,2)
        if CoinFlip == 1:
            x.current_Gamer = player1
            print "1st player will start first"
        elif CoinFlip == 2:
            x.current_Gamer = player2
            print "2nd player will start first"
        else:
            print "Error, please try again later"
        x.Gamers_turn()

#------------------------------This function let us know what is our score------------------------------------
    def Gamers_turn(x):
        print "1st player score is:", x.player1.score
        print "2nd player score is:", x.player2.score
        x.die.roll()
        if (x.die.value == 1):
            print "Upps... You got 1! Your score is 0!"
            x.Next()
        else:
            x.ts = x.ts + x.die.value
            x.player1.ts = x.ts
            x.player2.ts = x.ts
            print "Rolling result is:", x.die.value
            print "Total score is:", x.ts
            x.current_Gamer.choose()
            if (x.current_Gamer.hold == True and x.current_Gamer.roll == False):
                x.current_Gamer.score = x.current_Gamer.score + x.ts
                x.Next()
            elif (x.current_Gamer.hold == False and x.current_Gamer.roll == True):
                x.Gamers_turn()

#---------------------This function let us who won the game and total score of the winner----------------------
    def Next(x):
        x.ts = 0
        if x.player1.score >= 100:
            print "1st player won. Congratulations!"
            print "Your total score is:", x.player1.score
            x.End()
            startNewGame()
        elif x.player2.score >= 100:
            print "2nd player won. Congratulations!"
            print "Your total score is:", x.player2.score
            x.End()
            startNewGame()
        else:
            if x.current_Gamer == x.player1:
                x.current_Gamer = x.player2
            elif x.current_Gamer == x.player2:
                x.current_Gamer = x.player1
            else:
                print "Error, please try again later"

            print "New players turn, player is now:", x.current_Gamer.name
            x.Gamers_turn()

    def End(x):
        x.player1 = None
        x.player2 = None
        x.die = None
        x.ts = None

if not args.player1:
    player1type = 'human'
else:
    player1type = args.player1

if not args.player2:
    player2type = 'human'
else:
    player2type = args.player2

class Player():
    def __init__(x):
        x.turn = False
        x.roll = True
        x.hold = False
        x.score = 0
        x.ts = 0

    def choose(x):
        decision = raw_input('%s: Please type (h) for Hold or (r) for Roll? ' % x.name)
        decision = str(decision)
        if decision == 'h':
            x.hold = True
            x.roll = False
        elif decision == 'r':
            x.hold = False
            x.roll = True
        else:
            print('You have entered an incorrect input. Please enter (h) for Hold or (r) for Roll')
            x.choose()

class ComputerPlayer(Player):
    def choose(x):
        limit1 = 25
        limit2 = 100 - x.score
        if (limit1 < limit2):
            holdlimit = limit1
        else:
            holdlimit = limit2

        if (x.ts < holdlimit):
            print "Computer is rolling"
            x.hold = False
            x.roll = True
        else:
            print "Computer is holding"
            x.hold = True
            x.roll = False


class PlayerFactory():
    def __init__(x):
        return None

    def makeplayer(x, playertype):
        if playertype == 'human':
            return Player()
        elif playertype == 'computer':
            return ComputerPlayer()
        else:
            print "Unknown Player Type"

#---------------------With this function we start the timed game----------------------
class TimedGameProxy(Game):
    def __init__(x, player1, player2, die):
        x.start_time = time.time()
        x.ts = 0
        x.die = die
        x.player1 = player1
        x.player2 = player2
        x.player1.score = 0
        x.player2.score = 0
        x.player1.ts = x.ts
        x.player2.ts = x.ts
        x.player1.name = "1st player"
        x.player2.name = "2nd player"

        CoinFlip = random.randint(1,2)
        if CoinFlip == 1:
            x.current_Gamer = player1
            print "1st player will start first"
        elif CoinFlip == 2:
            x.current_Gamer = player2
            print "2nd player will start first"
        else:
            print "Error, please try again later"
        x.Gamers_turn()

#---------------------This function let us who won the game and total score of the winner----------------------
    def Next(x):
        x.ts = 0
        if x.player1.score >= 100:
            print "1st player won. Congratulations!"
            print "Your total score is:", x.player1.score
            x.End()
            startNewGame()
        elif x.player2.score >= 100:
            print "2nd player won. Congratulations!"
            print "Your total score is:", x.player2.score
            x.End()
            startNewGame()
        else:
            if x.current_Gamer == x.player1:
                x.current_Gamer = x.player2
            elif x.current_Gamer == x.player2:
                x.current_Gamer = x.player1
            else:
                print "Error, please try again later"

            print "New players turn, player is now:", x.current_Gamer.name
            x.Gamers_turn()

#------------------------------This function let us know what is our score when time ends-----------------------
    def End_2(x):
        print "Game is over!"
        print "1st player's score is:", x.player1.score
        print "2nd player's score is:", x.player2.score
        if x.player1.score > x.player2.score:
            print "1st player won. Congratulations!"
            x.End()
        elif x.player2.score > x.player1.score:
            print "2nd player won. Congratulations!"
            x.End()
            startNewGame()
        else:
            print "Tie Game. Both players got the same score."
            x.End()
            startNewGame()

#------------------------------This function let us know what is our score------------------------------------
    def Gamers_turn(x):
        x.timer = time.time()
        if (x.timer - x.start_time >= 60):
            x.End_2()
        else:
            print "1st player score is:", x.player1.score
            print "2nd player score is:", x.player2.score
            x.die.roll()
            if (x.die.value == 1):
                print "Upps... You got 1! Your score is 0!"
                x.Next()
            else:
                x.ts = x.ts + x.die.value
                x.player1.ts = x.ts
                x.player2.ts = x.ts
                print "Rolling result is:", x.die.value
                print "Total score is:", x.ts
                x.current_Gamer.choose()
                if (x.current_Gamer.hold == True and x.current_Gamer.roll == False):
                    x.current_Gamer.score = x.current_Gamer.score + x.ts
                    x.Next()
                elif (x.current_Gamer.hold == False and x.current_Gamer.roll == True):
                    x.Gamers_turn()

startNewGame()
