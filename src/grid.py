# @nicoiwas
##################
import numpy as np
##################

class map:

    def __init__(self, rows: int = 500, columns: int = 500):

        self.rows = rows
        self.columns = columns
        self.matrix = np.zeros((self.rows, self.columns))

