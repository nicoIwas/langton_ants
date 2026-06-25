# @nicoiwas
##############################
from src.grid.Grid import Grid
from src.agents.Ant import Ant
##############################

if __name__ == "__main__":

    ant_1 = Ant((191, 161), "R", ruleset="src/models/ant.json")
    ant_2 = Ant((192, 161), "R", ruleset="src/models/tna.json")
    ant_3 = Ant((193, 161), "R", ruleset="src/models/tna.json")
    ant_4 = Ant((194, 161), "R", ruleset="src/models/tna.json")
    ant_5 = Ant((195, 161), "R", ruleset="src/models/tna.json")

    anthill = Grid([ant_1, ant_2, ant_3, ant_4, ant_5], 576, 324)
    anthill.simulate(steps=100, debug=False)
