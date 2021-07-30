class Player:
    def __init__(self):
        self._nb_moves = 0
        self.captured = 0

    # increments by 1 the number of moves made by the player
    def addMove(self):
        self._nb_moves += 1

    # returns the number of moves
    def getNbMoves(self):
        return self._nb_moves

    # increases the number of pieces captured by 1
    def addCaptured(self):
        self.captured += 1

    # returns the number of pieces captured
    def getNbCaptured(self):
        return self.captured
