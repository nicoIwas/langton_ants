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
                        self.position = (self.position[0] - 1, self.position[1])
                        self.direction = "d"
                    case "r":  # turn right, move up
                        self.position = (self.position[0] + 1, self.position[1])
                        self.direction = "u"
            case "r":
                match move_direction:
                    case "l":  # turn left, move up
                        self.position = (self.position[0] + 1, self.position[1])
                        self.direction = "u"
                    case "r":  # move forward (right)
                        self.position = (self.position[0] - 1, self.position[1])
                        self.direction = "d"
            case "u":
                match move_direction:
                    case "l":  # turn left, move left
                        self.position = (self.position[0], self.position[1]-1)
                        self.direction = "l"
                    case "r":  # move forward (up)
                        self.position = (self.position[0], self.position[1] + 1)
                        self.direction = "r"
            case "d":
                match move_direction:
                    case "l":  # turn left, move right
                        self.position = (self.position[0], self.position[1] + 1)
                        self.direction = "r"
                    case "r":  # move forward (down)
                        self.position = (self.position[0], self.position[1] - 1)
                        self.direction = "l"
            case _:
                pass        

    def correct_position(self, anthill: np.ndarray) -> None:

        x_dimension = len(anthill)
        y_dimension = len(anthill[0])
        for idx in range(2):
            if self.position[idx] < 0:
                self.position = (len(anthill) + self.position[idx], self.position[1]) if idx == 0 else (self.position[0], len(anthill[idx]) + self.position[idx])
            
            elif (self.position[idx] >= x_dimension and idx == 0) or (self.position[idx] >= y_dimension and idx == 1):
                self.position = (self.position[idx] - len(anthill), self.position[1]) if idx == 0 else (self.position[0], self.position[idx] - len(anthill))
