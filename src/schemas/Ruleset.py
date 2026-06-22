# @nicoiwas
##########################
from typing import Literal, TypedDict
##########################

class Rule(TypedDict):
    
    turn: Literal["R", "L", "U", "D"]
    color_change: int

class Ruleset(TypedDict):
    ant_color: int
    current_color: dict[int, Rule]

