import unittest
from maze import Maze

# Ignore the "cannot access" warnings, it runs fine.


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    #    def test_big_maze(self):
    #        num_cols = 100
    #        num_rows = 100
    #        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #        self.assertEqual(len(m1._Maze__cells), num_cols)
    #        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False)
        self.assertEqual(m1._Maze__cells[9][9].has_bottom_wall, False)

    def test_break_small(self):
        m1 = Maze(0, 0, 1, 1, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False)
        self.assertEqual(m1._Maze__cells[0][0].has_bottom_wall, False)

    def test_reset_visited(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        m1._Maze__reset_cells_visited()
        self.assertEqual(m1._Maze__cells[0][0].visited, False)
        self.assertEqual(m1._Maze__cells[4][5].visited, False)
        self.assertEqual(m1._Maze__cells[2][3].visited, False)
        self.assertEqual(m1._Maze__cells[9][9].visited, False)


if __name__ == "__main__":
    unittest.main()
