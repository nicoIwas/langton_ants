# @nicoiwas
##########################
from abc import ABC, abstractmethod
from typing import Literal
import numpy as np
from src.ants.State import State
##########################

class Ant(ABC):

    def __init__(self, starting_position: tuple[int, int] = (0, 0), starting_direction: Literal["R", "L", "U", "D"] = "R", current_square: int = 0, state: State = {0: {"turn": "l", "next_state": 1}}):

        self.position: tuple[int, int] = starting_position
        self.direction = starting_direction
        self.color = None

        self.state = state
        # self.current_position: int = current_square
        # self.state: list[Literal["R", "L", "U", "D"]] = state
        # self.current_state_index = 0

        
    def move(self) -> None:

        move_direction: list[Literal["R", "L", "U", "D"]] = self.state

        match move_direction:

            case "L":
                self.move_left()
            
            case "R": 
                self.move_right()
            
            case "U": 
                self.move_up()
            
            case "D": 
                self.move_down()

        
    def move_up(self) -> None:

        x: int = self.position[0]
        y: int = self.position[1]

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

        x: int = self.position[0]
        y: int = self.position[1]

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

        x: int = self.position[0]
        y: int = self.position[1]

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

        x: int = self.position[0]
        y: int = self.position[1]

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

        x_position = self.position[0]
        y_position = self.position[1]

        # verifying x position to see if it checks on the necessary conditions
        if x_position < 0 or x_position >= x_dimension:
            self.position = (x_dimension - abs(x_position), y_position)

        # verifying y position to see if it checks on the necessary steps
        if y_position < 0 or y_position >= y_dimension:
            self.position = (x_position, y_dimension - abs(y_position))
