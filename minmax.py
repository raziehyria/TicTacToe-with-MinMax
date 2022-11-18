"""
minimax class to house the main algorithms and functions used for minimax algorithm
"""

class MinImax:

    def __init__(self):
        self.board = {}

    def minimax(self, computer, player, board, limit, maximum, winningletter, checkdraw):

        if winningletter(player):
            return 1
        elif winningletter(player):
            return -1
        elif checkdraw:
            return 0

        if maximum:
            maxScore = -1000
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = computer
                    score = self.minimax(self, computer, player, board, limit+1, maximum, winningletter, checkdraw)
                    board[key] = ' '
                    if score > maxScore:
                        bestScore = max(maxScore,score)
            return maxScore

        else:
            maxScore = 1000
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = player
                    score = self.minimax(self, computer,player, board, limit-1, maximum, winningletter, checkdraw)
                    board[key] = ' '
                    if score < maxScore:
                        maxScore = min(maxScore,score)

            return maxScore
