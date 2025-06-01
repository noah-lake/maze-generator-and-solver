from graphics import Line, Point


class Cell:
    def __init__(self, window):
        """Creates an object that tracks two x values, two y values, four walls, a window, and if it has been visited or not.
        Coontains methods to draw the cell and to draw lines between cells. Takes a Window object as an input."""
        # A cell has all four walls by default.
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # A cell's coodrdinates are off the sceen by default.
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        # A cell has not been visited by default.
        self.visited = False


    def draw(self, x1, y1, x2, y2):
        """Draws a rectangle on the screen between each given coordinate. Takes x1 (leftmost point),
        y1 (topmost point), x2 (rightmost point) and y2 (bottommost point) as arguments"""
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        # Creates point objects for each corner.
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        # Creates line objects for each wall.
        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)

        # Checks to see if the cell has a given wall, draws the cooresponding line
        # in black if it does and white if it doesnt. Draw in white so that the
        # updates are visible when a cell loses a wall.
        if self.has_left_wall:
            self.__win.draw_line(left_wall)
        else:
            self.__win.draw_line(left_wall, "white")
        if self.has_top_wall:
            self.__win.draw_line(top_wall)
        else:
            self.__win.draw_line(top_wall, "white")
        if self.has_right_wall:
            self.__win.draw_line(right_wall)
        else:
            self.__win.draw_line(right_wall, "white")
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall)
        else:
            self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        """Draws a line from the center of the current cell to the center of another cell.
        Draws in red if undo=False and in gray if undo=True."""
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2
        x2 = (to_cell.__x1 + to_cell.__x2) / 2
        y2 = (to_cell.__y1 + to_cell.__y2) / 2
        start_point = Point(x1, y1)
        end_point = Point(x2, y2)
        line = Line(start_point, end_point)
        self.__win.draw_line(line, fill_color)
