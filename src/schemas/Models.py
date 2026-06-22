# @nicoiwas
##########################
from typing import Literal, TypedDict
##########################

class ModelRule(TypedDict):
    color_source: int
    turn: Literal["R", "L", "U", "D"]
    color_change: int

class Model(TypedDict):
    color: int
    rules: list[ModelRule]
