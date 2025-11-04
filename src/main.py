# @nicoiwas
####################
from grid import Map
from ant import Ant
####################

if __name__ == "__main__":


    anthill = Map(Ant((125, 125)), 250, 250)
    anthill.simulate(steps=1000, debug=True)
