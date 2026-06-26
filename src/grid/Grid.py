# @nicoiwas
####################################
from src.agents.Ant import Ant
from src.grid.Anthill import Anthill
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
####################################

class Grid:

    def __init__(self, ant_list: list[Ant], columns: int = 500, rows: int = 500):

        # map itself (anthill... get it?)
        self.anthill: Anthill = Anthill(columns, rows)
        # the possibility of having the ants as a map for the grid to iterate on makes it easier to deal with everything
        self.ant_list: list[Ant] = ant_list

    # update position of the antill interface with the passed value
    def update_position(self,  x: int, y: int, value: int) -> None:
        
        self.anthill[x, y] = value

    # get value at defined position, x as collumn and y as row
    def get_position(self,  x: int, y: int) -> int:
        
        return self.anthill[x, y]
    
    def simulate(self, steps: int = 1, debug: bool = False) -> None:

        # cores dos pontos: 0 / 1 / formiga
        # colors = ["white", "black", "red", "blue"]
        # # intervalos de cores (respectivamente)
        # boundaries = [-0.5, 0.5, 1.5, 2.5, 3.5]
        
        # linkando o colormap
        # cmap = mcolors.ListedColormap(colors)
        # norm = mcolors.BoundaryNorm(boundaries, ncolors=cmap.N)

        fig, ax = plt.subplots() 

        # update each ant position to its correspondent color
        for i in range(len(self.ant_list)):
            
            x, y = self.ant_list[i].position
            self.ant_list[i].current_square = self.get_position(x, y)

        # update each ant position to its correspondent color
        for i in range(len(self.ant_list)):
            x, y = self.ant_list[i].position
            self.update_position(x, y, value=self.ant_list[i].ruleset["ant_color"])
            
        
        # rework is actually on the way
        mat_display = ax.matshow(self.anthill.raw, cmap="nipy_spectral", origin='lower')
        
        plt.ion()
        plt.draw()
        plt.pause(3)

        # throwback the grid colors to not have ant colors
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
                    
                for i in range(len(self.ant_list)):

                    x, y = self.ant_list[i].position
                    self.ant_list[i].move()
                    self.ant_list[i].color_buffer = self.get_position(x, y)
                    self.ant_list[i].position_buffer = (x, y)
                
                # update past position
                for i in range(len(self.ant_list)):

                    bufferd_x, buffered_y = self.ant_list[i].position_buffer
                    previous_square_color = self.ant_list[i].ruleset["current_color"][self.ant_list[i].current_square]["color_change"]
                    
                    self.update_position(bufferd_x, buffered_y, value=previous_square_color)
                    self.ant_list[i].correct_position(self.anthill.raw)
                    

                for i in range(len(self.ant_list)):
                    x, y = self.ant_list[i].position
                    self.ant_list[i].current_square = self.get_position(x, y)
                
                for i in range(len(self.ant_list)):
                    x, y = self.ant_list[i].position
                    self.update_position(x, y, self.ant_list[i].ruleset["ant_color"])

                if index % steps == 0:
                    if plt.fignum_exists(fig.number):
                        mat_display.set_data(self.anthill.raw)
                        fig.canvas.draw_idle()
                        plt.pause(0.01)
                    else:
                        raise Exception(">Closed Canvas; Stopping simulation")

                for i in range(len(self.ant_list)):
                    
                    x, y  = self.ant_list[i].position
                    self.update_position(x, y, self.ant_list[i].current_square)

                # debug
                if debug:
                    print(index)
                    for agent in self.ant_list: 
                        print(agent.position)

                index += 1
            # maybe add interactive actions here... what about a cli app?
            except Exception:
                plt.ioff()
                break
        plt.pause(1)
        plt.close()
