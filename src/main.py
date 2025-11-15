# @nicoiwas
####################
from Grid import Grid
from Ant import Ant
####################

if __name__ == "__main__":

    ant = Ant((125, 125))
    anthill = Grid(ant, 250, 250)
    anthill.simulate(steps=125, debug=True)
