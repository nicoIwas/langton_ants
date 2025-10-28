# @nicoiwas
###################################
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from grid import map
from ant import ant
import time
###################################

if __name__ == "__main__":

    # cores
    colors = ["black", "white", "red"]
    # intervalos
    boundaries = [-0.5, 0.5, 1.5, 2.5]
    # linkando o colormap
    cmap = mcolors.ListedColormap(colors)
    norm = mcolors.BoundaryNorm(boundaries, cmap.N)

    anthill = map(250, 250).matrix
    ant = ant((125, 125))


    fig, ax = plt.subplots()
    set_matrix = anthill.copy()
    set_matrix[ant.position[0]][ant.position[1]] = 2
    mat_display = ax.matshow(set_matrix, cmap=cmap, norm=norm)
    plt.ion()
    plt.show()
    plt.pause(1)
    for i in range(1000000):

        if anthill[ant.position[0]][ant.position[1]] == 0:
            anthill[ant.position[0]][ant.position[1]] = 1
            ant.move("l")
            # ant.position = (ant.position[0] + 1, ant.position[1] - 1)
        elif anthill[ant.position[0]][ant.position[1]] == 1:
            anthill[ant.position[0]][ant.position[1]] = 0
            ant.move("r")
            # ant.position = (ant.position[0] - 1, ant.position[1] + 1)
        if i % 200 == 0:
            print(i)
            set_matrix = anthill.copy()
            set_matrix[ant.position[0]][ant.position[1]] = 2
            mat_display.set_data(set_matrix)
            fig.canvas.draw_idle()
            plt.pause(1)
