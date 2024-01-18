import unittest

from graphics import Window
from maze import Maze


class Tests(unittest.TestCase):

    def setUp(self):
        self.num_cols = 10
        self.num_rows = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)
    
    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.maze._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.maze._cells[0]),
            self.num_rows,
        )

    def test_entrance(self):
        entrance = self.maze.get_cell(0, 0)
        self.assertEqual(
            entrance.has_top_wall,
            False,
        )

    def test_exit(self):
        exit = self.maze.get_cell(self.num_rows-1, self.num_cols-1)
        self.assertEqual(
            exit.has_bottom_wall,
            False,
        )

if __name__ == "__main__":
    unittest.main()