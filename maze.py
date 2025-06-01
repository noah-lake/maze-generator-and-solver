from cell import Cell
from time import sleep
import random


class Maze:
    # The maze strictly needs its upper leftmost corner (x1 and y1), the number of rows and number of columns in the maze,
    # the width of each cell (cel_size_x) and the height of each cell (cell_size_y). It can also accept a window object
    # (see graphics.py), and a seed for the randomness.
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        # Set some attributes
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        # Set the radomization state to the seed if one is provided.
        if seed:
            random.seed(seed)
        # Run the methods to create and solve the maze.
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.solve()

    def __create_cells(self):
        """Creates a two-dimensional list. The topmost lists are the columns, and each column contains a cell for each row.
        Then draws the cells onto the screen."""
        for cell in range(self.__num_cols):
            self.__cells.append([])
            for c in range(self.__num_rows):
                self.__cells[cell].append(Cell(self.__win))
        for column in range(len(self.__cells)):
            for row in range(len(self.__cells[column])):
                self.__draw_cells(column, row)

    def __draw_cells(self, column, row):
        """Calculates a point for each corner of a cell at a given index in the maze's __cells attribute
        then draws it."""
        # x1 is equal to the leftmost point of the maze (the x1 argument passed at initialization)
        # offset by the width of each cell multiplied by the current column.
        x1 = self.__x1 + self.__cell_size_x * column
        # y1 is equal to the topmost ppoint of the maze (the y1 argument passed at initialization)
        # offest by the height of each cell multiplied by the current row.
        y1 = self.__y1 + self.__cell_size_y * row
        # x2 is equal to x1 + the width of the cell
        x2 = x1 + self.__cell_size_x
        # y2 is equal to y1 + the height of the cell
        y2 = y1 + self.__cell_size_y
        # If the window exists (included for testing purposes)
        if self.__win:
            # Draw the cell, update the screen, sleep for a fraction of a second.
            self.__cells[column][row].draw(x1, y1, x2, y2)
            self.animate()

    def animate(self):
        """Updates the screen, then sleeps for a fraction of a second"""
        if self.__win:
            self.__win.redraw()
            sleep(0.005)

    def __break_entrance_and_exit(self):
        """Breaks the top wall of the upper leftmost cell (the entrance),
        and the bottom wall of the bottom rightmost cell (the exit)."""
        self.__cells[0][0].has_top_wall = False
        self.__draw_cells(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cells(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, column, row):
        """Breaks a random non-edge wall on each cell to create paths through the maze."""
        self.__cells[column][row].visited = True
        while True:
            neighbors = []

            # If the cell one column to the left of the current cell exists and has not been visited, it's a neighbor
            if column > 0 and not self.__cells[column - 1][row].visited:
                # Neighbors are recorded as a tuple containting their column (int), row (int),
                # and a direction (str) from the current cell.
                neighbors.append((column - 1, row, "left"))
            # If the cell one column to the right of the current cell exists and has not been visited, it's a neighnor
            if (
                column < self.__num_cols - 1
                and not self.__cells[column + 1][row].visited
            ):
                neighbors.append((column + 1, row, "right"))
            # If the cell one row above the current row (row -1, since row zero is the topmost row) exists and has
            # not been visited, it's a neighbor
            if row > 0 and not self.__cells[column][row - 1].visited:
                neighbors.append((column, row - 1, "up"))
            # If the cell one row below the current cell exists and has not been visited, it's a neighbor
            if row < self.__num_rows - 1 and not self.__cells[column][row + 1].visited:
                neighbors.append((column, row + 1, "down"))

            # If there are no neighbors, we're done.
            if len(neighbors) == 0:
                self.__draw_cells(column, row)
                return

            # Otherwise, pick a random neighbor
            direction = random.choice(neighbors)

            # Knock down the walls between the current cell and the selected neighbor
            if direction[2] == "right":
                self.__cells[column][row].has_right_wall = False
                self.__cells[column + 1][row].has_left_wall = False
            if direction[2] == "left":
                self.__cells[column][row].has_left_wall = False
                self.__cells[column - 1][row].has_right_wall = False
            if direction[2] == "down":
                self.__cells[column][row].has_bottom_wall = False
                self.__cells[column][row + 1].has_top_wall = False
            if direction[2] == "up":
                self.__cells[column][row].has_top_wall = False
                self.__cells[column][row - 1].has_bottom_wall = False

            # Then start the process over on the selected neighbor cell.
            self.__break_walls_r(direction[0], direction[1])

    # Sets the visited attribute for each cell to false.
    def __reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, column, row):
        """Searches for a path through the maze from a given starting cell (column, then row).
        If it reaches a dead end, it returns to the previous branch point and continues searching.
        Returns True if it found the path or False if it didn't."""
        self.animate()
        # Marks the current cell as visited so it isn't checked twice.
        self.__cells[column][row].visited = True
        # If we found the endpoint (the bottom rightmost cell) return True.
        if column == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True

        # Saves the current cell for readability
        current = self.__cells[column][row]

        # If there is a path in each direction, draw a line from the current cell to that cell in red and
        # call __solve_r recursively on the that cell. If it finds the exit, return True. If not, redraw the previous move in gray.

        # left
        if (
            column > 0
            and not self.__cells[column - 1][row].visited
            and not current.has_left_wall
            and not self.__cells[column - 1][row].has_right_wall
        ):
            current.draw_move(self.__cells[column - 1][row])
            if self.__solve_r(column - 1, row):
                return True
            current.draw_move(to_cell=self.__cells[column - 1][row], undo=True)
        # right
        if (
            column < self.__num_cols - 1
            and not self.__cells[column + 1][row].visited
            and not current.has_right_wall
            and not self.__cells[column + 1][row].has_left_wall
        ):
            current.draw_move(self.__cells[column + 1][row])
            if self.__solve_r(column + 1, row):
                return True
            current.draw_move(to_cell=self.__cells[column + 1][row], undo=True)
        # up
        if (
            row > 0
            and not self.__cells[column][row - 1].visited
            and not current.has_top_wall
            and not self.__cells[column][row - 1].has_bottom_wall
        ):
            current.draw_move(self.__cells[column][row - 1])
            if self.__solve_r(column, row - 1):
                return True
            current.draw_move(to_cell=self.__cells[column][row - 1], undo=True)
        # down
        if (
            row < self.__num_rows - 1
            and not self.__cells[column][row + 1].visited
            and not current.has_bottom_wall
            and not self.__cells[column][row + 1].has_top_wall
        ):
            current.draw_move(self.__cells[column][row + 1])
            if self.__solve_r(column, row + 1):
                return True
            current.draw_move(to_cell=self.__cells[column][row + 1], undo=True)
        # If there are no valid directions, this is a dead end, return False.
        return False
