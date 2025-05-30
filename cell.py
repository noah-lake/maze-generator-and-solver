from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)
        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)
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
