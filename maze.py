from cell import Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

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
            sleep(0.05)
