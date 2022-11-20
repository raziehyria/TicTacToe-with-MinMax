"""
minimax class to house the main algorithms and functions used for minimax algorithm
"""


class MinImax:
    def minimax(self, board, depth, maxplayer):
        from game import TicTacToe
        ttt = TicTacToe(board)
        draw = ttt.check_draw()

        if ttt.winning_letter('x'):  # ai
            return 1

        elif ttt.winning_letter('o'):  # player
            return -1

        elif draw:
            return 0

        if maxplayer:
            maxScore = -100
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'x'
                    bestscore = self.minimax(board, depth + 1, False)
                    board[key] = ' '
                    maxScore = max(maxScore, bestscore)
            return maxScore

        else:
            maxScore = 100
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'o'
                    bestscore = self.minimax(board, depth + 1, True)
                    board[key] = ' '
                    maxScore = min(maxScore, bestscore)
            return maxScore

    def mm_optimalMove(self, board):
        maxscore = -100
        bestscore = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'o'
                move = self.minimax(board, 0, False)
                board[key] = ' '
                if move > maxscore:
                    bestscore = key
                    maxscore = move
        return bestscore
