from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 10, 90, 90, win)

    win.wait_for_close()


main()
