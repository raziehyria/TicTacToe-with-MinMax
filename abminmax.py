'''minimax class to house the main algorithms and functions used for minimax algorithm'''


class ABMinmax:

    def abminimax(self, board, depth, maxplayer, alpha, beta):
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
                    bestscore = self.abminimax(board, depth + 1, False, alpha, beta)
                    maxScore = max(maxScore, bestscore)
                    alpha = max(alpha, bestscore)
                    board[key] = ' '
                    if beta <= alpha:
                        break
            return maxScore

        else:
            maxScore = 100
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'o'
                    bestscore = self.abminimax(board, depth + 1, True, alpha, beta)
                    maxScore = min(maxScore, bestscore)
                    beta = min(beta, maxScore)
                    board[key] = ' '
                    if beta <= alpha:
                        break
            return maxScore

    def ab_optimalMove(self, board):
        maxscore = -100
        alpha = -10
        beta = 10
        bestscore = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'o'
                move = self.abminimax(board, 0, False, alpha, beta)
                board[key] = ' '
                if move > maxscore:
                    bestscore = key
                    maxscore = move
        return bestscore
