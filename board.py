## representing the tic tac toe board and some other data
#
#

import random

# board class is what we use
class Board():
    """
    Handles the internal representation of the board as well as printing it out
    """

    # constants
    SPACE = " "
    X = "X"
    O = "O"
    WALL = "|"
    FLOOR = "-"

    BOARD = (
        "   {0} | {1} | {2}\n" +
        "  -----------\n" +
        "   {3} | {4} | {5}\n" +
        "  -----------\n" +
        "   {6} | {7} | {8}"
    )

    # diag checking
    DOWNTREND = (0,4,8)
    UPTREND = (6,4,2)

    def __init__(self, odds_you, odds_opp):
        """
        Constructor for the tic tac toe board
        ODDS assumed to be out of 100

        IN:
            odds_your - the odds your piece will appear
                Out of 100
            odds_opp - the odds your opponent's piece will appear
                Out of 100
        """

        # setting odds
        self.odds_you = odds_you
        self.odds_opp = odds_opp

        # the board internally
        self.display_board = list(range(1,10))
        self.internal_board = [self.SPACE] * 9

        # other setup
        random.seed()


    def __str__(self):
        """
        The string representation of the board is a nice one
        """
        return self.BOARD.format(*self.internal_board)


    def checkFull(self):
        """
        Checks if the board is full

        RETURNS:
            True if the board full, false otherwise
        """
        for spot in self.internal_board:
            if spot == self.SPACE:
                return False

        return True


    def checkRange(self, startdex, check_range):
        """
        Checks the spots in the given range if they are all the same char.
        The range is assumed to be the next spots to check

        IN:
            startdex - the starting location to check
            check_range - range of the next spots to check

        RETURNS:
            False if the spots are not all the same, True if all the same
        """
        curr_piece = self.internal_board[startdex]

        if curr_piece == self.SPACE:
            return False

        for index in check_range:
            if curr_piece != self.internal_board[index]:
                return False

        return True


    def checkWin(self):
        """
        Checks if a player won the game and returns the winning character

        RETURNS:
            the winning piece, or NOne if no winner
        """
        # first, lets check rows
        for row in range(0,3):
            rowdex = row*3
            if self.checkRange(rowdex, range(rowdex+1, rowdex+3)):
                return self.internal_board[rowdex]

        # now check columns
        for col in range(0,3):
            if self.checkRange(col, range(col+3, 9, 3)):
                return self.internal_board[col]

        # and then diags are special cases
        if self.checkRange(self.DOWNTREND[0], self.DOWNTREND[1:]):
            return self.internal_board[self.DOWNTREND[0]]
        if self.checkRange(self.UPTREND[0], self.UPTREND[1:]):
            return self.internal_board[self.UPTREND[0]]

        return None
    
    
    def insertPiece(self, piece, loc):
        """
        Inserts a piece onto the board on the given loc

        IN:
            piece - the character piece to insert
            loc - the location (1 through 9) to insert the piece

        RETURNS: True if the piece was inserted, False otherwise
        """
        if self.internal_board[loc-1] != self.SPACE:
            return False

        # otherwise its a valid location
        if random.randint(1, 100) <= self.odds_you:
            actual_piece = piece
        elif piece == self.X:
            actual_piece = self.O
        else:
            actual_piece = self.X

        # insert
        self.internal_board[loc-1] = actual_piece
        self.display_board[loc-1] = actual_piece
        return True


    def showBoard(self):
        """
        prints out the display board
        """
        print(self.BOARD.format(*self.display_board))
