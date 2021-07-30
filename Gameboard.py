import Player
import printpawn
from Piece import Piece

pieces = Piece()


# kid = "  K  "
# defender = "  D  "
# thief = "  X  "
# empty = "     "


class Gameboard:
    # initializes the array containing the positions
    def __init__(self, player_1, player_2):
        self.game_board = [[pieces.empty for _ in range(11)] for _ in range(11)]

        # top row pieces
        self.game_board[0][3] = pieces.defender
        self.game_board[0][4] = pieces.defender
        self.game_board[0][5] = pieces.defender
        self.game_board[0][6] = pieces.defender
        self.game_board[0][7] = pieces.defender

        # last row pieces
        self.game_board[10][3] = pieces.defender
        self.game_board[10][4] = pieces.defender
        self.game_board[10][5] = pieces.defender
        self.game_board[10][6] = pieces.defender
        self.game_board[10][7] = pieces.defender

        # second/second last row pieces
        self.game_board[1][5] = pieces.defender
        self.game_board[9][5] = pieces.defender

        # first column pieces
        self.game_board[3][0] = pieces.defender
        self.game_board[4][0] = pieces.defender
        self.game_board[5][0] = pieces.defender
        self.game_board[6][0] = pieces.defender
        self.game_board[7][0] = pieces.defender

        # last column pieces
        self.game_board[3][10] = pieces.defender
        self.game_board[4][10] = pieces.defender
        self.game_board[5][10] = pieces.defender
        self.game_board[6][10] = pieces.defender
        self.game_board[7][10] = pieces.defender

        # second/second last row pieces
        self.game_board[5][1] = pieces.defender
        self.game_board[5][9] = pieces.defender

        # thief
        self.game_board[5][5] = pieces.thief

        # middle pieces kids
        self.game_board[3][5] = pieces.kid
        self.game_board[4][5] = pieces.kid
        self.game_board[6][5] = pieces.kid
        self.game_board[7][5] = pieces.kid

        self.game_board[5][3] = pieces.kid
        self.game_board[5][4] = pieces.kid
        self.game_board[5][6] = pieces.kid
        self.game_board[5][7] = pieces.kid

        self.game_board[4][4] = pieces.kid
        self.game_board[4][6] = pieces.kid
        self.game_board[6][4] = pieces.kid
        self.game_board[6][6] = pieces.kid

        self.player1 = player_1
        self.player2 = player_2

    # returns the array containing the positions of the pieces
    def getGameboard(self):
        return self.game_board

    # Move piece at row_x1, column_y1 to row_x2, column_y2. Function args must be ints
    # Diagonal moves are invalid. Indices must be within board length
    # TODO: Check for diagonal moves for thief, check for length of move for thief, \
    #  check for empty paths, check for player moving only their pieces
    def move_piece(self, x1, y1, x2, y2):
        prev_pos = self.game_board[x1][y1]
        next_pos = self.game_board[x2][y2]

        if x1 < 0 or x1 > 10 or x2 < 0 or x2 > 10 or y1 < 0 or y1 > 10 or y2 < 0 or y2 > 10:
            print("Invalid starting position inputted. Move not possible")
        elif prev_pos is pieces.empty:
            print("No piece selected")
        elif next_pos is not pieces.empty:
            print("Cannot move piece to the inputted position")
        elif x1 - x2 != 0 and y1 - y2 != 0:
            print("Invalid move. Only horizontal and vertical moves allowed")
        elif prev_pos is not pieces.empty and next_pos is pieces.empty:
            self.game_board[x2][y2] = prev_pos
            self.game_board[x1][y1] = pieces.empty

    # returns 0 if players can do moves again
    # returns 1 if it's a draw
    def isgamefinished(self):
        if self.player1.getNbMoves() == 250 and self.player2.getNbMoves() == 250:
            return 1
        else:
            return 0

    # print the gameboard
    def printBoard(self):
        print("    1   |    2   |    3   |    4   |    5   |    6   |    7   |    8   |    9   |   10   |   11   |")
        for i in range(0, 11):
            print("-" * 99)
            print(chr(i + 97), end="|")
            for j in range(0, 11):
                item = self.game_board[i][j]
                printpawn.printpawn_board(str(item))
                print(' |', end="  ")
            print()
        print("-" * 99)
