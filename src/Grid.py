# @nicoiwas
###################################
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from Ant import Ant
###################################

class Grid:

    def __init__(self, ant_list: list[Ant], rows: int = 500, columns: int = 500):

        self.anthill = np.zeros((rows, columns))
        self.ant_list = ant_list
    
    def update_ant(self, value: int, index: int) -> None:

        self.anthill[self.ant_list[index].position[0]][self.ant_list[index].position[1]] = value
    
    def get_ant_position(self, index: int) -> int:
        
        return self.anthill[self.ant_list[index].position[0]][self.ant_list[index].position[1]]
    
    def simulate(self, steps: int = 1, debug: bool = False) -> None:

        # cores dos pontos: 0 / 1 / formiga
        colors = ["black", "white", "red"]
        # intervalos de cores (respectivamente)
        boundaries = [-0.5, 0.5, 1.5, 2.5]
        # linkando o colormap
        cmap = mcolors.ListedColormap(colors)
        norm = mcolors.BoundaryNorm(boundaries, cmap.N)

        fig, ax = plt.subplots() # type: ignore

        for i in range(len(self.ant_list)):
            self.update_ant(2, i)
        
        mat_display = ax.matshow(self.anthill, cmap=cmap, norm=norm) # type: ignore
        
        plt.ion() # type: ignore
        plt.show() # type: ignore
        
        for i in range(len(self.ant_list)):
            self.update_ant(self.ant_list[i].current_square, i)


        index = 0
        while True:
            try:
                
                for i in range(len(self.ant_list)):
                    
                    if self.get_ant_position(i) == 0:
                        self.update_ant(1, i)
                        self.ant_list[i].move_buffer = "l"

                    elif self.get_ant_position(i) == 1:
                        self.update_ant(0, i)
                        self.ant_list[i].move_buffer = "r"
                    
                
                for i in range(len(self.ant_list)):
                    self.ant_list[i].move(self.ant_list[i].move_buffer)
                
                for i in range(len(self.ant_list)):
                    #####
                    self.ant_list[i].correct_position(self.anthill)
                    self.ant_list[i].current_square = self.get_ant_position(i)
                    self.update_ant(2, i)

                if index % steps == 0:
                    mat_display.set_data(self.anthill)
                    fig.canvas.draw_idle() # type: ignore
                    plt.pause(0.01)
                
                for i in range(len(self.ant_list)):
                    self.anthill[self.ant_list[i].position[0], self.ant_list[i].position[1]] = self.ant_list[i].current_square

                # debug
                if debug:
                    print(index)
                index += 1
            
            except KeyboardInterrupt:  
                plt.ioff() # type: ignore
                break
        plt.pause(1)
        plt.close()
