# razie hyria's super late project
# proj1-tictactoe
# features: minmax and alphabeta pruning
# 442 algorithms course
from game import Game

"""
part 1:
Develop an application to play a tic-tac-toe game using minimax and alpha beta pruning
algorithm i.e., AI vs the player. (2 implementations – one using minimax and one using
alpha beta pruning)
Your program should allow the user to play and complete the game
"""

board2 = Game() #new game object
while not board2.check_winner(): # while a winner doesnt exist, allow each player to make a move
    board2.player_move()
    board2.computer_move()




