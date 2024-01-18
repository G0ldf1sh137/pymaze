import time

from graphics import Window, Cell

class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = []
        for c in range(self._num_cols):
            cell_col: list[Cell] = []
            for r in range(self._num_rows):
                x1 = self._x1 + (r * self._cell_size_x)
                x2 = x1 + self._cell_size_x
                y1 = self._y1 + (c * self._cell_size_y)
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                cell_col.append(cell)
            self._cells.append(cell_col)

        for c in range(self._num_cols):
            for r in range(self._num_rows):
                self._draw_cell(c, r)
        

    def _draw_cell(self, i: int, j: int):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def get_cell(self, x: int, y: int) -> Cell:
        return self._cells[y][x]