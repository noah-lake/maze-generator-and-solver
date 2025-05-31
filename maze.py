from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed:
            random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for cell in range(self.__num_cols):
            self.__cells.append([])
            for c in range(self.__num_rows):
                self.__cells[cell].append(Cell(self.__win))
        for column in range(len(self.__cells)):
            for row in range(len(self.__cells[column])):
                self.__draw_cells(column, row)

    def __draw_cells(self, column, row):
        if column == 0:
            x1 = self.__x1
        else:
            x1 = self.__x1 + self.__cell_size_x * column
        if row == 0:
            y1 = self.__y1
        else:
            y1 = self.__y1 + self.__cell_size_y * row
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        if self.__win:
            self.__cells[column][row].draw(x1, y1, x2, y2)
            self.animate()

    def animate(self):
        if self.__win:
            self.__win.redraw()
            sleep(0.1)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cells(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cells(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, column, row):
        self.__cells[column][row].visited = True
        while True:
            neighbors = []

            if column > 0 and not self.__cells[column - 1][row].visited:
                neighbors.append((column - 1, row, "left"))
            if (
                column < self.__num_cols - 1
                and not self.__cells[column + 1][row].visited
            ):
                neighbors.append((column + 1, row, "right"))
            if row > 0 and not self.__cells[column][row - 1].visited:
                neighbors.append((column, row - 1, "up"))
            if row < self.__num_rows - 1 and not self.__cells[column][row + 1].visited:
                neighbors.append((column, row + 1, "down"))

            if len(neighbors) == 0:
                self.__draw_cells(column, row)
                return

            direction = random.choice(neighbors)

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

            self.__break_walls_r(direction[0], direction[1])
