# @nicoiwas
###################################
from ty_extensions import Unknown
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from src.ants.Ant import Ant
###################################

class Grid:

    def __init__(self, ant_list: list[Ant], columns: int = 500, rows: int = 500):

        # map itself (anthill... get it?)
        self._anthill: np.ndarray[tuple[int, int], np.dtype[np.float64]] = np.zeros(shape=(rows, columns))
        # the possibility of having the ants as a map for the grid to iterate on makes it easier to deal with everything
        self.ant_list: list[Ant] = ant_list
    
    @property
    def anthill(self) -> np.ndarray:
        return self._anthill

    def __getitem__(self, position: tuple[int, int]) -> int:

        x, y = position
        return self._anthill[y, x]

    def __setitem__(self, position: tuple[int, int], value: int) -> None:

        x, y = position
        self._anthill[y, x] = value

    def update_ant_position(self, value: int | None = None, index: int = 0) -> None:

        self.anthill[self.ant_list[index].position[0]][self.ant_list[index].position[1]] = self.ant_list[index].collor_buffer
    
    def get_ant_position(self, index: int) -> int:
        
        return self.anthill[self.ant_list[index].position[0]][self.ant_list[index].position[1]]
    
    def simulate(self, steps: int = 1, debug: bool = False) -> None:

        # cores dos pontos: 0 / 1 / formiga
        colors = ["white", "black", "red"]
        # intervalos de cores (respectivamente)
        boundaries = [-0.5, 0.5, 1.5, 2.5]
        
        # linkando o colormap
        cmap = mcolors.ListedColormap(colors)
        norm = mcolors.BoundaryNorm(boundaries, ncolors=cmap.N)

        fig, ax = plt.subplots() 

        for i in range(len(self.ant_list)):
            self.update_ant_position(2, i)
        
        # rework is actually on the way
        mat_display = ax.matshow(self.anthill, cmap=cmap, norm=norm)
        
        plt.ion()
        plt.show()
        
        for i in range(len(self.ant_list)):
            self.update_ant_position(self.ant_list[i].current_position, i)


        index = 0
        while True:
            try:
                
                # now, each A(ge)NT will handle its own movement; it will only be passed as a parameter the current color
                for i in range(len(self.ant_list)):
                    
                    self.ant_list[i].collor_buffer = self.get_ant_position(i)
                    # : Unknown = current
                    # if self.get_ant_position(i) == 0:
                    #     self.update_ant_position(1, i)
                    #     self.ant_list[i].move_buffer = "l"

                    # elif self.get_ant_position(i) == 1:
                    #     self.update_ant_position(0, i)
                    #     self.ant_list[i].move_buffer = "r"
                    
                
                for i in range(len(self.ant_list)):
                    self.update_ant_position(index=i) # turn to it correct color
                    self.ant_list[i].move()
                
                for i in range(len(self.ant_list)):
                    #####
                    self.ant_list[i].correct_position(self.anthill)
                    self.ant_list[i].current_position: int = self.get_ant_position(index=i)
                
                for i in range(len(self.ant_list)):
                    self.update_ant_position(2, i)

                if index % steps == 0:
                    mat_display.set_data(self.anthill)
                    fig.canvas.draw_idle()
                    plt.pause(0.01)
                
                for i in range(len(self.ant_list)):
                    self.anthill[self.ant_list[i].position[1]][self.ant_list[i].position[0]] = self.ant_list[i].current_position

                # debug
                if debug:

                    print(index)
                    for agent in self.ant_list: print(agent.position)
                                    

                index += 1
            
            except KeyboardInterrupt:  
                plt.ioff()
                break
        plt.pause(1)
        plt.close()
