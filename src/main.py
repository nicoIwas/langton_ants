# @nicoiwas
####################
from Grid import Grid
from Ant import Ant
####################

if __name__ == "__main__":

    ant_1 = Ant((57, 119), "r")
    ant_2 = Ant((57, 120), "r")
    anthill = Grid([ant_1, ant_2], 116, 240)
    anthill.simulate(steps=100, debug=True)
