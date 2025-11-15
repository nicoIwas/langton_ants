# @nicoiwas
###################################
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from ant import Ant
###################################

class Map:

    def __init__(self, ant: Ant, rows: int = 500, columns: int = 500):

        self.rows = rows
        self.columns = columns
        self.anthill = np.zeros((self.rows, self.columns))
        self.ant = ant
    
    def update_ant(self, value: int) -> None:

        self.anthill[self.ant.position[0]][self.ant.position[1]] = value
    
    def get_ant_position(self) -> int:
        
        return self.anthill[self.ant.position[0]][self.ant.position[1]]
    
    def simulate(self, steps: int = 1, debug: bool = False) -> None:

        # cores dos pontos: 0 / 1 / formiga
        colors = ["black", "white", "red"]
        # intervalos de cores (respectivamente)
        boundaries = [-0.5, 0.5, 1.5, 2.5]
        # linkando o colormap
        cmap = mcolors.ListedColormap(colors)
        norm = mcolors.BoundaryNorm(boundaries, cmap.N)

        fig, ax = plt.subplots() # type: ignore

        
        self.update_ant(2)
        
        mat_display = ax.matshow(self.anthill, cmap=cmap, norm=norm) # type: ignore
        
        plt.ion() # type: ignore
        plt.show() # type: ignore
        
        self.update_ant(self.ant.current_square)


        i = 0
        while True:
            try:

                if self.get_ant_position() == 0:
                    self.update_ant(1)
                    self.ant.move("l")

                elif self.get_ant_position() == 1:
                    self.update_ant(0)
                    self.ant.move("r")

                self.ant.correct_position(self.anthill)
                self.ant.current_square = self.get_ant_position()
                self.update_ant(2)

                if i % steps == 0:
                    mat_display.set_data(self.anthill)
                    fig.canvas.draw_idle() # type: ignore
                    plt.pause(0.01)

                self.anthill[self.ant.position[0], self.ant.position[1]] = self.ant.current_square

                # debug
                if debug:
                    print(i)
                    i += 1
            
            except KeyboardInterrupt:  
                plt.ioff() # type: ignore
                break
        plt.pause(1)
        plt.close()