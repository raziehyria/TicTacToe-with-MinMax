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
b1 = {1: ' ', 2: ' ', 3: ' ',
      4: ' ', 5: ' ', 6: ' ',
      7: ' ', 8: ' ', 9: ' '}

b2 = {1: ' ', 2: ' ', 3: ' ',
      4: ' ', 5: ' ', 6: ' ',
      7: ' ', 8: ' ', 9: ' '}
board1 = TicTacToe(b1)  # new game object
board2 = TicTacToe(b1)

print("Welcome to tic tac toe. Player is o. AI is x. Ai gets first move. Cheats on.")
# minimax play
player = 'o'  # used for optimal solution, in live game the optimal aids the player
print("Min max solution")
while not board1.check_winner():  # while a winner doesnt exist, make a move until one wins or board is full
    board1.computer_move()  # after every computer move
    board1.optimalmoves(player)  # the optimal solution takes in the state of the board and recc. opt. move for o
    board1.player_move()  # player then moves

# alpha beta minimax play
'''print("Alpha beta solution")
while not board2.check_winner():
    board2.ab_computer_move()
    board2.optimalmoves(player)
    board2.player_move()'''

'''
Part-2:
 Develop a function which takes a set of inputs from the 2-player game i.e., any state and 
outputs an optimal move for the player i.e., optimal state.
 Your program should also take an input set and provide an optimal move for that input. 
For  example,  consider  the  below  input.  You  are  the  "X"  player,  it  is  your  turn  to  move, 
and the current board configuration is shown below:
'''

new_state = {1: ' ', 2: ' ', 3: 'o',
             4: 'x', 5: ' ', 6: 'o',
             7: ' ', 8: ' ', 9: ' '}

new_state2 = {1: ' ', 2: ' ', 3: 'o',
              4: 'x', 5: 'o', 6: 'o',
              7: ' ', 8: ' ', 9: 'x'}

t = TicTacToe(new_state)
player = 'x'
t.print_board()
t.optimalmoves(player)
