from graphics import Window
from maze import Maze


def main():
    win = Window(915, 915)

    # 40 colums/rows is SOMETIMES too much for the program.
    maze = Maze(10, 10, 30, 30, 30, 30, win)

    win.wait_for_close()


main()
