# @nicoiwas
####################
from src.grid.Grid import Grid
from src.ants.Ant import Ant
####################

if __name__ == "__main__":

    ant_1 = Ant((85, 53), "R")
    # ant_2 = Ant((120, 57), "r")
    # ant_3 = Ant((121, 57), "r")
    # anthill = Grid([ant_1, ant_2, ant_3], 240, 116)
    anthill = Grid([ant_1], 192, 108)
    anthill.simulate(steps=100, debug=False)
