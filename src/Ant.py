# @nicoiwas
##########################
from typing import Literal
import numpy as np
##########################

class Ant:

    def __init__(self, starting_position: tuple[int, int] = (0, 0), starting_direction: Literal["r", "l", "u", "d"] = "r", current_square: int = 0):

        self.position = starting_position
        self.direction = starting_direction
        self.current_square = current_square
        self.move_buffer: Literal["l", "r"] = "l"

    def move(self, move_direction: Literal["l", "r"]) -> None:

        match self.direction:
            case "l":
                match move_direction:
                    case "l":  # move forward (left)
                        self.position = (self.position[0], self.position[1] - 1)
                        self.direction = "d"
                    case "r":  # turn right, move up
                        self.position = (self.position[0], self.position[1] + 1)
                        self.direction = "u"
            case "r":
                match move_direction:
                    case "l":  # turn left, move up
                        self.position = (self.position[0], self.position[1] + 1)
                        self.direction = "u"
                    case "r":  # move forward (right)
                        self.position = (self.position[0], self.position[1] - 1)
                        self.direction = "d"
            case "u":
                match move_direction:
                    case "l":  # turn left, move left
                        self.position = (self.position[0] - 1, self.position[1])
                        self.direction = "l"
                    case "r":  # move forward (up)
                        self.position = (self.position[0] + 1, self.position[1])
                        self.direction = "r"
            case "d":
                match move_direction:
                    case "l":  # turn left, move right
                        self.position = (self.position[0] + 1, self.position[1])
                        self.direction = "r"
                    case "r":  # move forward (down)
                        self.position = (self.position[0] - 1, self.position[1])
                        self.direction = "l"
            case _:
                pass        

    def correct_position(self, anthill: np.ndarray) -> None:

        x_dimension = len(anthill[0])
        y_dimension = len(anthill)

        x_position = self.position[0]
        y_position = self.position[1]

        # verifying x position to see if it checks on the necessary conditions
        if x_position < 0 or x_position >= x_dimension:
            self.position = (x_dimension - abs(x_position), y_position)

        # verifying y position to see if it checks on the necessary steps
        if y_position < 0 or y_position >= y_dimension:
            self.position = (x_position, y_dimension - abs(y_position))
