from tkinter import Tk, BOTH, Canvas


class Window:
    """Creates a Tk and Canvas object bundled into one. Has methods for updating, closing when the x is clicked,
    and drawing lines on the screen."""

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        """Refreshes the screen"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Updates the screen constantly while the program is running."""
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        """Draws a line on the screen. Takes a line object and a fill color as input. Fill color defaults to black."""
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False


class Point:
    """Creates an object that contains a single x and y coordinate."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    """Creates an object that containes two Point objects."""

    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        """Draws a line between each of the line's points. Takes a Canvas object and a fill color as inputs.
        Fill color defaults to black."""
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
