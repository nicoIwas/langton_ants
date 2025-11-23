# @nicoiwas
####################
from Grid import Grid
from Ant import Ant
####################

if __name__ == "__main__":

    ant_1 = Ant((119, 57), "r")
    ant_2 = Ant((120, 57), "r")
    ant_3 = Ant((121, 57), "r")
    anthill = Grid([ant_1, ant_2, ant_3], 240, 116)
    anthill.simulate(steps=1, debug=True)
