# @nicoiwas
##########################
from abc import ABC
from typing import Literal
import numpy as np
from src.ants.schemas.Ruleset import Ruleset, Rule
##########################

class Ant(ABC):

    def __init__(self, 
                starting_position: tuple[int, int] = (0, 0), 
                starting_direction: Literal["R", "L", "U", "D"] = "R", 
                # current_square: int = 0, 
                ruleset: Ruleset = Ruleset(current_color={0: Rule(turn="L", color_change=1), 1: Rule(turn="R", color_change=0)})
    ):

        self.position: tuple[int, int] = starting_position
        self.direction: Literal["R", "L", "U", "D"] = starting_direction
        # self.color = 2
        self.ruleset: Ruleset = ruleset
        self.current_square: int = 0 # current_square
        self.color_buffer: int = 0

    def move(self) -> int:

        move_direction: Literal["R", "L", "U", "D"] = self.ruleset["current_color"][self.current_square]["turn"]

        match move_direction:

            case "L":
                self.move_left()
            
            case "R": 
                self.move_right()
            
            case "U": 
                self.move_up()
            
            case "D": 
                self.move_down()

        return self.ruleset["current_color"][self.current_square]["color_change"]
 
    def move_up(self) -> None:

        x, y = self.position

        match self.direction:

            case "L":
                self.position = (x - 1, y)
                self.direction = "L"

            case "R":
                self.position = (x + 1, y)
                self.direction = "R"

            case "U":
                self.position = (x, y + 1)
                self.direction = "U"

            case "D":
                self.position = (x , y - 1)
                self.direction = "D"
    
    def move_down(self) -> None:

        x, y = self.position

        match self.direction:

            case "L":
                self.position = (x + 1, y)
                self.direction = "R"

            case "R":
                self.position = (x - 1, y)
                self.direction = "L"

            case "U":
                self.position = (x, y - 1)
                self.direction = "D"

            case "D":
                self.position = (x , y + 1)
                self.direction = "U"

    def move_left(self) -> None:

        x, y = self.position

        match self.direction:

            case "L":
                self.position = (x, y - 1)
                self.direction = "D"

            case "R":
                self.position = (x, y + 1)
                self.direction = "U"

            case "U":
                self.position = (x - 1, y)
                self.direction = "L"

            case "D":
                self.position = (x + 1, y)
                self.direction = "R"

    def move_right(self) -> None:

        x, y = self.position

        match self.direction:

            case "L":
                self.position = (x, y + 1)
                self.direction = "U"

            case "R":
                self.position = (x, y - 1)
                self.direction = "D"

            case "U":
                self.position = (x + 1, y)
                self.direction = "R"

            case "D":
                self.position = (x - 1, y)
                self.direction = "L"

    # this basically exists so the ant can go in 'loops' on the lattice
    def correct_position(self, anthill: np.ndarray) -> None:

        x_dimension = len(anthill[0])
        y_dimension = len(anthill)

        x_position, y_position = self.position

        # verifying x position to see if it checks on the necessary conditions
        if x_position < 0 or x_position >= x_dimension:
            self.position = (x_dimension - abs(x_position), y_position)

        # verifying y position to see if it checks on the necessary steps
        if y_position < 0 or y_position >= y_dimension:
            self.position = (x_position, y_dimension - abs(y_position))
