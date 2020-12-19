"""
File:         board_square_hw.py
Author:       Vu Nguyen
Date:         11/6/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Modify the can_move method so it can return
              True or False.
"""


class UrPiece:
    WHITE = 'White'
    BLACK = 'Black'
    OFF_BOARD_MOVE = 1
    CANT_MOVE = 0

    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol
        self.StartPos = None
        self.exit_pos = None

    def can_move(self, num_moves, the_board):

        if num_moves == self.CANT_MOVE:
            return False
        else:

            # This loop find which board_square is the piece is currently on
            for row in the_board:
                for board_square in row:

                    # This condition checks if the piece is on the board
                    if self.position == board_square:
                        check_position = self.position
                        if self.color == self.WHITE:

                            # This loop checks position for white piece
                            for steps in range(num_moves):
                                if check_position == self.exit_pos:

                                    # This function checks for exiting position for white
                                    if num_moves - steps > self.OFF_BOARD_MOVE:
                                        return False
                                    else:
                                        return True
                                else:
                                    check_position = check_position.next_white

                            # This call function to check the square for pieces and rosette
                            if self.checking_square(check_position):
                                return True
                            else:
                                return False

                        elif self.color == self.BLACK:

                            # This loop checks position for black piece
                            for steps in range(num_moves):
                                if check_position == self.exit_pos:

                                    # This function checks for exiting position for black
                                    if num_moves - steps == self.OFF_BOARD_MOVE:
                                        return True
                                    else:
                                        return False
                                else:
                                    check_position = check_position.next_black

                            # This call function to check the square for pieces and rosette
                            if self.checking_square(check_position):
                                return True
                            else:
                                return False
                    # This condition checks if the piece is off the board and haven't completed the game for white.
                    elif not self.position and board_square.entrance == self.WHITE:
                        check_position = board_square

                        # This loop find the new position to checks for off board white piece
                        for steps in range(num_moves - self.OFF_BOARD_MOVE):
                            if check_position == self.exit_pos:

                                # This function checks for exiting position for white
                                if (num_moves - self.OFF_BOARD_MOVE) - steps == self.OFF_BOARD_MOVE:
                                    return True
                                else:
                                    return False
                            else:
                                check_position = check_position.next_white

                        # This call function to check the square for pieces and rosette
                        if self.checking_square(check_position):
                            return True
                        else:
                            return False

                    # This condition checks if the piece is off the board and haven't completed the game for black.
                    elif not self.position and board_square.entrance == self.BLACK:
                        check_position = board_square

                        # This loop find the new position to checks for off board black piece
                        for steps in range(num_moves - self.OFF_BOARD_MOVE):
                            if check_position == self.exit_pos:

                                # This function checks for exiting position for white
                                if (num_moves - self.OFF_BOARD_MOVE) - steps == self.OFF_BOARD_MOVE:
                                    return True
                                else:
                                    return False
                            else:
                                check_position = check_position.next_black

                        # This call function to check the square for pieces and rosette
                        if self.checking_square(check_position):
                            return True
                        else:
                            return False

    def checking_square(self, check_position):
        """
        This helper function check whether the new position is empty, different color pieces
        or no rosette square occupied by the different pieces.
        :param check_position: The Board Square that the piece suppose to go on
        :return: Either True or False
        """
        if not check_position.piece:
            return True
        else:
            if check_position.piece.color != self.color and not check_position.resette:
                return True
            else:
                return False


class BoardSquare:
    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit,
                'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}
