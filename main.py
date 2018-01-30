# an unusual form of tictactoe
#
# @author Andre
# @email potato@desu.zone

# input args
import argparse

parser = argparse.ArgumentParser(
    description=(
        "Unusal Tic Tac Toe. Piece insertion is handled with some odds-based" +
        "mechanic that allows for some randomness."
    )
)
parser.add_argument(
    "odds_you", 
    metavar="N", 
    type=int, 
    default=50,
    help=(
        "the odds that your piece will actually appear when you select a " +
        "spot. Must be <= 100"
    )
)

args = parser.parse_args()

if args.odds_you > 100:
    print("Odds must be <= 100")
    exit(0)

# getting the board
import board

# turn states
STATE_O = 0
STATE_X = 1

def turn(t_board, piece):
    """
    Does a game turn

    IN:
        t_board - the tictactoe board
        piece - the current piece turn

    RETURNS: a tuple of the following format:
        [0] - True if this piece won, False if not, None if no winners
        [1] - the current piece, None if no winners
    """

    # now prompt for user input
    good_input = False
    user_sel = None
    while not good_input:
        # first, display the boards
        print("BOARD:\n\n{0}\n\nInput map:\n".format(str(t_board)))
        t_board.showBoard()
        print("\n")

        # then prompt
        user_sel = input("Enter (1-9) for {0}, or 0 to lose: ".format(piece))

        if len(user_sel) == 1 and "0" <= user_sel <= "9":
            user_sel = int(user_sel)

            # losing
            if user_sel == 0:
                return (False, piece)

            # otherwise, check for valid piece insert
            if t_board.insertPiece(piece, user_sel):
                good_input = True
            else:
                print("spot taken")

        else:
            print("Invalid selection")

    # otherwise good selection, check win
    win_piece = t_board.checkWin()

    if win_piece:
        return (win_piece == piece, piece)

    # otherwise, check if board is full
    if t_board.checkFull():
        return (None, None)

    return (None, piece)
    
# begin main flow
no_quit = True
the_board = board.Board(args.odds_you, 100-args.odds_you)
state = STATE_X
winner = None
while no_quit:

    # turn piece checking
    if state == STATE_X:
        curr_piece = board.Board.X
    else:
        curr_piece = board.Board.O

    # now do a turn
    results = turn(the_board, curr_piece)

    # check results
    if results[0] is not None:
        # we have a winner or loser

        # curernt piece is winner
        if results[0]:
            winner = results[1]

        # other piece is winner
        elif results[1] == board.Board.X:
            winner = board.Board.O
        else:
            winner = board.Board.X

        no_quit = False

    # check for no winner
    elif results[1] is None:
        no_quit = False

    # otherwise switch state
    else:
        state = (state+1) % 2

# print winner
print("\n\nBOARD:\n\n{0}\n".format(str(the_board)))
if winner:
    print("'{0}' is winner!".format(winner))
else:
    print("no winner")
