from graphics import Window, Point, Line, Cell, Maze



def main():
    win = Window(800, 600)

    maze = Maze(10,10,12,10,50,50,win)
    c1 = maze.get_cell(1,5)
    c2 = maze.get_cell(2,5)
    c1.draw_move(c2)

    win.wait_for_close()



if __name__ == "__main__":
    main()