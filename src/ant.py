# @nicoiwas
##########################
from typing import Literal
##########################

class Ant:

    def __init__(self, starting_position: tuple[int, int] = (0, 0), starting_direction: Literal["r", "l", "u", "d"] = "r", current_square: int = 0):

        self.position = starting_position
        self.direction = starting_direction
        self.current_square = current_square

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

        if self.position[0]             
        
