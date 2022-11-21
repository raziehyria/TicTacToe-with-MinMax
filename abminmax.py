'''minimax class to house the main algorithms and functions used for minimax algorithm'''


class ABMinmax:
    # It stops evaluating a move when it makes sure that it's worse than previously examined move.
    def abminimax(self, board, depth, maxplayer, alpha, beta):
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
        if maxplayer:  # for AI optimization
            maxScore = -100  # arbitrary max score for neg inf

            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'x'  # mark empty field with it's move
                    bestscore = self.abminimax(board, depth + 1, False, alpha, beta)  # recurse for the score and store
                    maxScore = max(maxScore, bestscore)
                    alpha = max(alpha, bestscore)  # Best already explored option for player Max
                    board[key] = ' '  # undo move
                    if beta <= alpha: # cut off all the other children of the node we're at.
                        break
            return maxScore  # returns the optimal score

        else:
            maxScore = 100  # the arbitrary max score for pos inf
            for key in board.keys():  # for Player optimization
                if board[key] == ' ':
                    board[key] = 'o'  # mark empty field with it's move
                    bestscore = self.abminimax(board, depth + 1, True, alpha, beta)  # recurse for the score and store
                    maxScore = min(maxScore, bestscore)  # take the smallest of the comparison
                    beta = min(beta, maxScore)  # Best already explored option for player Min
                    board[key] = ' '  # undo move
                    if beta <= alpha:  # cut off all the other children of the node we're at.
                        break
            return maxScore  # returns the optimal score

    # method which returns the optimal move for a player depending on the current state of the board
    def ab_optimalMove(self, board):
        maxscore = -100
        alpha = -10
        beta = 10
        bestscore = 0
        # print("Alpha Beta optimal move:")
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'x'  # mark empty field with it's move
                score = self.abminimax(board, 0, False, alpha, beta)  # recurse for the score and store
                board[key] = ' '
                if score > maxscore:
                    maxscore = score
                    bestscore = key  # the optimized key with greatest value gets returned
        return bestscore  # returns the optimal score
