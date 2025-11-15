# @nicoiwas
####################
from grid import Map
from ant import Ant
####################

if __name__ == "__main__":

    ant = Ant((125, 125))
    anthill = Map(ant, 250, 250)
    anthill.simulate(steps=500, debug=True)
