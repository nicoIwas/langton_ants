# @nicoiwas
##########################
from typing import Literal, TypedDict
##########################

class Rule(TypedDict):
    
    turn: Literal["R", "L", "U", "D"]
    next_state: int

class State(TypedDict):
    
    state: dict[int, Rule]
