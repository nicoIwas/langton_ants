# @nicoiwas
###################################
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from src.ants.Ant import Ant
###################################

class Anthill:

    def __init__(self, columns: int = 500, rows: int = 500):
        # map itself (anthill... get it?)
        self._anthill: np.ndarray[tuple[int, int], np.dtype[np.float64]] = np.zeros(shape=(rows, columns))
        self.raw = self._anthill

    @property
    def anthill(self) -> np.ndarray:
        return self._anthill
    
    def __getitem__(self, position: tuple[int, int]) -> int:

        x, y = position
        return self._anthill[y, x]

    def __setitem__(self, position: tuple[int, int], value: int) -> None:

        x, y = position
        self._anthill[y, x] = value

class Grid:

    def __init__(self, ant_list: list[Ant], columns: int = 500, rows: int = 500):

        # map itself (anthill... get it?)
        self.anthill: Anthill = Anthill(columns, rows)
        # np.ndarray[tuple[int, int], np.dtype[np.float64]] = np.zeros(shape=(rows, columns))
        # the possibility of having the ants as a map for the grid to iterate on makes it easier to deal with everything
        self.ant_list: list[Ant] = ant_list

    def update_position(self,  x: int, y: int, value: int) -> None:
        
        self.anthill[x, y] = value

    def get_position(self,  x: int, y: int) -> int:
        
        return self.anthill[x, y]
    
    def simulate(self, steps: int = 1, debug: bool = False) -> None:

        # cores dos pontos: 0 / 1 / formiga
        colors = ["white", "black", "red"]
        # intervalos de cores (respectivamente)
        boundaries = [-0.5, 0.5, 1.5, 2.5]
        
        # linkando o colormap
        cmap = mcolors.ListedColormap(colors)
        norm = mcolors.BoundaryNorm(boundaries, ncolors=cmap.N)

        fig, ax = plt.subplots() 

        # update each ant position to its correspondent color
        for i in range(len(self.ant_list)):
            
            x, y = self.ant_list[i].position
            self.ant_list[i].current_square = self.get_position(x, y)

        # update each ant position to its correspondent color
        for i in range(len(self.ant_list)):
            x, y = self.ant_list[i].position
            self.update_position(x, y, value=2)
            
        
        # rework is actually on the way
        mat_display = ax.matshow(self.anthill.raw, cmap=cmap, norm=norm, origin='lower')
        
        plt.ion()
        plt.show()
        plt.pause(3)

        for i in range(len(self.ant_list)):

            x, y = self.ant_list[i].position

            self.update_position(x, y, self.ant_list[i].current_square)


        index = 0
        while True:
            try:
                # now, each A(ge)NT will handle its own movement;
                for i in range(len(self.ant_list)):
                    
                    x, y = self.ant_list[i].position
                    
                    self.ant_list[i].current_square = self.get_position(x, y)
                    
                    new_square_color = self.ant_list[i].move()
                    self.update_position(x, y, value=new_square_color)

                    self.ant_list[i].correct_position(self.anthill.raw)

                    new_x, new_y = self.ant_list[i].position
                    
                    self.ant_list[i].current_square = self.get_position(new_x, new_y)
                    
                    self.update_position(new_x, new_y, 2)

                if index % steps == 0:
                    mat_display.set_data(self.anthill.raw)
                    fig.canvas.draw_idle()
                    plt.pause(0.01)
                
                for i in range(len(self.ant_list)):
                    
                    x: int = self.ant_list[i].position[0]
                    y: int = self.ant_list[i].position[1]

                    self.anthill[x, y] = self.ant_list[i].current_square

                # debug
                if debug:
                    print(index)
                    for agent in self.ant_list: 
                        print(agent.position)
                                    

                index += 1
            
            except KeyboardInterrupt:  
                plt.ioff()
                break
        plt.pause(1)
        plt.close()
