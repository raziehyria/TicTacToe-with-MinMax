# razie hyria's super late project
# proj1-tictactoe
# features: minmax and alphabeta pruning
# 442 algorithms course
from game import TicTacToe

"""
part 1:
Develop an application to play a tic-tac-toe game using minimax and alpha beta pruning
algorithm i.e., AI vs the player. (2 implementations – one using minimax and one using
alpha beta pruning)
Your program should allow the user to play and complete the game
"""
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
board2 = TicTacToe(board)  # new game object

while not board2.check_winner():  # while a winner doesnt exist, allow each player to make a move
    board2.computer_move()
    board2.player_move()


'''
Part-2:
 Develop a function which takes a set of inputs from the 2-player game i.e., any state and 
outputs an optimal move for the player i.e., optimal state.
 Your program should also take an input set and provide an optimal move for that input. 
For  example,  consider  the  below  input.  You  are  the  "X"  player,  it  is  your  turn  to  move, 
and the current board configuration is shown below:
'''
