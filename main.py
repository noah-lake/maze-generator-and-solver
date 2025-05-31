from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 5, 5, 90, 90, win)
    maze._Maze__break_entrance_and_exit()
    maze._Maze__break_walls_r(0, 0)

    win.wait_for_close()


main()
