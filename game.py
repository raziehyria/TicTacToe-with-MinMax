'''
Game class to house all the basic features for a tictactoe game
'''
from minmax import MinImax


class TicTacToe:
    def __init__(self, board):
        # initialize board using a dictionary
        self.board_state = board
        self.player = 'o'
        self.computer = 'x'
        self.mm = MinImax()

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

    def check_winner(self):  # this function will check and see if any of the win states are met on the board
        if self.board_state[1] == self.board_state[2] and self.board_state[1] == self.board_state[3] \
                and self.board_state[1] != ' ':
            return True
        elif self.board_state[4] == self.board_state[5] and self.board_state[4] == self.board_state[6] \
                and self.board_state[4] != ' ':
            return True
        elif self.board_state[7] == self.board_state[8] and self.board_state[7] == self.board_state[9] \
                and self.board_state[7] != ' ':
            return True
        elif self.board_state[1] == self.board_state[4] and self.board_state[1] == self.board_state[7] \
                and self.board_state[1] != ' ':
            return True
        elif self.board_state[2] == self.board_state[5] and self.board_state[2] == self.board_state[8] \
                and self.board_state[2] != ' ':
            return True
        elif self.board_state[3] == self.board_state[6] and self.board_state[3] == self.board_state[9] \
                and self.board_state[3] != ' ':
            return True
        elif self.board_state[1] == self.board_state[5] and self.board_state[1] == self.board_state[9] \
                and self.board_state[1] != ' ':
            return True
        elif self.board_state[7] == self.board_state[5] and self.board_state[7] == self.board_state[3] \
                and self.board_state[7] != ' ':
            return True
        else:
            return False

    def winning_letter(self, letter):  # check which letter accomplished that win state
        if self.board_state[1] == self.board_state[2] and self.board_state[1] == self.board_state[3] \
                and self.board_state[1] == letter:
            return True
        elif self.board_state[4] == self.board_state[5] and self.board_state[4] == self.board_state[6] \
                and self.board_state[4] == letter:
            return True
        elif self.board_state[7] == self.board_state[8] and self.board_state[7] == self.board_state[9] \
                and self.board_state[7] == letter:
            return True
        elif self.board_state[1] == self.board_state[4] and self.board_state[1] == self.board_state[7] \
                and self.board_state[1] == letter:
            return True
        elif self.board_state[2] == self.board_state[5] and self.board_state[2] == self.board_state[8] \
                and self.board_state[2] == letter:
            return True
        elif self.board_state[3] == self.board_state[6] and self.board_state[3] == self.board_state[9] \
                and self.board_state[3] == letter:
            return True
        elif self.board_state[1] == self.board_state[5] and self.board_state[1] == self.board_state[9] \
                and self.board_state[1] == letter:
            return True
        elif self.board_state[7] == self.board_state[5] and self.board_state[7] == self.board_state[3] \
                and self.board_state[7] == letter:
            return True
        else:
            return False

    # inserting into board
    def insert_move(self, letter, pos):  # given the key and value
        if self.open_space(pos):  # if it's an open space
            self.board_state[pos] = letter  # insert the letter
            print(self.print_board())  # print board each time a letter is inserted
            if self.check_draw():  # ref check draw function,
                print("Draw!")
                exit()
            if self.check_winner():
                if letter == 'o':  # checks to see if the inserted layer belongs to the computer or the player
                    print("Player wins!")  # then if the win state is met, they win
                    exit()  # exit from the player input
                else:
                    print("Computer wins!")
                    exit()
            return
        else:
            print("Can't insert there!")  # invalid move, prompt a new input
            position = int(input("Please enter new position:  "))
            self.insert_move(letter, position)  # recurse to accommodate new move
            return

    # player move -- move into main py
    def player_move(self):
        position = int(input("Enter Position for 'o': "))
        self.insert_move(self.player, position)
        return

    # computer moves
    def computer_move(self):
        maxscore = -10
        bestmove = 0
        for key in self.board_state.keys():
            if self.board_state[key] == ' ':
                self.board_state[key] = self.computer
                score = self.mm.minimax(self.board_state, 0, False)
                self.board_state[key] = ' '
                if score > maxscore:
                    maxscore = score
                    bestmove = key
        self.insert_move(self.computer, bestmove)
        return


# testing
'''board = Game()
board.print_board()
board.insert_move('x', 1)
board.insert_move('0', 2)
print("Space open?", board.open_space(1))
board.print_board()
board.insert_move('0', 2)'''
