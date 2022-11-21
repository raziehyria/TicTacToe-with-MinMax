'''
Game class to house all the basic features for a tictactoe game
'''
from minmax import MinImax
from abminmax import ABMinmax


class TicTacToe:
    def __init__(self, board):
        # initialize board using a dictionary
        self.board_state = board  # board state can be hardcoded or input for each game.
        self.player = 'o'
        self.computer = 'x'
        self.mm = MinImax()  # min max object
        self.ab = ABMinmax()  # alpha beta object

        # comparisons we will be using later on
        # win states for the board
        '''self.cases = {
            "top": self.board_state[1] == self.board_state[2] and self.board_state[1] == self.board_state[3],
            "mid": self.board_state[4] == self.board_state[5] and self.board_state[4] == self.board_state[6],
            "bot": self.board_state[7] == self.board_state[8] and self.board_state[7] == self.board_state[9],
            "left": self.board_state[1] == self.board_state[4] and self.board_state[1] == self.board_state[7],
            "center": self.board_state[2] == self.board_state[5] and self.board_state[2] == self.board_state[8],
            "right": self.board_state[3] == self.board_state[6] and self.board_state[3] == self.board_state[9],
            "ldiag": self.board_state[1] == self.board_state[5] and self.board_state[1] == self.board_state[9],
            "rdiag": self.board_state[7] == self.board_state[5] and self.board_state[7] == self.board_state[3]
        }
'''

    # print board
    def print_board(self):
        # values in board correspond to key in dictionary
        print(self.board_state[1] + '|' + self.board_state[2] + '|' + self.board_state[3])  # first row
        print('-+-+-')
        print(self.board_state[4] + '|' + self.board_state[5] + '|' + self.board_state[6])  # second row
        print('-+-+-')
        print(self.board_state[7] + '|' + self.board_state[8] + '|' + self.board_state[9])  # third
        print("\n")

    # check if space is free
    def open_space(self, pos):
        if self.board_state[pos] == ' ':  # if the space is empty
            return True  # returns true if it's an open space
        else:
            return False

    # checking for a winner or a draw
    def check_draw(self):
        for key in self.board_state.keys():  # accessing the values
            if self.board_state[key] == ' ':  # if any position of the board is empty, its not a draw
                return False
        return True  # otherwise, all positions are full and its a draw

    # this function will check and see if any of the win states are met on the board
    def check_winner(self):
        if self.board_state[1] == self.board_state[2] and self.board_state[1] == self.board_state[3] \
                and self.board_state[1] != ' ':
            return True  # top row
        elif self.board_state[4] == self.board_state[5] and self.board_state[4] == self.board_state[6] \
                and self.board_state[4] != ' ':
            return True  # middle row
        elif self.board_state[7] == self.board_state[8] and self.board_state[7] == self.board_state[9] \
                and self.board_state[7] != ' ':
            return True  # bottom row
        elif self.board_state[1] == self.board_state[4] and self.board_state[1] == self.board_state[7] \
                and self.board_state[1] != ' ':
            return True  # left column
        elif self.board_state[2] == self.board_state[5] and self.board_state[2] == self.board_state[8] \
                and self.board_state[2] != ' ':
            return True  # center column
        elif self.board_state[3] == self.board_state[6] and self.board_state[3] == self.board_state[9] \
                and self.board_state[3] != ' ':
            return True  # right column
        elif self.board_state[1] == self.board_state[5] and self.board_state[1] == self.board_state[9] \
                and self.board_state[1] != ' ':
            return True  # left diagonal
        elif self.board_state[7] == self.board_state[5] and self.board_state[7] == self.board_state[3] \
                and self.board_state[7] != ' ':
            return True  # right diagonal
        else:
            return False

    # check which letter accomplished said win state
    def winning_letter(self, letter):
        if self.board_state[1] == self.board_state[2] and self.board_state[1] == self.board_state[3] \
                and self.board_state[1] == letter:
            return True  # top row
        elif self.board_state[4] == self.board_state[5] and self.board_state[4] == self.board_state[6] \
                and self.board_state[4] == letter:
            return True  # middle row
        elif self.board_state[7] == self.board_state[8] and self.board_state[7] == self.board_state[9] \
                and self.board_state[7] == letter:
            return True  # bottom row
        elif self.board_state[1] == self.board_state[4] and self.board_state[1] == self.board_state[7] \
                and self.board_state[1] == letter:
            return True  # left column
        elif self.board_state[2] == self.board_state[5] and self.board_state[2] == self.board_state[8] \
                and self.board_state[2] == letter:
            return True  # center column
        elif self.board_state[3] == self.board_state[6] and self.board_state[3] == self.board_state[9] \
                and self.board_state[3] == letter:
            return True  # right column
        elif self.board_state[1] == self.board_state[5] and self.board_state[1] == self.board_state[9] \
                and self.board_state[1] == letter:
            return True  # left diagonal
        elif self.board_state[7] == self.board_state[5] and self.board_state[7] == self.board_state[3] \
                and self.board_state[7] == letter:
            return True  # right diagonal
        else:
            return False

    # inserting into board
    def insert_move(self, letter, pos):  # given the key and value
        if self.open_space(pos):  # if it's an open space
            self.board_state[pos] = letter  # insert the letter
            print(self.print_board())  # print board each time a letter is inserted
            if self.check_draw():  # check to see if there currently exists a draw,
                print("Draw!")
                exit()  # and exit the game
            if self.check_winner():  # other wise, check to see if any win states have occurred
                if letter == 'o':  # checks to see if the inserted letter belongs to the computer or the player
                    print("Player wins!")  # and they win
                    exit()  # exit from the player input
                else:  # other wise the opposing player wins
                    print("Computer wins!")
                    exit()
            return
        else:
            print("Can't insert there!")  # invalid move, prompt a new input
            position = int(input("Please enter new position:  "))
            self.insert_move(letter, position)  # recurse to accommodate new move
            return

    # player move --
    def player_move(self):
        print("Players's turn...")
        position = int(input("Enter Position for 'o': "))  # use user input to insert value to key
        self.insert_move(self.player, position)
        return

    # function that controls the AI, or computer movement using only minmax function
    def computer_move(self):
        maxscore = -10  # arbitrary number used for maximizing
        bestmove = 0  # number used to keep track of optimized position or key value
        print("Computer's turn...")
        for key in self.board_state.keys():  # so for every key or location on the board
            if self.board_state[key] == ' ':  # if there is an empty spot
                self.board_state[key] = self.computer  # insert that move
                score = self.mm.minimax(self.board_state, 0, False)  # check its score with minmax
                self.board_state[key] = ' '  # and undo the move
                if score > maxscore:  # and keep repeating until the best move is found
                    maxscore = score
                    bestmove = key
        self.insert_move(self.computer, bestmove)  # the optimized key with greatest value get sent to be inserted
        return

    # function that controls the AI, or computer movement using alpha beta
    def ab_computer_move(self):
        maxscore = -10  # arbitrary number used for maximizing
        alpha = -10  # arbitrary max for alpha beta
        beta = 10  # arbitrary min for alpha beta
        bestmove = 0  # number used to keep track of optimized position or key value
        print("Computer's turn...")
        for key in self.board_state.keys():  # for every key or location on the board
            if self.board_state[key] == ' ':
                self.board_state[key] = self.computer
                score = self.ab.abminimax(self.board_state, 0, False, alpha, beta)  # send to AB function for score
                self.board_state[key] = ' '
                if score > maxscore:  # and keep repeating until the best move is found
                    maxscore = score
                    bestmove = key
        self.insert_move(self.computer, bestmove) # the optimized key with greatest value get sent to be inserted
        return

    # function to return the optimal moves to the player
    def optimalmoves(self, player):
        if player == 'o':  # for the live game, the ai has to optimization methods change depending on target letter
            print("Min Max optimal move is: ", self.mm.mm_optimalMove(self.board_state))  # for player
        else:  # for x, or ai
            print("Alpha beta optimal move is: ", self.ab.ab_optimalMove(self.board_state))  # prints the optimal move

        # return self.ab.ab_optimalMove(self.board_state, player), self.mm.mm_optimalMove(self.board_state, player)


# testing
'''board = Game()
board.print_board()
board.insert_move('x', 1)
board.insert_move('0', 2)
print("Space open?", board.open_space(1))
board.print_board()
board.insert_move('0', 2)'''
