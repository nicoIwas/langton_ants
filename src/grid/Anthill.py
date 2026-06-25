# @nicoiwas
##################
import numpy as np
##################

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