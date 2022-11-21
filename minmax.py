"""
minimax class to house the main algorithms and functions used for minimax algorithm
"""


class MinImax:
    def minimax(self, board, depth, maxplayer):
        from game import TicTacToe  # imported in the class to avoid Python ImportError for partially init. module
        ttt = TicTacToe(board)
        draw = ttt.check_draw()
        # score system based off who won or if there was a draw
        if ttt.winning_letter('x'):  # ai
            return 1

        elif ttt.winning_letter('o'):  # player
            return -1

        elif draw:
            return 0
        # Returns optimal value for current player
        if maxplayer:  # for computer- AI x
            maxScore = -100  # arbitrary number used for maximizing
            for key in board.keys():  # loops to keep track of best score for next move
                if board[key] == ' ':  # so for every key or location on the board
                    board[key] = 'x'  # marks the AI move
                    bestscore = self.minimax(board, depth + 1, False)  # recurse for the score and store
                    board[key] = ' '  # undo the move
                    maxScore = max(maxScore, bestscore)
            return maxScore # returns the optimal score

        else:  # If this the min player - HUMAN o
            maxScore = 100  # arbitrary number used for min
            for key in board.keys(): # loops to keep track of best score for next move
                if board[key] == ' ':  # if there is an empty spot
                    board[key] = 'o'  # marks the players move
                    bestscore = self.minimax(board, depth + 1, True)  # recurse for the score and store
                    board[key] = ' '  # undo the move
                    maxScore = min(maxScore, bestscore)  # and take the min from the comparison
            return maxScore # returns the optimal score

    # method which returns the optimal move for a player depending on the current state of the board
    def mm_optimalMove(self, board):
        maxscore = 100  # -100 for x
        bestscore = 0
        # print("Min max optimal move:")
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'o'  # or x
                score = self.minimax(board, 0, True)  # false for x
                board[key] = ' '
                if score < maxscore:  # score > maxscore for x optimize
                    maxscore = score
                    bestscore = key
        return bestscore
