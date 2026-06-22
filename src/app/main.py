# @nicoiwas
####################
from src.grid.Grid import Grid
from src.agents.Ant import Ant
####################

if __name__ == "__main__":

    # ant_1 = Ant((85, 53), "R")
    ant_1 = Ant((191, 161), "R", ruleset="src/models/ant.json")
    ant_2 = Ant((384, 161), "R", ruleset="src/models/tna.json")

    anthill = Grid([ant_1, ant_2], 576, 324)
    # anthill = Grid([ant_1], 192, 108)
    anthill.simulate(steps=100, debug=False)
