from Piece import Piece


class Pcolors:
    DARK_GREY = '\033[1;30;40m'
    WHITE = '\033[1;37;40m'
    ENDC = '\033[0m'

    pieces = Piece()


def printpawn_board(paw):
    if paw == Pcolors.pieces.kid:
        print(Pcolors.WHITE + paw + Pcolors.ENDC, end="")

    elif paw == Pcolors.pieces.defender:
        print(Pcolors.DARK_GREY + paw + Pcolors.ENDC, end="")

    elif paw == Pcolors.pieces.thief:
        print(Pcolors.WHITE + paw + Pcolors.ENDC, end="")

    else:
        print(Pcolors.pieces.empty, end="")
