from Gameboard import Gameboard
from Player import Player


class GameSession:
    def __init__(self):
        self.white = Player()
        self.black = Player()
        self.session = Gameboard(self.white, self.black)

    def start_game(self):
        self.session.printBoard()

        # TODO: Clear screen after each print of board?
        x1, y1, x2, y2 = self.get_player_input()
        self.session.move_piece(x1, y1, x2, y2)

        self.session.printBoard()

    def get_player_input(self):
        prev_pos = input("Enter position of piece to move. Please enter letter and number of position: ")
        next_pos = input("Enter position to move to piece to. Please enter letter and number of position: ")

        # Map user input to array indices
        input_mappings = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                          "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "11": 10}

        x_1, y_1 = prev_pos[:1], prev_pos[1:]
        x_2, y_2 = next_pos[:1], next_pos[1:]

        upper_x_1 = x_1.upper()
        upper_x_2 = x_2.upper()

        if upper_x_1 not in input_mappings or y_1 not in input_mappings:
            print("Valid piece position not selected")
        elif upper_x_2 not in input_mappings or y_2 not in input_mappings:
            print("Cannot move piece to inputted position. Please enter a valid position")
        else:
            return input_mappings[x_1.upper()], input_mappings[y_1], input_mappings[x_2.upper()], \
                   input_mappings[y_2]
